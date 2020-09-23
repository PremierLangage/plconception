# Réponse textuelle libre

Le modèle `model/basic/input.pl` permet de fabriquer des exercices avec un champ de réponse textuel libre.

## Clés spécifiques
* `solution` (chaîne de caractères). Cette clé contient la ou les solutions.
* `casesensitive` (booléen). Cette clé détermine si l'évaluation de la réponse tien compte de la casse ou pas. Par défaut, cette clé vaut `false`.
* `diffmeasure` ("EditDist", "EditRatio"). Cette clé définit la mesure utilisée pour calculer l'écart entre la réponse entrée par l'élève et la solution.
* `tolerance` (nombre). Cette clé définit l'écart maximal accepté (pour la mesure définit dans `diffmeasure`).
* `data` (chaîne de caractères au format CSV). Cette clé contient des données qui pourront être utilisées dans les clés `text` et `solution`.
* `delimiter`. Cette clé définiti le délimiteur utilisé pour lire les données de la clé `data`. Le délimiteur par défaut est la virgule.
* `skipinitialspace`.

## Exemples

~~~
extends = /model/basic/input.pl

text ==
Qui a écrit *Les Misérables* ?
==

solution ==
Victor Hugo
Hugo
==
~~~

~~~
extends = /model/basic/input.pl

title ==
Exemple 2
==

data ==
symbole,nom
Hydrogène,H
Hélium,He
Carbone,C
Azote,N
Oxygène,O
Fluor,F
Néon,Ne
Sodium,Na
Magnésium,Mg
Aluminium,Al
Silicium,Si
Phosphore,P
Soufre,S
Chlore,Cl
Argon,Ar
Potassium,K
Calcium,Ca
Chrome,Cr
Manganèse,Mn
Fer,Fe
Cobalt,Co
Nickel,Ni
Cuivre,Cu
Zinc,Zn
==

text ==
Quel élément chimique a pour symbole **{{ symbole }}** ?
==

solution ==
{{ nom }}
==

diffmeasure = EditDist

tolerance = 1
~~~
