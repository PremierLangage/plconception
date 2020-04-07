# Karma

Le karma est un entier qui représente le droit d'un enseignant dans une discipline (Exemple : Prog C, python, java ...).
Chaque enseignant a donc un karma pour chaque discipline. Pour le moment, il existe 3 niveau de karma (0, 1 ou 2).

Exemple : Pour la programmation un enseignant a un karma en informatique, mais pas en mathématiques ni en lettres modernes.

Le karma est privé, il n'est pas visible.
Le karma est gagné en étant actif sur la plateforme.
Un karma  de base peut être déterminé par les diplômes de l'utilisateur (à la discression de l'administrateur).

Le niveau 0 une discipline permet de:
- réponde a des aav de la disicpline
- créer des exercices dans la discipline.

Les droits conférés par le karma au niveau 1 sont :
- la posibilité de valider un aav de la discipline.
- labeliser un exercice de sa discipline.
- manipler (changer les noeux du graph) de ontologie savante.
- valider les ressources de la discipline 

Si un utilisateur atteint le niveau 2, il peut:
* supprimer des exercices (validé ou non).
* supprimer des tags (validé ou non).
* 

## Gain de  karma pour les créateurs 



Pour chaque type de création (exercice ou feuille ou ...), l'enseignant peut gagner un [badge](../concept/badge.md). Il peut obtenir un badge à partir d'un certain palier.
Par exemple, lorsqu'il a créé 10 exercices, il remporte un badge.
Il en gagne un 2ème lorsqu'il en aura créé 50, puis un 3ème lorsqu'il en aura créé 100.
Il en est de même pour les feuilles, les grains et les ressources ...

Chaque création rapporte de la réputation au créateur.
Il gagne :
* 2 Points par commentaire + un point par pouce
* 10 points pour la création d'un exercice + log a base2 de (un point par utilisation)
* 20 points pour la création d'une feuille + log a base2 de (un point par utilisation)
* 20 points pour la création d'un AAV + un point par pouce
* 1000 points pour la création d'une nouveau type d'exercice (donné par un utilisateur karma niveau 10).


## Niveau et Karma 

Un certain nombre de points de karam permet d'atteindre un "niveau". 

Le niveau permet de réalisé certaines actions. 


+ **karma=0** -> niveau 0 
 * possibilité de proposer une nouvelle ressource
 * possibilité de faire une demande d'aav (attention pas un aav mais une demande).

+ **karma>0**  -> niveau 1
 * possibilité de commenter un aav 

+ **karma> (1*ressource+10*comments+) **

## Réputation 

le karma est basé sur le même principe que la réputation sur stackoverflow.

