
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Configuration du style
sns.set_theme(style="whitegrid")


# Chargement des données
df = pd.read_csv("catastrophe_donnees_nettoyees.csv")


# Définition de votre palette de couleurs (du plus critique au moins critique)
mes_couleurs = ["#EE0000", "#F92C2C", "#EC2B09", "#F6541D", "#FF6633",
                "#FFB406", "#FAC840", "#F2E85C", "#ADF675", "#BFF59B"]


# 🟦 1. Préparation et Visualisation : Top 10 pays
top_10 = df['pays'].value_counts().head(10).reset_index()
top_10.columns = ['pays', 'nombre']


plt.figure(figsize=(10, 6))
sns.barplot(data=top_10, x='pays', y='nombre', palette=mes_couleurs, hue='pays', legend=False)


plt.title("Top 10 pays les plus touchés", fontsize=14, pad=20)
plt.ylabel("Nombre d'événements")
plt.xlabel("Pays")
plt.xticks(rotation=45)
plt.ylim(2500, 2650) # Zoom pour mieux voir les différences
sns.despine()
plt.tight_layout()
plt.show()


# 2. Regroupement par zone géographique
continent_map = {
    'France':'Europe', 'Turkey': 'Europe', 'Germany': 'Europe', 'Greece': 'Europe',
    'Spain': 'Europe', 'Italy': 'Europe', 'United States': 'Amérique du Nord',
    'Canada': 'Amérique du Nord', 'Mexico': 'Amérique du Nord', 'Brazil': 'Amérique du Sud',
    'Chile': 'Amérique du Sud', 'China': 'Asie', 'India': 'Asie',
    'Bangladesh': 'Asie', 'Indonesia' : 'Asie', 'Philippines' : 'Asie',
    'Japan': 'Asie', 'Australia': 'Océanie', 'Nigeria': 'Afrique', 'South Africa': 'Afrique',
}


df['continent'] = df['pays'].map(continent_map)


# 3. Visualisation : Répartition par continent
plt.figure(figsize=(8, 5))
continents = df['continent'].value_counts().reset_index()
continents.columns = ['continent', 'nombre']


sns.barplot(data=continents, x='continent', y='nombre', palette=mes_couleurs, hue='continent', legend=False)
plt.title("Répartition des catastrophes par continent", fontsize=14, pad=20)
sns.despine()
plt.show()

# Ajout colonne mois
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['mois'] = df['date'].dt.month
df.to_csv("catastrophe_donnees_nettoyees.csv", index=False)

# Types de catastrophes les plus fréquents
df['type_catastrophe'].value_counts().plot(kind='bar', figsize=(12,5))
plt.title("Types de catastrophes les plus fréquents")
plt.xlabel("Type")
plt.ylabel("Nombre")
plt.xticks(rotation=45)
plt.ylim(4800, 5300)
plt.show()

# Croisement Type × Zone
cross = pd.crosstab(df['type_catastrophe'], df['continent'])

plt.figure(figsize=(14,6))
sns.heatmap(cross, annot=True, fmt='d', cmap='Oranges')

# Highlight max par continent
for continent in cross.columns:
    top_type = cross[continent].idxmax()
    y = cross.index.tolist().index(top_type)
    x = cross.columns.tolist().index(continent)
    plt.gca().add_patch(plt.Rectangle((x, y), 1, 1, fill=False, edgecolor='red', lw=3))

plt.title("Croisement Type × Zone géographique (highlight max)")
plt.show()


#1) Extraction de l’année

df['year'] = df['date'].dt.year


#2) Comptage des catastrophes par année

counts_year = df['year'].value_counts().sort_index()
print(counts_year)


#3) Visualisation : évolution annuelle

plt.figure(figsize=(10,5))
counts_year.plot(kind='line', marker='o', linewidth=2, color='steelblue')
plt.title("Nombre de catastrophes par année")
plt.xlabel("Année")
plt.ylabel("Nombre")
plt.grid(True)
plt.show()

