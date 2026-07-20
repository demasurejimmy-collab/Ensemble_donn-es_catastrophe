
# Comment optimiser la répartition des fonds d'urgence et le déploiement des équipes terrain en corrélant les types de sinistres, leur intensité par zone géographique sur la période 2018-2024?

-Années couvertes : 2018–2024
-Régions : 20 pays sur tous les continents
-Records : 50 000 événements simulés de catastrophe
-Attributs : 12 variables descriptives et numériques

**RECAP IMPACT/CARACTERISTIQUES CATASTROPHES :** 

Top 10 : les pays les plus touchés par les catastrophes ->  Brésil, l'Australie, la Turquie, le Bangladesh et l'Espagne avec plus de 2540 catastrophes par pays de 2018 à 2023. 

Top 10 : les pays comptabilisants le plus grand nombre de victimes toutes catastrophes confondues de 2028 à 2024 sont le Brésil, la Turquie, la Chine,l'Australie avec tous plus de 256000 victimes (le Brésil à plus de 262000)

Les continents les plus touchés sont majoritairement l'Europe et l'Asie avec plus de 14000 événements chacun sur la période 

Les trois catastrophes les plus fréquentes (toutes zones géographiques confondues sur l'ensemble de la période) sont les glissements de terrain, les tremblements de terre et les innondations 

On observe un pic d'événements entre 2020 et 2021 (+200 événements par an/7200). L'augmentation étant nettement observable depuis 2019. 

On observe que la plus grosse partie des événements a un indice d'intensité entre 3 et 7 avec un pic autour de 5

**Analyse Croisée : Diagnostic des Incohérences Opérationnelles - INTERPRETATION**
1. Vigilence sur l'attribution des fonds en fonction de la classification de la catastrophe : 

Point critique : En catégorisant les catastrophes comme majeures ou standards (majeures = 25% les plus couteuses en termes de dégâts) ainsi que les aides financières en "budget exceptionnel" ou "enveloppe standard" (budget exceptionnel = 25% des plus grosses enveloppes d'aides), on observe que certaines catastrophes considérées comme standard ont reçu des budgets exceptionnels et à l'inverse de certaines catastrophes majeures ont reçues des enveloppes standards.

Conséquences : Les catastrophes majeures recevant des enveloppes standard subissent un risque accru de défaillance logistique et à l'inverse les catastrophes standard recevant un trop perçu s'exposent à des risques de fraude.

Explication : Les catastrophes comptabilisant le plus (top 10) de pertes économiques (entre 22 et 24M$), et ayant un niveau d'intensité élévé, sont également celles recevant le plus d'aides, ce qui démontre une réponse adaptée. Cependant les quelques anomalies relevées (susmentionnées) peuvent mettre en avant une défaillance du système de décision actuel d'allocation des aides pouvant être biaisé par des facteurs subjectifs sur certaines catastrophes : poids politique du pays, visibilité médiatique, etc.


2. Adaptabilité de l'aide à la nature de la catastrophe et ses impacts : 

Point critique : Les glissements de terrain sont majoritaires, mais l'Afrique est dominée par les tremblements de terre.

Conséquences : Les tremblements de terre causant des dommages structurels plus conséquents que les glissements de terrain (prédominant ailleurs), l'Afrique affiche ainsi les pertes économiques unitaires les plus élevées (moyenne > 5M$). 

Explication : Il semble que les paquets d'aide pré-determiné soient standardisés. Ainsi, l'aide ne s'adapte pas à la typologie du risque local impactant le coût unitaire sur le continent Africain (5 103 153$).

3. Reactivité adaptée face à l'indice du risque

Point critique : On observe que pour plus de 90% des catastrophes, l'aide apportée a été realisée en moins de 30 heures. Cependant, on observe que plus la réponse est longue, moins elle est efficace (l'impact de la catastrophe sur les population peut alors continuer de croître). #cqfd

Explications : Les zones à haut risque (Asie (9.41) /Europe (8.94)), determinées par la fréquence, l'intensité, et l'impact financier,  bénéficient d'un "effet de proximité" ou d'infrastructures plus denses, ce qui maintient une efficacité élevée du système d'aide malgré la haute fréquence. À l'inverse, une catastrophe dans une zone à score moyen/faible (ex: certaines régions d'Afrique ou d'Océanie) subit une "latence logistique" pouvant transformer un événement standard en crise majeure.
 
4. Proposer une réponse régionale

Point critique: Il existe un volume massif d'événements à intensité moyenne (3 à 7).

Conséquences : Le risque n'est pas uniquement dans le pic d'intensité (10), mais dans l'accumulation des intensités. Ces événements, pris isolément, semblent "standards", mais leur fréquence cumulée épuise les budgets exceptionnels destinés aux crises majeures.

Explication : Risque de "mort par mille coupures"-> La stratégie actuelle de gestion de crise traite chaque événement individuellement au lieu de gérer le flux continu.

### 5. Matrice d'Actions 

| Quandrant | Catarestique | Stratégie Préconisée|
| :--- | :--- | :--- |
| **Urgence Critique** | Score Risque > 8 ET Majeur | Déclenchement automatique des fonds et déploiement immédiat (Plan A). | 
| **Dérive Budgétaire** | Standard ET Budget Exceptionnel| Audit immédiat : pourquoi l'aide dépasse-t-elle le besoin estimé ? |
| **Sous-financement** | Majeur ET Budget Standard | Réaffectation prioritaire : risque de catastrophe humanitaire majeure. | 
| **Gestion des flux** | Intensité moyenne ET Fréquence haute| Passage à la maintenance préventive : infrastructures résilientes plutôt que secours d'urgence.| 

6. Limites du Dataset
- Dataset fictif 
- Période courte ne permettant pas une analyse temporelle et des variations sur plusieurs décénies 
- Dataset peut représentatif des réelles catastrophes naturelles (ex: proportion extrême de tremblements terre en France avec des vicitmes comptabilisées)
- Manque de "réalité" dans les données ne permettant une correlation saisonnière -> Par exemple, il n'a pas été possible de montrer que certaines innondations auraient pu s'expliquer par la période des pluies et des typhons dans les pays concernés (ce qui aurait permis de proposer un type d'aide spécifique)
- Pour certaines colonnes et indicateurs, aucune information contextuelles disponibles empêchant la bonne compréhension des chiffres et laissant place à une interprétation personnelle. 













