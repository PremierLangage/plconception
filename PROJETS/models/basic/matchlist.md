# Apparier des items

Le modèle `model/basic/matchlist.pl` permet de fabriquer des exercices où l'élève doit apparier des items.

## Clés spécifiques
* `pairs` (chaîne multilignes ou liste). Cette clé contient les paires d'items que l'élève devra mettre en relation. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à une paire d'items) ou une liste de listes.
* `nbsample` (entier).
* `scoring`. Cette clé définit le barème de l'exercice.

## Exemple 1

~~~
extends = model/basic/matchlist.pl

text ==
Relier chaque pays à sa capitale.
==

pairs ==
Allemagne;Berlin
Autriche;Vienne
Belgique;Bruxelles
Danemark;Copenhague
Espagne;Madrid
Finlande;Helsinki
France;Paris
Grèce;Athènes
Hongrie;Budapest
Irlande;Dublin
Italie;Rome
Norvège;Oslo
Pays-Bas;Amsterdam
Pologne;Varsovie
Portugal;Lisbonne
Roumanie;Bucarest
Royaume-Uni;Londres
Slovaquie;Bratislava
Suède;Stockholm
Suisse;Berne
==

nbsample = 4
~~~