df['indice_severite'].plot(kind='hist', bins=30, figsize=(10,5))
plt.title("Distribution de l'indice de sévérité")
plt.xlabel("Sévérité")
plt.show()


import plotly.express as px
import pandas as pd

# Assure la date + mois
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['mois'] = df['date'].dt.month

# Agrégat : nombre d'événements par mois, pays, type
agg = df.groupby(['mois', 'pays', 'type_catastrophe']).size().reset_index(name='nb')

# Graphique interactif Plotly
fig = px.bar(
    agg,
    x="mois",
    y="nb",
    color="pays",
    facet_col="type_catastrophe",
    facet_col_wrap=3,
    title="Catastrophes par mois, pays et type",
    labels={"mois": "Mois", "nb": "Nombre d'événements", "pays": "Pays"}
)

fig.update_layout(barmode="group")
fig.show()

# partie 2 : ______________________________________________________________________________________________________________________________________________________________

#Analyse des pertes économiques
df['pertes_economiques_usd'].describe()
df['pertes_economiques_usd'].plot(kind='hist', bins=30, figsize=(10,5))
plt.title("Distribution des pertes économiques")
plt.xlabel("Pertes (USD)")
plt.show()
#Pertes majeures :👉 Les 25 % événements les plus coûteux sont considérés comme majeurs.
seuil_pertes_majeures = df['pertes_economiques_usd'].quantile(0.75)
seuil_pertes_majeures

df['pertes_majeures'] = df['pertes_economiques_usd'] >= seuil_pertes_majeures
#Analyse croisée : Sévérité × Pertes économiques 👉 Ce graphique te permet de voir si les catastrophes les plus graves sont aussi les plus coûteuses.

sns.scatterplot(data=df, x='indice_severite', y='pertes_economiques_usd')
plt.title("Sévérité vs pertes économiques")
plt.xlabel("Indice de sévérité")
plt.ylabel("Pertes économiques (USD)")
plt.show()
#Intégration des pertes économiques dans le scoring
risk = df.groupby(['continent', 'date']).agg(
    frequence=('type_catastrophe', 'count'),
    intensite=('indice_severite', 'mean'),
    cout_moyen=('pertes_economiques_usd', 'mean'))
risk['score_risque'] = risk['frequence'] * risk['intensite'] * risk['cout_moyen']
risk

risk['score_risque'].unstack().plot(kind='bar', figsize=(12,6))
plt.title("Score de risque (Fréquence × Sévérité × Pertes) par zone et par année")
plt.xlabel("Zone")
plt.ylabel("Score de risque")
plt.show()




"""#indices severite/victimes
# 1) Création d’un indice combiné victimes + ressources
df['indice_majeur'] = df['victimes'] + df['aide_financiere_usd']

# 2) Calcul du seuil majeur (quantile 75%)
seuil_majeur = df['indice_majeur'].quantile(0.75)

# 3) Ajout d’une colonne booléenne
df['seuil_majeur'] = df['indice_majeur'] >= seuil_majeur

print("Seuil majeur :", seuil_majeur)

plt.figure(figsize=(14,6))

sns.heatmap(
    cross,
    annot=True,
    fmt='d',
    cmap='Reds',
    linewidths=1,
    linecolor='black'
)

plt.title("Catastrophes dépassant le seuil majeur (victimes + ressources $)")
plt.xlabel("Dépasse le seuil majeur")
plt.ylabel("Type de catastrophe")
plt.xticks([0.5, 1.5], ["Non", "Oui"])
plt.yticks(rotation=0)

plt.show()

plt.figure(figsize=(14,6))
ax = sns.heatmap(
    cross,
    annot=True,
    fmt='d',
    cmap='Reds',
    linewidths=1,
    linecolor='black'
)

# Highlight de la catastrophe la plus grave
max_val = cross[True].max()
max_type = cross[True].idxmax()

y = list(cross.index).index(max_type)
x = 1  # colonne True

ax.add_patch(plt.Rectangle((x, y), 1, 1, fill=False, edgecolor='blue', lw=3))

plt.title("Catastrophes dépassant le seuil majeur (highlight)")
plt.xlabel("Dépasse le seuil majeur")
plt.ylabel("Type de catastrophe")
plt.xticks([0.5, 1.5], ["Non", "Oui"])
plt.yticks(rotation=0)

plt.show()


# Graphique interactif
fig = px.bar(
    agg,
    x="mois",
    y="nb",
    color="pays",
    facet_col="type_catastrophe",
    facet_col_wrap=3,
    title="Catastrophes par mois, pays et type",
    labels={"mois": "Mois", "nb": "Nombre d'événements", "": "Pays"}
)

fig.update_layout(barmode="group")
fig.show()


plt.figure(figsize=(12,6))
ax = risk['score_risque'].unstack().plot(kind='bar', figsize=(12,6), colormap='Reds')

plt.title("Score de risque par zone et par année")
plt.xlabel("Zone géographique")
plt.ylabel("Score de risque")
plt.xticks(rotation=45)
plt.grid(True)

"""

