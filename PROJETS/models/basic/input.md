# `input`

Le modèle `input` permet de fabriquer des exercices avec un champ de réponse textuel libre.

[![](inpu1.png)](https://pl.u-pem.fr/filebrowser/demo/33986/)

## Clés spécifiques

* `text` (chaîne de caractères). Enoncé de l'exercice.
* `solution` (chaîne de caractères). Solution de l'exercice.
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

#### Clés de données (optionnelles)
* `data` (string). Données (au format CSV) qui pourront être utilisées dans les clés `text` et `solution`.
* `delimiter`(string). Délimiteur utilisé dans le format CSV des données de `data`. Par défaut, cette clé vaut `","`.
* `skipinitialspace` (boolean). Si cette clé vaut `false`, l'espace initial après chaque délimiteur est ignoré à la lecture des données. Par défaut, cette clé vaut `true`.



## Exemples avec des données

#### Conjugaison

Dans cet exemple, les conjugaisons du verbe être sont définies dans la clé `data`. A chaque exécution de l'exercice, une ligne du tableau de données est tirée aléatoirement.

[Tester l'exercice](https://pl.u-pem.fr/filebrowser/demo/34257/)


~~~
extends = /model/basic/input.pl

title ==
Conjugaison
==

data ==
pronom,conjugaison
je,suis
tu,es
il ou elle,est
nous,sommes
vous,êtes
ils ou elles,sont
==

text ==
Conjuguer le verbe **être** pour le pronom {{ pronom }}.
==

solution ==
{{ conjugaison }}
==
~~~


#### Latin

~~~
extends = /model/basic/input.pl

title ==
Latin
==

data ==
phrase|motlatin
Le **maître** appelle l'esclave de son fils.|dominus
Le maître appelle l'**esclave** de son fils.|servum
Le maître appelle l'esclave de son **fils**.|filii
**Esclave**, donne de la nourriture aux chevaux.|serve
Esclave, donne de la nourriture aux **chevaux**.|equis
Les **fils** des esclaves devenaient eux-mêmes des esclaves.|filii
Les fils des **esclaves** devenaient eux-mêmes des esclaves.|servorum
L'**esclave** donne un livre au fils du maître.|servus
L'esclave donne un **livre** au fils du maître.|librum
L'esclave donne un livre au **fils** du maître.|filio
L'esclave donne un livre au fils du **maître**.|domini
==

delimiter = |

text ==
Traduire en latin, en utilisant le bon cas, le mot en gras dans la phrase suivante :

{{ phrase }}
==

solution ==
{{ motlatin }}
==
~~~

#### Chimie

En général, il est préférable de stocker les données d'un exercice dans un fichier à part et de les importer. Cela rend le fichier source de l'exercice plus lisible et facilite la réutilisation de ces données dans d'autres exercices. L'exemple suivant montre comment importer des données.

On dispose d'un fichier CSV `data/elements_chimiques.csv` contenant les noms et symboles des principaux éléments chiques.

~~~
nom,symbole
Hydrogène,H
Hélium,He
Carbone,C
Azote,N
Oxygène,O
Fluor,F
...
~~~

Pour affecter le contenu de ce fichier à la clé data, il suffit d'utilise l'opérateur `=@` dans le fichier source de l'exercice.

~~~
extends = /model/basic/input.pl

title ==
Chimie
==

data =@ data/elements_chimiques.csv

text ==
Quel élément chimique a pour symbole **{{ symbole }}** ?
==

solution ==
{{ nom }}
==

diffmeasure = EditDist

tolerance = 1
~~~
