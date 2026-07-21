# Journal de bord du projet

Ce fichier sert de suivi quotidien. Chaque fin de journée, il précise nos avancées, les obstacles et les décisions prises.

---

### Historique des entrées

| Date | Phase | Tâche effectuée | Commentaires |
| :--- | :--- | :--- | :--- |
| **---** | **AUDIT DE QUALITE** | **---** | **---** |
| 15/07 | Set d'observation des données | dataset relativement propre | Décision : Créer un script de nettoyage permettant la correction et la traduction automique pour tout nouveau dataset . |
| **---** | **NETTOYAGE** | **---** | **Problèmes/Arbritrages** |
| 15/07 | Nettoyage | Harmonisation de l'écriture et de la ponctuation | Pratique standard |
| 15/07 | Nettoyage | Normalisation des colonnes | Pratique standard |
| 15/07 | Nettoyage | Convertir les types de dates | Pratique standard |
| 15/07 | Nettoyage | Détecter les valeurs abérrantes | Décision : filtrage géographique et logique (valeurs positives) |
| 16/07 | Nettoyage | Suppression doublons | Décision : Supprimer car erreurs de saisie + réassignation de l'index|
| 16/07 | Nettoyage | Gestion valeurs manquantes | Décision : Suppression des lignes contenant des valeurs manquantes. Les données vides empêcheraient la cohérence de l'analyse. 
| 16/07 | Nettoyage | Traduction des typologies de catastrophes | Décision : Traduction en français pour s'adapter la langue du client |
| **---** | **ANALYSE** | **KPIs** | **INFOS** |
| 17/07 | Analyse | Top 10 pays par nombre d'événements | Met en avant les pays les plus impactés par les catastrophes - Top 10 pays |
| 17/07 | Analyse | Top 10 pays par nombre de victimes | Met en avant les pays ayant le grand nombre de victimes du aux catastrophes - Top 10 pays |
| 17/07 | Analyse | Nombre de catastrophes par continent | Met en avant la répartition du nombre de catastrophes total sur chaque continent |
| 17/07 | Analyse | Types de catastrophes les plus fréquents (10)| Permet de rendre compte des catastrophes les plus recensées |
| 17/07 | Analyse | Croisement type de catastrophes vs zones géographiques | Permet de rendre compte des types de catastrophes les plus courrantes sur chaque continent |
| 17/07 | Analyse | Nombre total de catastrophes par an | Permet une vision de la totalité des catastrophes par années  |
| 17/07 | Analyse | Distribution (répartition) de l'indice de sévérité (entre 0 et 10) | Permet de rendre compte de la proportion du nombres d'événements par tranche de sévérité. |
| 20/07 | Analyse | Distribution (répartition) des catastrophes par pays, mois et type d'événement | Permet, par pays, de se rendre compte de la correlation, existante ou non, entre la période de la catastrophe et le type d'événement (pouvant êtes liés à des phénomènes météréologiques de saison) |
| 20/07 | Analyse | Distribution (répartition) des pertes économiques par tranche d'intensité (entre 0 et 10) | Permet de rendre compte de l'impact financier de chaque tranche d'intensité |
| 20/07 | Analyse | Pertes majeures : les 25 % événements les plus coûteux | Permet de faire ressortir les événements catégorisés comme "Majeurs" en raison des pertes économiques dues à la catastrophe |
| 20/07 | Analyse | Aides majeures :les 25 % événements les plus coûteux | Permet  de faire ressortir les événements pour lesquelles un bugdet exceptionnel a été alloué|
| 20/07 | Analyse | Score de risque (de 1 à 10) par continent : fréquence x intensité x pertes économiques | Le score de risque permet de prioriser les zones nécessitant un déploiement renforcé. ✔ Score faible → catastrophes peu fréquentes et peu graves → aides légères, prévention minimal ✔ Score moyen → catastrophes régulières ou modérément graves → renforcement des équipes, fonds de prévention ✔ Score élevé → catastrophes fréquentes ET graves → déploiement massif, fonds d’urgence, réparation, pré‑positionnement des ressources.|
| 20/07 | Analyse | Pertes économiques moyennes par continent | Determine le niveau de pertes économiques par continent |
| 20/07 | Analyse | Distribution (répartition) du temps de réponse selon l'intensité de la catastrophe | Permet d'observer une correlation potentielle entre l'intensité de la catastrophe et le temps de réponses des équipes d'aides déployées |
| 20/07 | Analyse | Score d'efficacité : Temps de réponse vs efficacité |Permet de mettre en avant l'efficacité des équipes sur place dans leur réponse fournie |
| **---** | **REQUÊTES** | **TITRES** | **INFOS** |
| 21/07 | Requêtes | nombre d'événements par pays | Infos : Permet d'identifier les zones les plus exposées: Priorisation des ressources |
| 21/07 | Requêtes | nombre d'événements par types | Infos : Permet de comprendre quels types de catastrophes dominent : Pilotage des politiques de prévention |
| 21/07 | Requêtes | pertes économiques par continent | Infos : Permet d'identifier les zones où les catastrophes coûtent le plus : Allocation budgétaire |
| 21/07 | Requêtes | délais d'intervention moyen par pays | Infos : Permet d'évaluer la performance des équipes de réponses : KPIs opérationnels |
| 21/07 | Requêtes | croisement type vs continent | Infos : Permet de comprendre quels types de catatrophes touchent quelles régions : Ségmentation géographique |
**---** | **PILOTAGE** | **---** | **---** |
| 21/07 | Création et mise à jour du REAMDE, fichier de suivi et plan de répartition | Mise à jour continue chaque jour |

---

### Instructions pour les prochaines entrées
* **Date :** Format JJ/MM/AAAA.
* **Tâche :** Description concise de l'action principale.
* **Problème :** Blocage technique, doute sur la méthodologie ou manque d'information.
* **Arbitrage :** La solution retenue ou la direction prise pour débloquer la situation.


