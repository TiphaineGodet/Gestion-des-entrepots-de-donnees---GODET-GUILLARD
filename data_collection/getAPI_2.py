import requests
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime

class WeatherAPIClient:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            # Afficher l'URL de l'API utilisée
            print(f"Récupération des données depuis l'API : {self.api_url}")
            response = requests.get(self.api_url)
            print(f"Code de statut de la réponse : {response.status_code}")
            
            if response.status_code == 200:
                # Convertir la réponse en JSON
                json_data = response.json()
                print(f"Structure des données récupérées : {json_data}")  # Affichage des données
                return json_data, 1  # Retourne l'ensemble des données et un total fictif
            else:
                print(f"Échec de la récupération des données. Code : {response.status_code}, Réponse : {response.text}")
                return None, None
        except Exception as e:
            print(f"Une erreur s'est produite lors de la récupération des données de l'API : {e}")
            return None, None

class MongoDBPipeline:
    def __init__(self):
        # Charger les variables d'environnement
        load_dotenv()

        # Récupérer les informations de connexion depuis les variables d'environnement
        self.username = os.getenv('MONGO_USERNAME')
        self.password = os.getenv('MONGO_PASSWORD')
        self.dbname = os.getenv('MONGO_DBNAME')
        self.mongodb_uri = os.getenv('MONGO_URL')

        # Vérifier si l'URL MongoDB est définie
        if not self.mongodb_uri:
            raise ValueError("L'URL MongoDB n'est pas définie dans les variables d'environnement.")

        # Initialiser la connexion à MongoDB
        try:
            self.client = MongoClient(self.mongodb_uri, tls=True)
            self.db = self.client[self.dbname]  # Connexion à la base de données
            self.collection = self.db['weather']  # Nom de la collection
            print("Connexion réussie à MongoDB Atlas !")
        except Exception as e:
            print(f"Erreur lors de la connexion à MongoDB Atlas : {e}")
            exit()

    def convert_timestamp(self, data):
        """Convertir les timestamps en dates lisibles."""
        if 'dt' in data:
            try:
                # Convertir le champ 'dt' en une date UTC lisible
                data['dt_converted'] = datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S UTC')
            except Exception as e:
                print(f"Erreur lors de la conversion du timestamp : {e}")
        return data

    def insert_data_to_mongodb(self, data):
        try:
            if data:
                # Convertir les timestamps avant l'insertion
                data = self.convert_timestamp(data)

                # Insérer un document unique dans MongoDB
                result = self.collection.insert_one(data)
                print(f"Document inséré dans MongoDB avec l'_id : {result.inserted_id}")
            else:
                print("Aucune donnée à insérer.")
        except Exception as e:
            print(f"Erreur lors de l'insertion des données dans MongoDB : {e}")

    def close_connection(self):
        # Fermer la connexion MongoDB
        self.client.close()
        print("Connexion à MongoDB fermée.")

def main():
    # Charger les variables d'environnement
    load_dotenv()

    # URL de l'API OpenWeatherMap
    api_url = "http://api.openweathermap.org/data/2.5/weather?q=Paris&appid=aea2f47b02f42c9f78ad703ba4045069"
    if not api_url:
        print("L'API_URL n'est pas définie dans le fichier .env.")
        return

    # Créer une instance du client API
    api_client = WeatherAPIClient(api_url)

    # Récupérer les données depuis l'API
    data, total_records = api_client.fetch_data()
    if data:
        print(f"Données récupérées avec succès depuis l'API.")
        if total_records is not None:
            print(f"Nombre total d'enregistrements traités : {total_records}")
        
        # Initialiser le pipeline MongoDB
        mongo_pipeline = MongoDBPipeline()

        # Insérer les données dans MongoDB
        mongo_pipeline.insert_data_to_mongodb(data)

        # Fermer la connexion MongoDB
        mongo_pipeline.close_connection()
    else:
        print("Échec de la récupération des données depuis l'API.")

if __name__ == "__main__":
    main()
