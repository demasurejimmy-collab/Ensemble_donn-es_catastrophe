
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

##CONFIGURATION 

# Configuration du style
sns.set_theme(style="whitegrid")


# Chargement des données
df = pd.read_csv("catastrophe_donnees_nettoyees.csv")


# Définition de votre palette de couleurs (du plus critique au moins critique)
mes_couleurs = ["#EE0000", "#F92C2C", "#EC2B09", "#F6541D", "#FF6633",
                "#FFB406", "#FAC840", "#F2E85C", "#ADF675", "#BFF59B"]

## partie 1 : ________________________________________________________________________________________________________________________________

# 1.a Top 10 pays les plus touchés (en nombres d'évènements)
top_10 = df['pays'].value_counts().head(10).reset_index()
top_10.columns = ['pays', 'nombre']

plt.figure(figsize=(10, 6))
sns.barplot(data=top_10, x='pays', y='nombre', palette=mes_couleurs, hue='pays', legend=False)

plt.title("Top 10 pays par nombre d'événements", fontsize=14, pad=20)
plt.ylabel("Nombre d'événements")
plt.xlabel("Pays")
plt.xticks(rotation=45)
plt.ylim(2500, 2650)
sns.despine()
plt.tight_layout()
plt.show()

# 1.b Top 10 pays les plus touchés (en nombres de victimes)
df_victims = df.groupby('pays')['victimes'].sum().reset_index()
df_victims = df_victims.sort_values(by='victimes',ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=df_victims, x='pays', y='victimes', palette=mes_couleurs, hue='pays', legend=False)

plt.title("Top 10 pays par nombre de victimes", fontsize=14, pad=20)
plt.ylabel("Nombre total de victimes")
plt.xlabel("Pays")
plt.xticks(rotation=45)
plt.ylim(251000, 265000)
sns.despine()
plt.tight_layout()
plt.show()

# 2. Continents les plus touchés (proportionnalité : plus de pays européens et asiatiques)
continent_map = {
    'France':'Europe', 'Turkey': 'Europe', 'Germany': 'Europe', 'Greece': 'Europe',
    'Spain': 'Europe', 'Italy': 'Europe', 'United States': 'Amérique du Nord',
    'Canada': 'Amérique du Nord', 'Mexico': 'Amérique du Nord', 'Brazil': 'Amérique du Sud',
    'Chile': 'Amérique du Sud', 'China': 'Asie', 'India': 'Asie',
    'Bangladesh': 'Asie', 'Indonesia' : 'Asie', 'Philippines' : 'Asie',
    'Japan': 'Asie', 'Australia': 'Océanie', 'Nigeria': 'Afrique', 'South Africa': 'Afrique',
}

df['continent'] = df['pays'].map(continent_map)
plt.figure(figsize=(8, 5))
continents = df['continent'].value_counts().reset_index()
continents.columns = ['continent', 'nombre']

sns.barplot(data=continents, x='continent', y='nombre', palette=mes_couleurs, hue='continent', legend=False)
plt.title("Répartition des catastrophes par continent", fontsize=14, pad=20)
plt.ylabel("Nombre d'événements")
plt.xlabel("Continent")
sns.despine()
plt.show()

# Ajout colonne mois (necessaire à l'analyse)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['mois'] = df['date'].dt.month
df.to_csv("catastrophe_donnees_nettoyees.csv", index=False)

# 3. Types de catastrophes les plus fréquents
df['type_catastrophe'].value_counts().plot(kind='bar', figsize=(12,5))
plt.title("Types de catastrophes les plus fréquents")
plt.xlabel("Type de catastrophes")
plt.ylabel("Nombre d'événements")
plt.xticks(rotation=45)
plt.ylim(4800, 5300)
plt.show()

# 4. Croisement Type × Zone géographique
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

# 5.Nombre de catastrophes par année
# Extraction de l’année

df['year'] = df['date'].dt.year

