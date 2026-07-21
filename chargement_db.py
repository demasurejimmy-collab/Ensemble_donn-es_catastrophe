import sqlite3
import pandas as pd


def normalize_text(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip()


# Charger le CSV nettoyé
df = pd.read_csv("catastrophe_donnees_nettoyees.csv")
df["pays"] = normalize_text(df["pays"])
df["continent"] = normalize_text(df["continent"])
df["type_catastrophe"] = normalize_text(df["type_catastrophe"])

# Connexion à la base SQLite
conn = sqlite3.connect("db.sqlite")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()

# Créer les tables si elles n'existent pas
cur.execute("""
CREATE TABLE IF NOT EXISTS pays (
    id_pays INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_pays TEXT NOT NULL UNIQUE,
    continent TEXT NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS type_catastrophe (
    id_type INTEGER PRIMARY KEY AUTOINCREMENT,
    libelle_type TEXT NOT NULL UNIQUE
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS evenements (
    id_event INTEGER PRIMARY KEY AUTOINCREMENT,
    date_event DATE,
    intensite REAL,
    pertes_economiques REAL,
    delai_intervention INTEGER,
    id_pays INTEGER NOT NULL,
    id_type INTEGER NOT NULL,
    FOREIGN KEY (id_pays) REFERENCES pays(id_pays),
    FOREIGN KEY (id_type) REFERENCES type_catastrophe(id_type)
)
""")

# Recharger proprement les données pour éviter les doublons et les incohérences
cur.execute("DELETE FROM evenements")
cur.execute("DELETE FROM pays")
cur.execute("DELETE FROM type_catastrophe")
conn.commit()

# Insérer les pays
pays_uniques = df[['pays', 'continent']].drop_duplicates()
for _, row in pays_uniques.iterrows():
    cur.execute("""
        INSERT INTO pays (nom_pays, continent)
        VALUES (?, ?)
    """, (row['pays'], row['continent']))

# Récupérer les ID pays
cur.execute("SELECT id_pays, nom_pays FROM pays")
map_pays = {nom: id for id, nom in cur.fetchall()}

# Insérer les types de catastrophes
types_uniques = df['type_catastrophe'].drop_duplicates()
for type_cat in types_uniques:
    cur.execute("""
        INSERT INTO type_catastrophe (libelle_type)
        VALUES (?)
    """, (type_cat,))

# Récupérer les ID types
cur.execute("SELECT id_type, libelle_type FROM type_catastrophe")
map_types = {nom: id for id, nom in cur.fetchall()}

# Insérer les événements
for idx, row in df.iterrows():
    pays_id = map_pays.get(row['pays'])
    type_id = map_types.get(row['type_catastrophe'])

    if pays_id is None or type_id is None:
        print(f"Ligne {idx}: pays '{row['pays']}' ou type '{row['type_catastrophe']}' introuvable dans la base")
        continue

    cur.execute("""
        INSERT INTO evenements (
            date_event, intensite, pertes_economiques,
            delai_intervention, id_pays, id_type
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        row['date'],
        row['indice_severite'],
        row['pertes_economiques_usd'],
        row['temps_reponse_heures'],
        pays_id,
        type_id
    ))

conn.commit()
conn.close()

print("Données insérées avec succès !")