#partie 3 : ______________________________________________________________________________________________________________________________________________________________

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================================
# 1) Pertes économiques moyennes par région
# ============================================================


vals = df.groupby('continent')['pertes_economiques_usd'].mean().sort_values()

plt.figure(figsize=(12,6))
ax = vals.plot(
    kind='bar',
    color=sns.color_palette("viridis", len(vals))
)

plt.title("Pertes économiques moyennes par région (optimisé)")
plt.xlabel("Région")
plt.ylabel("Pertes moyennes (USD)")
plt.xticks(rotation=45)
plt.grid(True)

# Zoom sur les différences
plt.ylim(vals.min() - 50000, vals.max() + 50000)

# Ajouter les valeurs
for i, v in enumerate(vals):
    ax.text(i, v + 20000, f"{v:,.0f}", ha='center', fontweight='bold')

plt.show()



# ============================================================
# 4) Heatmap régionale (fréquence × intensité × pertes)
# ============================================================

heat = df.groupby('continent').agg(
    frequence=('type_catastrophe', 'count'),
    intensite=('indice_severite', 'mean'),
    pertes=('pertes_economiques_usd', 'mean')
)

plt.figure(figsize=(10,6))
sns.heatmap(heat, annot=True, cmap='Oranges')
plt.title("Heatmap : Fréquence × Intensité × Pertes par région")
plt.show()

# ============================================================
# 5) Proportionnalité des ressources engagées     ne generent rien 
# ============================================================

df['ressources_theoriques'] = df['indice_severite'] * df['pertes_economiques_usd']
df['ratio_proportionnalite'] = df['aid_amount_usd'] / (df['ressources_theoriques'] + 1)

plt.figure(figsize=(10,5))
df['ratio_proportionnalite'].plot(kind='hist', bins=30, color='purple')
plt.title("Distribution du ratio de proportionnalité des ressources")
plt.xlabel("Ratio (aide réelle / aide théorique)")
plt.grid(True)
plt.show()

# ============================================================
# 6) Détection des hotspots (zones les plus sollicitées)    ne generent rien
# ============================================================

hotspots = df.groupby('continent').agg(
    frequence=('disaster_type', 'count'),
    intensite=('indice_severite', 'mean'),
    pertes=('pertes_economiques_usd', 'sum'),
    aide=('aid_amount_usd', 'sum')
)

plt.figure(figsize=(12,6))
hotspots[['frequence', 'pertes', 'aide']].plot(kind='bar')
plt.title("Hotspots : fréquences, pertes et aide par région")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# ============================================================
# 7) Temps de réponse des équipes     ne generent rien 
# ============================================================

plt.figure(figsize=(10,5))
df['response_time_hours'].plot(kind='hist', bins=30)
plt.title("Distribution du temps de réponse")
plt.xlabel("Heures")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='response_time_hours', y='response_efficiency_score')
plt.title("Temps de réponse vs efficacité")
plt.xlabel("Temps de réponse (h)")
plt.ylabel("Score d’efficacité")
plt.grid(True)
plt.show()