counts_year = df['year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
counts_year.plot(kind='line', marker='o', linewidth=2, color='steelblue')
plt.title("Nombre de catastrophes par année")
plt.xlabel("Année")
plt.ylabel("Nombre d'événements")
plt.grid(True)
plt.show()

# 6. Distribution de l'indice de sévérité
df['indice_severite'].plot(kind='hist', bins=30, figsize=(10,5))
plt.title("Distribution de l'indice de sévérité")
plt.xlabel("Sévérité")
plt.ylabel("Nombre d'événements")
plt.show()

# 7. Nombre d'événements par mois, pays, type (page externe)
agg = df.groupby(['mois', 'pays', 'type_catastrophe']).size().reset_index(name='nb')

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
 #-------------
 # Masquer tous les titres d'axes Y individuels
fig.update_yaxes(title_text="")

# Ajouter une annotation centrée à gauche pour faire office d'axe Y unique
fig.add_annotation(
    dict(
        x=-0.07,  # Position horizontale (ajustez selon votre besoin)
        y=0.5,    # Position verticale (centré)
        text="Nombre d'événements",
        textangle=-90,
        showarrow=False,
        xref="paper",
        yref="paper",
        font=dict(size=14)
    )
)

# Ajuster les marges pour laisser de la place à l'annotation
fig.update_layout(
    barmode="group",
    margin=dict(l=80) 
)

fig.show()
#-----------------

##fig.update_layout(barmode="group")
##fig.show()

# partie 2 : ______________________________________________________________________________________________________________________________________________________________

# 8. Analyse des pertes économiques
bins = range(0,11)
labels = [f"{i}-{i+1}" for i in range(10)]
df['groupe_severite'] = pd.cut(df['indice_severite'], bins=bins, labels=labels, include_lowest=True)
df['pertes_millions'] = (df['pertes_economiques_usd'] / 1_000_000).astype(int)
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='groupe_severite', y='pertes_millions', palette="viridis")
plt.title("Distribution des pertes économiques par tranche d'intensité (0-10)", fontsize=14)
plt.xlabel("Tranche d'intensité", fontsize=12)
plt.ylabel("Pertes économiques (en millions USD)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 9. Pertes majeures :👉 Les 25 % événements les plus coûteux sont considérés comme majeurs (en terme de dégats* : nous avons interpreter la colonne #pertes économiques dans le sens impact/dégats économiques résultants de la catastrophe).
seuil_pertes_majeures = df['pertes_economiques_usd'].quantile(0.75)
df['categorie_pertes'] = np.where(df['pertes_economiques_usd'] >= seuil_pertes_majeures,'Majeur','Standard')
df.to_csv("catastrophes_nettoyees.csv", index=False)

df_majeurs = df[df['categorie_pertes'] == 'Majeur'].copy()
df_majeurs = df_majeurs.sort_values(by='pertes_economiques_usd', ascending=False)
tableau_majeurs = df_majeurs[['date','pays','type_catastrophe', 'indice_severite', 'pertes_millions']]
tableau_majeurs.columns = ['Date', 'Pays', 'Catastrophe', 'Intensité', 'Pertes (M$ USD)']
print(tableau_majeurs.head(10).to_string(index=False))
print("\n")

# 10. Aides majeures : 👉 Les 25 % événements les plus coûteux en terme d'aides financières
seuil_aides_majeures = df['aide_financiere_usd'].quantile(0.75)
df['categorie_aide'] = np.where(df['aide_financiere_usd'] >= seuil_aides_majeures,'Budget Exceptionnel','Enveloppe Standard')
df.to_csv("catastrophes_nettoyees.csv", index=False)

df_majeures = df[df['categorie_aide'] == 'Budget Exceptionnel'].copy()
df_majeures = df_majeures.sort_values(by='aide_financiere_usd', ascending=False)
tableau_majeures = df_majeures[['date','pays','type_catastrophe', 'indice_severite', 'aide_financiere_usd']]
tableau_majeurs.columns = ['Date', 'Pays', 'Catastrophe', 'Intensité', 'Aides (M$ USD)']
print(tableau_majeurs.head(10).to_string(index=False))


# 11. Calcul du risque d'un événement : sa fréquence, son intensité et son coût
risk = df.groupby('continent').agg(
    frequence=('type_catastrophe', 'count'),
    intensite=('indice_severite', 'mean'),
    cout_total=('pertes_economiques_usd', 'sum') # Le total est plus parlant pour le risque cumulé
)

scaler = MinMaxScaler(feature_range=(0, 1))
risk_norm = pd.DataFrame(scaler.fit_transform(risk), columns=risk.columns, index=risk.index)

risk_norm['score_final'] = (
    (risk_norm['frequence'] * 0.2) + 
    (risk_norm['intensite'] * 0.3) + 
    (risk_norm['cout_total'] * 0.5)
) * 10

plt.figure(figsize=(10, 6))
risk_norm['score_final'].sort_values(ascending=False).plot(kind='bar', color='salmon')
plt.title("Score de Risque Composite (1 à 10) par Continent")
plt.ylabel("Score de Risque")
plt.xlabel("Continent")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#partie 3 : ______________________________________________________________________________________________________________________________________________________________

# 12. Pertes économiques moyennes par région

vals = df.groupby('continent')['pertes_economiques_usd'].mean().sort_values()

plt.figure(figsize=(12,6))
ax = vals.plot(
    kind='bar',
    color=sns.color_palette("viridis", len(vals))
)

plt.title("Pertes économiques moyennes par région (optimisé)")
plt.xlabel("Région")
plt.ylabel("Pertes moyennes en million (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.ylim(vals.min() - 50000, vals.max() + 50000)

for i, v in enumerate(vals):
    ax.text(i, v + 20000, f"{v:,.0f}", ha='center', fontweight='bold')

plt.show()

# 13. Temps de réponse des équipes

plt.figure(figsize=(10,5))
df['temps_reponse_heures'].plot(kind='hist', bins=30)
plt.title("Distribution du temps de réponse")
plt.xlabel("Heures")
plt.grid(True)
plt.show()

# 14. Score d'efficacité

plt.figure(figsize=(10,5))
sns.scatterplot(data=df, x='temps_reponse_heures', y='score_efficacite_reponse')
plt.title("Temps de réponse vs efficacité")
plt.xlabel("Temps de réponse (h)")
plt.ylabel("Score d’efficacité")
plt.grid(True)
plt.show()
