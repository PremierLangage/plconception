
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

1° Il faut qu'il y ai des données:
Avoir des exercices présents dans la base de données et un certain nombres d'exercice réalisés par des 
étudiants pour pouvoir analyser les résultats.
2° Que l'utilisateur soit un analyste (soit un prof pour son cours, soit un responsable d'une formation pour tout les cours de la formation). 
3° Le cas d'utilisation démarre quand l'option du menu général "analysis" est choisie.


## Scénario 

l'interface d'analyse apparait, la liste des activités produisant des "traces" (pour le moment 20/8/2019 uniquement des answers) est affiché avec un check box de selection pour chaque.

Puis pour tout les activités sélectionner un certains nombre de choix sont proposés :
- afficher tout les answers 
- export en json 
- export en csv 

le cas d'utilisation se termine quand l'acteurs change de page sur le site.



