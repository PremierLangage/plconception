# Etiquettes à glisser-déposer

Le modèle `model/basic/dragdrop.pl` permet de fabriquer des exercices avec des étiquettes à glisser-déposer.

## Clés spécifiques
* `labelcontents` (chaîne multilignes ou liste). Cette clé contient les valeurs des étiquettes. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à une étiquette) ou une liste.
* `nbdrops` (entier). Nombre de zones de dépôt pour les étiquettes.
* `dropsolutions` (chaîne multilignes ou liste). Cette clé contient les valeurs des solutions attendues dans les zones de dépôt. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à une zone de dépôt) ou une liste.
* `shuffle` (booléen). Si `shuffle` vaut `true`, la liste des étiquettes est mélangée. Sinon, elle est laissée dans l'ordre entré dans `labelcontents`. Par défaut, `shuffle` vaut `false`.
