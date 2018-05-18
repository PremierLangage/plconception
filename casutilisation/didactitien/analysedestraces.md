
# Analyse les traces
Objectif : Permettre au didactitien de faire des statistiques sur les exercices pour les analyser afin de savoir ceux qui 
sont les plus efficaces, ceux qu'induisent l'élève en erreur etc.

Résumé général : Le didactitien choisit un ensemble de données, soit tout les exercices fait par un élève, une classe, un niveau, un type de cours. Soit toutes les réalisations d'un exercice ou d'un type d'exercice/ensemble d'exercice.
Ensuite il choisit les paramêtres/propriété/valeurs qu'il souhaite voir sur cet ensemble de données. 
Ensuite il choisit le format d'affichage.
Le système affiche les données dans le mode d'affichage choisi et le didactitien peut enfin 
analyser les données. 

# Données

Acteur Principal : Didactitien



## Pré-conditions

Avoir des exercices présents dans la base de données et un certain nombres d'exercice réalisés par des 
étudiants pour pouvoir analyser les résultats.
<Pre>
Le use case login.
Le use case choisir son rôle.
Les use case permettant la réalisation d'exercices ;)
</pre>

## Post Conditions

TODO
Cherche à trouver des informations intéressantes à propos des exercices dans la base de données : le taux 
de réussite des exercices, le temps passé dessus, le nombre d'essais avant la réussite de l'exercice.

TODO
En cas de succès : Donne des statistiques utiles au didactitien par rapport à l'analyse des données sur les 
exercices

En cas d'échec : Affiche une erreur lors de l'analyse des traces


# Navigation / IHM 

TODO
Demande d'analyse des données par le didactitien depuis son tableau de bord.
Accès à la base de données, recherche des informations en lien avec ce que le didactitien a demandé, analyse ces données.


## Scénarios

TODO
<PRE> FIXME
MAIN SUCCESS SCENARIO
S	[Analyse des informations demandées par le didactiten, affichage des données trouvées]
1	[Commence lorsque le didactitien souhaite accéder à ses statistiques]
2	[Accès à la base de données, analyse les données demandé par le didactitien suivant les paramêtres qu'il a choisit]
3	[Plusieurs statistiques disponibles issus de l'analyse de ces données]
</PRE>


<!--- 
Author : Raphael
Validator : 
-->


