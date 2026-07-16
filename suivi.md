# Journal de bord du projet

Ce fichier sert de suivi quotidien. Chaque fin de journée, il précise nos avancées, les obstacles et les décisions prises.

---

### Historique des entrées

| Date | Phase | Tâche effectuée | Problème / Arbitrage |
| :--- | :--- | :--- | :--- |
| **---** | **AUDIT DE QUALITE** | **---** | **---** |
| 15/07 | Set d'observation des données | dataset relativement propre | Décision : Créer un script de nettoyage permettant la correction et la traduction automique pour tout nouveau dataset . |
| **---** | **NETTOYAGE** | **---** | **---** |
| 15/07 | Nettoyage | Harmonisation de l'écriture et de la ponctuation | Pratique standard |
| 15/07 | Nettoyage | Normalisation des colonnes | Pratique standard |
| 15/07 | Nettoyage | Convertir les types de dates | Pratique standard |
| 15/07 | Nettoyage | Détecter les valeurs abérrantes | Décision : filtrage géographique et logique (valeurs positives) |
| 16/07 | Nettoyage | Suppression doublons | Décision : Supprimer car erreurs de saisie + réassignation de l'index|
| 16/07 | Nettoyage | Gestion valeurs manquantes | Décision : Suppression des lignes contenant des valeurs manquantes. Les données vides empêcheraient la cohérence de l'analyse. 
| 16/07 | Nettoyage | Traduction des typologies de catastrophes | Décision : Traduction en français pour s'adapter la langue du client |
| **---** | **ANALYSE** | **---** | **---** |
| 17/07 | Analyse | Calcul corrélations | Ras : Tout est cohérent. |
| **---** | **REQUÊTES** | **---** | **---** |
| 18/07 | Requêtes | Optimisation index | Problème : Temps de réponse lent. Arbitrage : Ajout index sur colonne ID. |

---

### Instructions pour les prochaines entrées
* **Date :** Format JJ/MM/AAAA.
* **Tâche :** Description concise de l'action principale.
* **Problème :** Blocage technique, doute sur la méthodologie ou manque d'information.
* **Arbitrage :** La solution retenue ou la direction prise pour débloquer la situation.


