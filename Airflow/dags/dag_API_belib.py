from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import requests

# Charger les variables d'environnement pour les tâches Airflow
load_dotenv()

# Définir les arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),  # Ajustez la date de début
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définir le DAG
dag = DAG(
    'belib_data_ingestion_dag',
    default_args=default_args,
    description='Récupère les données depuis l\'API Belib et les insère dans MongoDB',
    schedule_interval='0 * * * *',  # Exécution toutes les heures
)

# Classes BelibAPIClient et MongoDBPipeline
class BelibAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self, limit=50):
        try:
            print(f"Récupération des données depuis l'API : {self.api_url} avec une limite : {limit}")
            response = requests.get(self.api_url, params={'limit': limit})
            print(f"Code de statut de la réponse : {response.status_code}")
            if response.status_code == 200:
                json_data = response.json()
                total_records = json_data.get('total_count', None)
                records = json_data.get('results', [])
                return records, total_records
            else:
                print(f"Échec de la récupération des données. Code de statut : {response.status_code}")
                return None, None
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None, None


class MongoDBPipeline:
    def __init__(self):
        load_dotenv()
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.dbname = os.getenv('MONGO_DBNAME')
        self.mongodb_uri = os.getenv('MONGO_URL')

        if not self.username or not self.password or not self.dbname or not self.mongodb_uri:
            raise ValueError("Les informations de connexion MongoDB sont manquantes.")

        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.dbname]
        self.collection = self.db['belib']

    def insert_data_to_mongodb(self, data):
        try:
            if data:
                result = self.collection.insert_many(data)
                print(f"{len(result.inserted_ids)} documents insérés.")
            else:
                print("Aucune donnée à insérer.")
        except Exception as e:
            print(f"Erreur lors de l'insertion : {e}")

    def close_connection(self):
        self.client.close()
        print("Connexion MongoDB fermée.")


# Fonction principale
def main():
    api_url = os.getenv("API_URL")
    if not api_url:
        print("L'API_URL n'est pas définie.")
        return

    api_client = BelibAPIClient(api_url)
    data, total_records = api_client.fetch_data(limit=50)

    if data:
        print(f"{len(data)} enregistrements récupérés.")
        mongo_pipeline = MongoDBPipeline()
        mongo_pipeline.insert_data_to_mongodb(data)
        mongo_pipeline.close_connection()
    else:
        print("Échec de la récupération des données.")

# Définir la tâche Airflow
ingest_data_task = PythonOperator(
    task_id='ingest_belib_data',
    python_callable=main,
    dag=dag,
)
