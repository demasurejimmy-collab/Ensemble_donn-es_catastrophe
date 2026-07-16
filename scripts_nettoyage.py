## Scripts d'automatisation du nettoyage et de la traduction

import pandas as pd
import numpy as np

df = pd.read_csv("global_disaster_response_2018_2024.csv")

#harmoniser l'écriture des données :
df.columns = (df.columns.str.strip().str.lower().str.replace("","_").str.replace("","_"))
df.columns

#normaliser les colonnes :
df = pd.read_csv("global_disaster_response_2018_2024.csv", sep=",", encoding="utf-8")
print(df.columns)

#normaliser les noms de colonnes :
df.columns = df.columns.str.lower()

#convertir les types dates :
df["date"] = pd.to_datetime(df["date"], errors="coerce")


#supprimer les valeurs erronées :
def nettoyer_donnees(df):
    """Supprime les données physiquement impossibles."""

    # Filtrage géographique
    df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
    df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
    
    # Filtrage logique (pour les valeurs ne pouvant être que positives)
    cols_positives = ['casualties', 'economic_loss_usd', 'aid_amount_usd', 
                      'response_time_hours', 'recovery_days']

    for col in cols_positives:
        df = df[df[col] >= 0]
        
    return df

#suppression des lignes identiques :
df=df.drop_duplicates(df).reset_index(drop=True)

#suppression des lignes avec des valeurs manquantes et réassignation de l'index :
df=df.dropna(how='any').reset_index(drop=True)

#dictionnaire de traduction des types de catastrophes : 
mapping = {
    "Earthquake": "Tremblement de terre",
    "Flood": "Inondation",
    "Wildfire": "Feu de forêt",
    "Hurricane": "Ouragan",
    "Tornado": "Tornade",
    "Drought": "Sécheresse",
    "Volcanic Eruption": "Éruption volcanique",
    "Tsunami": "Tsunami",
    "Landslide": "Glissement de terrain",
    "Cyclone": "Cyclone",
    "Blizzard": "Blizzard",
    "Heatwave": "Canicule",
    "Extreme Heat": "Chaleur extrême",
    "Storm Surge": "Onde de tempête"
}

#traduction de la colonne disaster_type :
df["disaster_type"] = df["disaster_type"].map(mapping).fillna(df["disaster_type"])

#traduction des noms de colonnes :
traductions = {
    "date": "date",
    "country": "pays",
    "disaster_type": "type_catastrophe",
    "severity_index": "indice_severite",
    "casualties": "victimes",
    "economic_loss_usd": "pertes_economiques_usd",
    "response_time_hours": "temps_reponse_heures",
    "aid_amount_usd": "aide_financiere_usd",
    "response_efficiency_score": "score_efficacite_reponse",
    "recovery_days": "jours_retablissement",
    "latitude": "latitude",
    "longitude": "longitude"
}

df = df.rename(columns=traductions)

#export du CSV final
df.to_csv("catastrophe_donnees_nettoyees.csv", index=False)

print("CSV traduit et nettoyé généré : catastrophe_donnees_nettoyees.csv")