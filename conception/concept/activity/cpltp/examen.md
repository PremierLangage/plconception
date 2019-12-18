# Examen

L'idée est de proposer une activité examen. 
Le logiciel ne fournis pas un mode d'accès aux machines spécifique  qui permet de s'assurer qu'il n'y a pas de communication entre les étudiants ni d'accès à l'internet (mode tp noté).

Dans un cadre sécurisé l'activité permet de faie passer une évaluation.

## Conditions de passage de l'épreuve

Les conditions spécifiques :
- ni les scores ni les feedback ne sont fournis 
- dans le cas d'un exercice avec une phase de correction syntaxique de la réponse, les erreurs sont remontées aux élèves.
- la seed utilisé est la même pour tout le monde 
- l'ordre des exercices est aléatoire et ils sont indentifiés par des numéros ou des texts non significatifs : question 1, problème 1, Question A. Mais pour conserver une équité les exercices doivent être fournis par groupes d'exercices de niveau équivalents.

- l'accès a la feuille d'exercices est limité au machine de la salle de tp (option)
- l'accès est limités au étudiants sur place (option).
- l'accès est limité a une sous liste des étudiants inscrits au cours,
- le temps est limité une fois que l'etudiant a commencé il a un temps limité, il est prévenu 5 et 1 minutes avant la fin avec un compteur décroissant. Une fois celui ci à zéro la page se ferme avec un remerciement.

En suite, une fois que tout le monde a passé l'épreuve, le professeur peut acceder à la page de correction.

# La page d'édition 

La page d'édition permet de manipuler le sujet d'examen (tests, choix de la seed pour chaque question, preview) etc. En plus de la page d'édition normale d'un pltp.

# La page de correction 

La page de correction permet d'accèder a une page d'évaluation pour les questions **Ouvertes** ou **semi-ouvertes**.

Cette page d'évaluation d'une question contient l'**enonce** de la question un tableau **reponses** + **evaluation** correspondantes (boutons avec une note 0/1/2/3/4) et une **grille critèriée**  (modifiable directement, ajout) permettant l'évaluation. (remarque dans un mode dynamique il est possible d'imaginer que si l'on ajoute une nouvelle ligne dans la grille critèrié tout les reponses évaluer avant doivent être réévaluées).

# la page de note

Un feuille de tableur avec dans les premières lignes des informations générales (eventuellement graphiques) sur l'état actuel de la notation: moyenne,  médiane, ecart type etc. 

Une table donnant pour chaque question:
- le coefficient (l'idée est chaque question à un coefficient entier positif) et que la note sur vingt est calculé par la machine (si l'on veux une note sur 10 ou autre etc c'est possible).
- le taux de success 
- la difficulté (si l'on a l'information a partir de la base de donnée de pl).

une table avec la note de chaque élève.


La page de note est exportable en CSV/ODC/Excel avec plusieurs options sur les colones et les filtres.




