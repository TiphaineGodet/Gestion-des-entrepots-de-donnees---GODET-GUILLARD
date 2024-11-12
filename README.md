# Gestion-des-entrepots-de-donnees-GODET-GUILLARD

## Technologies Utilisées

### Langage

![Python](https://img.shields.io/badge/Python-3.10.12-blue?logo=python&logoColor=white)


### Cloud & Bases de Données

![MongoDB](https://img.shields.io/badge/MongoDB-5.0-green?logo=mongodb&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue?logo=postgresql&logoColor=white)


### Bibliothèques de Données & Machine Learning

![Pandas](https://img.shields.io/badge/Pandas-1.5.2-brightgreen?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21.0-blue?logo=numpy&logoColor=white)

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


## 🎭 Cibles
- **Utilisateurs de Vélos en Libre-Service (Cyclistes)** Les cyclistes pourraient utiliser les données croisées pour choisir les meilleures périodes pour louer un vélo, en fonction de la météo et de la disponibilité des stations Belib.
  
- **Gestionnaires des Systèmes de Vélo** (Opérateurs Belib)** Les opérateurs peuvent utiliser les données pour mieux gérer l'implantation et la disponibilité des vélos dans certaines stations. Par exemple, des stations peuvent être réapprovisionnées en vélos pendant les jours où la météo est favorable à l'utilisation de vélos.
   
- **Autorités Locales et Urbanistes** Les autorités de la ville de Paris ou des urbanistes pourraient utiliser ces données pour optimiser la planification des infrastructures de transport urbain, améliorer l’accessibilité et encourager l’utilisation des vélos.
   
- **Assureurs et Sociétés de Transport** Les assureurs et les entreprises de transport pourraient utiliser ces informations pour mieux comprendre l'impact de la météo sur la sécurité des cyclistes et sur la demande de transport en vélo.
   
- **Chercheurs et Analystes en Mobilité Urbaine** Les chercheurs peuvent analyser les comportements de mobilité des citadins en fonction de facteurs externes comme la météo. Cela pourrait contribuer à des études sur les modes de transport durables et la manière dont les conditions météorologiques influencent le choix des moyens de transport.
   
- **Développeurs d'Applications et Startups** Des entreprises tech ou des startups dans le domaine de la mobilité urbaine pourraient utiliser ces données pour créer des applications ou des services qui optimisent l’utilisation des vélos partagés en fonction de la météo.
   
- **Touristes et Visiteurs à Paris** Les touristes peuvent profiter d'une application qui leur fournit des conseils sur les conditions de voyage en vélo à Paris, en prenant en compte la météo.
  
