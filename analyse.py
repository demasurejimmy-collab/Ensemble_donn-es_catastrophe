#Analyse
df.describe(include="all")

# distribution des catatstrophes par pays
df['country'].value_counts().head(20)

# typologie des catastrophes les plus frequentes : 
df['disaster_type ]
   
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