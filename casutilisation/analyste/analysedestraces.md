
# Analyse les traces

Objectif : Permettre à l'analyste de faire des statistiques sur les exercices pour les analyser afin de savoir ceux qui 
sont les plus efficaces, ceux qui induisent l'étudiant en erreur etc.

Résumé général : Cherche à trouver des informations intéressantes à propos des exercices dans la base de données : le taux de réussite des exercices, le temps passé dessus, le nombre d'essais avant la réussite de l'exercice, etc...
L'analyste choisit un ensemble de données, soit tous les exercices fait par un élève, une classe, un niveau, un type de cours. Soit toutes les réalisations d'un exercice ou d'un type d'exercice/ensemble d'exercice.
Ensuite il choisit les paramètres/propriété/valeurs qu'il souhaite voir sur cet ensemble de données.
Ensuite il choisit le format d'affichage.
Le système affiche les données dans le mode d'affichage choisi et l'analyste peut enfin 
analyser les données. 

# Données

Acteur Principal : Analyste

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un analyste veut analyser des données.



## Pré-conditions

Avoir des exercices présents dans la base de données et un certain nombres d'exercice réalisés par des 
étudiants pour pouvoir analyser les résultats.

Le use case [Login](../utilisateur/login.md)
Le use case choisir son rôle.
Les use case permettant la réalisation d'exercices ([créer exercice](../createur/createexercice.md), [faire exercice](../etudiant/faireexercice.md))


## Post Conditions

En cas de succès : Il peut faire l'analyse des données obtenues à partir des exercices. Il peut créer un indicateur à partir des ces résultats.

En cas d'échec : Affiche une erreur lors de l'analyse des traces


# Navigation / IHM 

Demande d'analyse des données par l'analyste depuis son tableau de bord.
Accès à la base de données, recherche des informations en lien avec ce que l'analyste a demandé, analyse ces données.


## Scénarios

MAIN SUCCESS SCENARIO
S	[Analyse des informations demandées par l'analyste, affichage des données trouvées]
1	[Commence lorsque l'analyste souhaite accéder à ses statistiques]
2   [L'analyste choisit les paramètres et les données sur lesquels il veut avoir des statistiques]
3	[Accès à la base de données, analyse les données demandé par l'analyste suivant les paramètres qu'il a choisit]
4	[Plusieurs statistiques disponibles pour l'analyste issus de l'analyse de ces données]


# RELATED INFORMATION

Include Use Cases    [Login](../utilisateur/login.md)


<!--- 
Author : Raphael
Validator : Hugo
-->


