# Classification disciplinaire

### WIMS Taxonomie

Arbre de notion disciplinaire.

La racine est une discipline, les noeuds sont des cours et les feuilles sont des notions.

Une discipline comprend plusieurs cours et les cours plusieurs notions.

Par exemple :

Pour la discipline Informatique :

Informatique a pour fils :

                -Programmation
                -C2I
                -etc...

Programmation aura pour fils :

                -Python
                -C
                -Java
                -etc...

Ensuite Python a pour fils :

                -One liner
                -File
                -HTTP
                -Condition
                -etc..

Et ainsi de suite.

Ceci est représenté sous forme d'arbre ce qui est très utile pour la recherche de notion etc...

Lorsqu'on cherche un mot présent dans l'arbre on aura comme résultat tous ses fils.
Dans notre exemple si on cherche Python on aura comme resultat :

                -One liner
                -File
                -HTTP
                -Condition
                -etc..

Dans ce cas la on connait aussi le chemin qui mène de la racine jusqu'au mot recherché par l'utilisateur, ici Informatique -> Programmation -> Python .

<!---
Author : Jordan
Validator :
-->