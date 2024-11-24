from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Définir les arguments par défaut pour le DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),  # Date de début
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définir le DAG
dag = DAG(
    'weather_data_ingestion_dag',
    default_args=default_args,
    description='Récupère les données météo depuis l\'API OpenWeather et les insère dans MongoDB',
    schedule_interval='0 * * * *',  # Exécution toutes les heures
)


# Classe pour récupérer les données de l'API météo
class WeatherAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            print(f"Récupération des données depuis l'API : {self.api_url}")
            response = requests.get(self.api_url)
            print(f"Code de statut de la réponse : {response.status_code}")

            if response.status_code == 200:
                json_data = response.json()
                print(f"Données récupérées avec succès.")
                return json_data
            else:
                print(f"Échec de la récupération des données. Code : {response.status_code}, Réponse : {response.text}")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération des données de l'API : {e}")
            return None


# Classe pour insérer les données dans MongoDB
class MongoDBPipeline:
    def __init__(self):
        # Charger les variables d'environnement
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.dbname = os.getenv('MONGO_DBNAME')
        self.mongodb_uri = os.getenv('MONGO_URL')

        # Vérification des informations de connexion
        if not self.username or not self.password or not self.dbname or not self.mongodb_uri:
            raise ValueError("Les informations de connexion MongoDB sont manquantes.")

        # Connexion à MongoDB
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.dbname]
        self.collection = self.db['weather']

    def insert_data_to_mongodb(self, data):
        try:
            if data:
                result = self.collection.insert_one(data)
                print(f"Document inséré dans MongoDB avec l'_id : {result.inserted_id}")
            else:
                print("Aucune donnée à insérer.")
        except Exception as e:
            print(f"Erreur lors de l'insertion dans MongoDB : {e}")

    def close_connection(self):
        self.client.close()
        print("Connexion MongoDB fermée.")


# Fonction principale appelée par le DAG
def fetch_weather_data():
    # URL de l'API météo (avec clé d'accès)
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=aea2f47b02f42c9f78ad703ba4045069"

    # Initialiser le client API
    api_client = WeatherAPIClient(api_url)

    # Récupérer les données depuis l'API
    data = api_client.fetch_data()
    if data:
        print(f"Données récupérées avec succès depuis l'API.")

        # Initialiser le pipeline MongoDB
        mongo_pipeline = MongoDBPipeline()

        # Insérer les données dans MongoDB
        mongo_pipeline.insert_data_to_mongodb(data)

        # Fermer la connexion MongoDB
        mongo_pipeline.close_connection()
    else:
        print("Aucune donnée récupérée depuis l'API.")


# Définir la tâche Airflow
fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    dag=dag,
)
