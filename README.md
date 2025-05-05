# Football Predictor

Système modulaire de prédiction des résultats de football avec crawling de données, stockage MySQL et entraînement de modèles ML.

## Structure du projet

```
football_predictor/
├── __init__.py
├── airflow/
│   ├── dags/
│   │   ├── base_football_dag.py
│   │   └── league_dags/
│   │       └── swiss_league_dag.py
│   ├── logs/
│   └── plugins/
├── api/
│   ├── __init__.py
│   └── server.py
├── config/
│   ├── __init__.py
│   ├── credentials.py
│   └── settings.py
├── core/
│   ├── __init__.py
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── base_extractor.py
│   │   └── google_search.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connector.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   └── models.py
│   └── ml/
│       ├── __init__.py
│       ├── features/
│       │   └── __init__.py
│       ├── features.py
│       ├── models/
│       │   └── __init__.py
│       ├── predict.py
│       └── train.py
├── leagues/
│   ├── __init__.py
│   ├── base.py
│   ├── premier_league/
│   │   └── __init__.py
│   └── swiss_league/
│       ├── __init__.py
│       ├── extractors.py
│       ├── features.py
│       └── transformers.py
├── logs/
├── README.md
├── requirements.txt
└── scripts/
```

## Installation

1. Créer un environnement virtuel : `python -m venv venv`
2. Activer l'environnement : 
   - Linux/Mac : `source venv/bin/activate`
   - Windows : `venv\Scripts\activate`
3. Installer les dépendances : `pip install -r requirements.txt`
4. Configurer les variables d'environnement dans un fichier `.env`

## Étapes d'implémentation

1. **Préparation de l'environnement**
   - Exécuter le script `setup_project.sh` pour créer la structure de base
   - Configurer les variables d'environnement
   - Installer les dépendances requises

2. **Configuration des API et de la base de données**
   - Créer un compte Google Custom Search API
   - Configurer MySQL sur le serveur avec port forwarding
   - Renseigner les credentials dans la configuration

3. **Développement par modules**
   - Module crawler : Implémentation de la récupération des données
   - Module DB : Configuration des modèles et connexion MySQL
   - Module ML : Développement du pipeline d'entraînement pour RTX3060

4. **Workflow Airflow**
   - Installation d'Airflow
   - Développement du DAG pour la Super League suisse
   - Configuration de la communication inter-serveurs

5. **Tests et déploiement**
   - Test de chaque composant
   - Optimisation des performances
   - Déploiement complet du système

6. **Extension à d'autres ligues**
   - Ajout de nouveaux modules pour d'autres championnats