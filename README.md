# Diagnostic Data : ONG - Réponse d'urgence aux catastrophes naturelles

## 1. Contexte du projet
Ce projet a été réalisé dans le cadre d'un mandat pour le cabinet *Numeris Conseil*. L'objectif est de réaliser un diagnostic complet et rigoureux des données simulées d'ONG fournissant une réponse humanitaire d'urgence au catastrophes naturelles. Le diagnostic servira à rendre les données exploitables pour les équipes BI et pour des modélisations prédictives (ML).

## 2. Problématique Métier
"Comment optimiser la répartition des fonds d'urgence et le déploiement des équipes terrain en corrélant les types de sinistres, leur intensité par zone géographique sur la période 2018-2024 et les standards de prise en charge ?"

## 3. Dataset
- **Sujet :** Disaster & Emergency Response Dataset (2018–2024)
- **Source :** https://www.kaggle.com/datasets/emirhanakku/disaster-and-emergency-response-dataset-20182024
- **Description :** Données simulées couvrant 50 000 événements de catastrophes naturelles dans 20 pays.

## 4. Structure du projet
```text
Ensemble_données_catastrophe/
├── global_disaster_response_2018_2024   # Données brutes 
├── audit_qualite_donnees          # Notebooks de nettoyage 
├── requetes                # Schéma et requêtes SQL pour la BI
├── scripts                 # Python


├── .gitignore          # Fichiers ignorés par Git
├── plan_repartition    # Répartition des tâches dans l'équipe
├── README.md           # Descriptif du projet
├── requirements        # Bibliothèques nécessaires au projet
└── suivi               # Descriptif des étapes suivies