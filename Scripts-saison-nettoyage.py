import pandas as pd
import numpy as np

df = pd.read_csv("seasonal-events-calendar.csv")


colonne_supprimee=['id','iso','country_wide','adm1','adm1_eng_name','comment','source','source_date','source_link']
df = df.drop(columns=colonne_supprimee)

df = df.sort_values(by='country')

df_filtre = df[df['event_type'].str.contains('hazard', case=False, na=False)]

df_filtre.to_csv("saisonnalite.csv", index=False)