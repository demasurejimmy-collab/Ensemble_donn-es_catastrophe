import pandas as pd
df = pd.read_csv("catastrophe_donnees_nettoyees")

#🟦 Distribution des catastrophes par pays et regroupement par zone
df['country'].value_counts().head(20)

#Visualisation : Top 10 pays les plus touchés 
import matplotlib.pyplot as plt

df['country'].value_counts().head(10).plot(kind='bar', figsize=(10,5))
plt.title("Top 10 pays les plus touchés")
plt.xlabel("Pays")
plt.ylabel("Nombre d'événements")
plt.xticks(rotation=45)
plt.show()

#Regrouper par zone géographique
continent_map = {
    'France':'Europe',
    'Turkey': 'Europe',
    'Germany': 'Europe',
    'Greece': 'Europe',
    'Spain': 'Europe',
    'Italy': 'Europe',
    'United States': 'Amérique du Nord',
    'Canada': 'Amérique du Nord',
    'Mexico': 'Amérique du Nord',
    'Brazil': 'Amérique du Sud',
    'Chile': 'Amérique du Sud',
    'China': 'Asie',
    'India': 'Asie',
    'Bangladesh': 'Asie',
    'Indonesia' : 'Asie',
    'Philippines' : 'Asie',
    'Japan': 'Asie',
    'Australia': 'Océanie',
    'Nigeria': 'Afrique',
    'South Africa': 'Afrique',
}

df['continent'] = df['country'].map(continent_map)
df['continent'].value_counts()

#Visualisation : 
df['continent'].value_counts().plot(kind='bar', figsize=(8,5))
plt.title("Répartition des catastrophes par continent")
plt.xlabel("Continent")
plt.ylabel("Nombre d'événements")
plt.show()

#Cartographie simple (scatter plot lat/long) :
plt.figure(figsize=(10,6))
plt.scatter(df['longitude'], df['latitude'], alpha=0.4, s=20)
plt.title("Localisation des catastrophes dans le monde")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()



#Analyse des valeurs extrêmes :
def identifier_donnees_extremes_metier(df):
    """
    Marque les événements comme 'Majeur' si les critères du tableau sont atteints.
    Critères classe 5 : >= 1000 victimes OU >= 3 000 000 000 euros.
    """
    # Conversion des unités : 3 Md€ = 3 000 000 000
    seuil_victimes = 1000
    seuil_eco = 3_000_000_000
    
    # Utilisation de np.where avec une condition OU (|)
    df['statut_catastrophe'] = np.where(
        (df['casualties'] >= seuil_victimes) | (df['economic_loss_usd'] >= seuil_eco),
        'Majeur',
        'Standard'
    )
    return df

# --- Application ---
df_propre = nettoyer_donnees(df)
df_final = identifier_donnees_extremes_metier(df_propre)

# Pour examiner les catastrophes extrêmes séparément :
donnees_extremes = df_final[df_final['statut_catastrophe'] == 'Majeur']

# Pour examiner les cas normaux :
donnees_normales = df_final[df_final['statut_catastrophe'] == 'Standard']