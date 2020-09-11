# Choix multiples (plusieurs réponses possibles)

Le modèle `model/basic/checkbox.pl` permet de fabriquer des exercices à choix multiples avec plusieurs réponses possibles.

## Clés spécifiques
* `choices` (chaîne multilignes ou liste). Cette clé contient les choix proposés à l'élève. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à un choix) ou une liste.
* `numsol` (liste d'entiers). Numéros des bonnes réponses parmi les choix. Attention, la numérotation des choix commence à 0 !
* `shuffle` (booléen). Si `shuffle` vaut `true`, la liste des choix est mélangée. Sinon, elle est laissée dans l'ordre entrée dans `choices`. Par défaut, `shuffle` vaut `true`.
