# Choix multiples (une réponse possible)

Le modèle `model/basic/radio.pl` permet de fabriquer des exercices à choix multiples avec une seule réponse possible.

## Clés spécifiques
* `choices` (chaîne multilignes ou liste). Cette clé contient les choix proposés à l'élève. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à un choix) ou une liste.
* `numsol` (entier). Numéro de la solution parmi les choix. Attention, la numérotation des choix commence à 0 ! Par défaut, `numsol` vaut `0`.
* `shuffle` (booléen). Si `shuffle` vaut `true`, la liste des choix est mélangée. Sinon, elle est laissée dans l'ordre entrée dans `choices`. Par défaut, `shuffle` vaut `true`.

## Exemple 1

~~~
extends = model/basic/radio.pl

text ==
Quel pays a pour capitale Budapest ?
==

choices ==
Hongrie
Estonie
Roumanie
Slovaquie
==
~~~

## Exemple 2

~~~
extends = model/basic/radio.pl

text ==
A quel siècle vivait Louis XI ?
==

choices ==
XIe siècle
XIIe siècle
XIIIe siècle
XIVe siècle
XVe siècle
==

numsol = 4

shuffle = false
~~~

## Exemple 3 (génération des données par un script)

~~~
extends = model/basic/sortlist.pl

text ==
Sélectionner le plus petit nombre de la liste suivante.
==

before ==
import random as rd
choices = sorted(rd.sample(range(50), 4))
==
~~~

## Exemple 4 (lecture des données dans un fichier externe)

~~~
extends = model/basic/radio.pl

@ pays_europe.csv

before ==
import random as rd
import csv

with open('pays_europe.csv', newline='') as file:
    all_rows = list(csv.DictReader(file, delimiter=','))
    
sample_rows = rd.sample(all_rows, 4)

capitale = sample_rows[0]['capitale']
choices = [row['pays'] for row in sample_rows]
==

text ==
Quel pays a pour capitale {{ capitale }} ?
==
~~~
