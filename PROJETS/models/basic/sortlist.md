# Ordonner des items

Le modèle `model/basic/sortlist.pl` permet de fabriquer des exercices où l'élève doit ordonner des items.

## Clés spécifiques
* `sortedlist` (chaîne multilignes ou liste). Cette clé contient les items que l'élève devra ordonner. Elle peut-être déclarée comme une chaîne multilignes (chaque ligne correspondant à un item) ou une liste. Les items doivent y être entrés dans selon l'ordre que l'élève devra retrouver (l'exercice se chargeant de les mélanger).
* `nbsample` (entier). Si la clé `nbsample` est déclarée, la liste à ordonner par l'élève sera un échantillon aléatoire de `nbsample` items de `sortedlist`. Si la clé `nbsample` n'est pas déclarée, la liste à ordonner par l'élève contiendra tous les items de `sortedlist`.
* `scoring`. Cette clé définit le barème de l'exercice. Deux barèmes sont proposés : "ExactOrder" (défaut) ou "KendallTau".

## Exemple 1

~~~
extends = model/basic/sortlist.pl

text ==
Classer les mots suivants dans l'ordre alphabétique.
==

sortedlist ==
Abricot
Avion
Ballon
Cartable
==
~~~

## Exemple 2

~~~
extends = model/basic/sortlist.pl

text ==
Classer ces premiers ministres de la Ve République du plus ancien au plus récent (selon la date d'entrée en fonction).
==

sortedlist ==
Michel Debré
Georges Pompidou
Maurice Couve de Murville
Jacques Chaban-Delmas
Pierre Messmer
Jacques Chirac
Raymond Barre
Pierre Mauroy
Laurent Fabius
Michel Rocard
Édith Cresson
Pierre Bérégovoy
Édouard Balladur
Alain Juppé
Lionel Jospin
Jean-Pierre Raffarin
Dominique de Villepin
François Fillon
Jean-Marc Ayrault
Manuel Valls
Bernard Cazeneuve
Édouard Philippe
Jean Castex
==

nbsample = 5

scoring = "KendallTau"

demo = https://pl.u-pem.fr/filebrowser/demo/25075/
~~~

## Exemple 3 (génération des données par un script)

~~~
extends = model/basic/sortlist.pl

text ==
Classer les nombres suivants du plus petit au plus grand.
==

before ==
import random as rd
sortedlist = sorted(rd.sample(range(1, 100), 5))
==
~~~

## Exemple 4 (lecture des données dans un fichier externe)

/exemple/sortedlistfile.pl 

~~~
extends = /model/basic/sortlist.pl
@ fichierdedonnee.csv [truc.csv]
column=noms # Choix de la columns 

text==
En utilisant Drag and Drop, rangez les valeurs dans l'ordre.
==

before==
import csv

with open("truc.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)
    # Lecture de la column dans l'ordre du fichier
    lue = [ row[column] for row in reader]

sortedlist= "\n".join(lue)
import sys
print("Copie terminée", file=sys.stderr)



==
~~~

