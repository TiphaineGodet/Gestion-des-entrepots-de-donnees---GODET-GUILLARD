# Gestion-des-entrepots-de-donnees-GODET-GUILLARD

## Technologies Utilisées

### Langage

![Python](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)


### Cloud & Bases de Données

![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green?logo=mongodb&logoColor=white)

### Automatisation

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.6.3-darkblue?logo=apache-airflow&logoColor=white)

### Outils de Visualisation

![Kibana](https://img.shields.io/badge/Kibana-8.15.0-orange?logo=kibana&logoColor=white)

---

## Objectif du Projet

Ce projet a pour objectif de mettre en place un flux de gestion et d’analyse de données en plusieurs étapes, depuis leur extraction jusqu’à leur visualisation. Le processus est structuré pour automatiser l’acquisition, le traitement et la valorisation des données afin d’en extraire des insights utiles.

## Étapes du Projet

Récupération des Données via API :
    Les données sont extraites de deux API externes pour collecter les informations nécessaires. Ces sources apportent des informations sur les belib à Paris ainsi que des données de météo comme la température, pluviométrie etc.

Stockage Initial des Données :
    Les données récupérées sont stockées dans une base de données MongoDB pour garantir leur persistance et faciliter les traitements ultérieurs.

Transformation des Données :
    Les données brutes sont ensuite transformées et nettoyées à l'aide d'un script pour s’assurer de leur cohérence, fiabilité et pertinence pour les analyses. Ce processus peut inclure la normalisation, le filtrage ou l'enrichissement des données.

Restockage des Données Transformées :
    Les données nettoyées et enrichies sont stockées dans un entrepôt de données PosgreSQL, facilitant l'accès rapide aux données prêtes pour l’analyse.

Visualisation des Données :
    Pour valoriser les données, des visualisations interactives sont créées, permettant de générer des insights visuels et des rapports. Ces visualisations sont essentielles pour l’analyse de tendances et l’aide à la décision.


## 🎯 Cibles
- **Utilisateurs de Belib en Libre-Service ** Les utilisateurs pourraient utiliser les données croisées pour choisir les meilleures périodes pour utiliser les bornes, en fonction de la météo et de la disponibilité des stations Belib.
  
- **Gestionnaires des Systèmes de bornes (Opérateurs Belib)** Les opérateurs peuvent utiliser les données pour mieux gérer l'implantation et la disponibilité des bornes dans certaines stations. 
   
- **Autorités Locales et Urbanistes** Les autorités de la ville de Paris ou des urbanistes pourraient utiliser ces données pour optimiser la planification des infrastructures de transport urbain, améliorer l’accessibilité et encourager l’utilisation des belib.
   
- **Assureurs et Sociétés de Transport** Les assureurs et les entreprises de transport pourraient utiliser ces informations pour mieux comprendre l'impact de la météo sur la sécurité et sur la demande de transport.
   
- **Chercheurs et Analystes en Mobilité Urbaine** Les chercheurs peuvent analyser les comportements de mobilité des citadins en fonction de facteurs externes comme la météo. Cela pourrait contribuer à des études sur les modes de transport durables et la manière dont les conditions météorologiques influencent le choix des moyens de transport.
   
- **Développeurs d'Applications et Startups** Des entreprises tech ou des startups dans le domaine de la mobilité urbaine pourraient utiliser ces données pour créer des applications ou des services qui optimisent l’utilisation des vélos partagés en fonction de la météo.
   
- **Touristes et Visiteurs à Paris** Les touristes peuvent profiter d'une application qui leur fournit des conseils sur les conditions de voyage à Paris, en prenant en compte la météo.


## Architecture du Projet 

```
.
├── Airflow
│   └── dags
│   └── └── _pycache_
│   └── └── └── dag_API_belib.cpython-310.pyc
│   └── └── └── dag_API_meteo.cpython-310.pyc
│   └── └── └── dag_API_cpython-310.pyc
│   └── └── dag_API_belib.py
│   └── └── dag_API_meteo.py
│   └── script
│   └── └── entrypoint.sh
│   └── confi_airflow.md
│   └── docker-compose.yml
│   └── requirements.txt
├── data_collection
│   ├── getAPI_2.py
│   ├── getAPI.py
├── ELK
│   ├── docker-compose.yml
│   ├── export_mongodb_collections_fixed.csv
│   ├── export-donnees
├── .env
├── .gitignore
├── config.yml
├── README.md

```

## Workflow et Schéma d'Architecture

1. **Ingestion des Données de Belib (opendata.paris.fr)** :
   - Extraction des informations sur les locations de belib à Paris, envoi des données dans une collection belib sur MongoDB .

2. **Ingestion des informations météo (infoclimat.fr)** :
   - Extraction des données de météo sur Paris en temps réel avec l'api openweathermap.org  (température, pluviométrie etc) envoie des données dans une collection weather sur MongoDB.

3. **Traitement des Données** :
   - Agrégation par la date et stockage grace au code export-donnees dans un fichier csv export_multiple_collection_fixed.csv

4. **Visualisation et Analyse** :
   - Kibana est utilisé pour créer des tableaux de bord interactifs, permettant de faire des analyses croisées des données des bornes de recharge Belib et de la météo.




**Configurer les variables d'environnement :**
   Créez un fichier `.env` et renseignez les informations de connexion MongoDB , OPENAI , le topic kafka , le lien de l'api et Elasticsearch :
   ```env
MONGO_USERNAME="******"
MONGO_PASSWORD="******"
MONGO_DBNAME="*******"
MONGO_URI="*********"
API_URL="*********"

   ```
  
## 🛑 **Difficultés Rencontrées**  

1. **Choix de l'API**  
   - Identifier une API fiable fournissant des données complètes et pertinentes a été une étape complexe.  
   - Certaines APIs testées ne proposaient pas de données en temps réel ou nécessitaient une authentification complexe.  


2. **Insertion dans MongoDB**  
   - La structure des données issues de l'API a nécessité des transformations avant l'insertion dans MongoDB.  
   - Des problèmes de compatibilité et des erreurs de validation ont ralenti l'insertion dans MongoDB.  

3. **Automatisation avec Apache Airflow**  
   - Intégrer des workflows automatisés et s’assurer de leur fiabilité a demandé une montée en compétence sur cet outil.  
   - Des erreurs dans la configuration des DAGs ont parfois causé des échecs imprévus.  

4. **Analyse sur Kibana**  
   - L’apprentissage de Kibana a été compliqué, car l’équipe n’avait pas d’expérience avec cet outil.
  
5. **Problème de configuration**  
   - On s'était organisé pour créer deux branches afin de pousser nos codes chacun de notre côté. Mais à cause des problèmes de configuration (notamment pour le lancement d'Airflow) et d'un manque de connaissance, l'ensemble des codes ont été lancés depuis un PC, ce qui a ralenti l'avancé du projet.    

---

## 🌟 **Compétences Développées**  

1. **Maîtrise des APIs**  
   - Compréhension  des mécanismes des API : authentification, formats JSON, gestion des erreurs.  

2. **Bases de données NoSQL**  
   - Manipulation de MongoDB : création de collections, gestion des schémas flexibles, et insertion des données.  

3. **Orchestration de flux de travail**  
   - Utilisation d’Apache Airflow pour automatiser la collecte, la transformation, et le stockage des données.  

4. **Visualisation des données**  
   - Création de tableaux de bord avec Kibana pour analyser et interpréter les données des stations Belib'.  

5. **Résolution de problèmes complexes**  
   - Identifier et corriger des bugs liés aux intégrations, aux workflows, et aux transformations de données.  

6. **Travail collaboratif et méthodologie**  
   - Application de bonnes pratiques en gestion de projet (versionning).  
