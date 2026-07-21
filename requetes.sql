


--nbr d'evenements par pays: commentaire : Permet d’identifier les-- 
--zones les plus exposées → priorisation des ressources--

SELECT p.nom_pays, COUNT(*) AS nb
FROM evenements e
JOIN pays p ON e.id_pays = p.id_pays
GROUP BY p.nom_pays
ORDER BY nb DESC;



--nbr d'evenements par type  : Permet de comprendre quels types de-- 
--catastrophes dominent → pilotage des politiques de prévention.--

SELECT t.libelle_type, COUNT(*) AS nb
FROM evenements e
JOIN type_catastrophe t ON e.id_type = t.id_type
GROUP BY t.libelle_type
ORDER BY nb DESC;



--Pertes économiques par continent : Permet d’identifier les zones-- 
--où les catastrophes coûtent le plus → allocation budgétaire.--

SELECT p.continent, SUM(e.pertes_economiques) AS pertes_totales
FROM evenements e
JOIN pays p ON e.id_pays = p.id_pays
GROUP BY p.continent
ORDER BY pertes_totales DESC;



--Délai d’intervention moyen par pays : Permet d’évaluer la --
--performance des équipes de réponse → KPI opérationnel.--

SELECT p.nom_pays, AVG(e.delai_intervention) AS delai_moyen
FROM evenements e
JOIN pays p ON e.id_pays = p.id_pays
GROUP BY p.nom_pays
ORDER BY delai_moyen ASC;



--Croisement type * continent : Permet de comprendre quels types --
--de catastrophes touchent quelles régions → segmentation géographique.--

SELECT t.libelle_type, p.continent, COUNT(*) AS nb
FROM evenements e
JOIN type_catastrophe t ON e.id_type = t.id_type
JOIN pays p ON e.id_pays = p.id_pays
GROUP BY t.libelle_type, p.continent
ORDER BY t.libelle_type, nb DESC;



