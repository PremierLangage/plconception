# Karma

Le karma estun entier qui représente le droit d'un enseignant dans une discipline (Exemple : Prog C, python, java ...).
Chaque enseignant a donc un karma pour chaque discipline. Por le moment c'est 1 ou 0 (oui ou non).
Exemple : Pour la programmation un enseignant a un karma en informatique. Mais pas en mathematiques.

Le karma est privé, il n'est pas visible.
Le karma est attrbuer un Administrateur.
Le karma peut être déterminer par les diplômes de l'utilisateur.

Les droits conféré par le karma sont :
- la posibilité de valider un grain de la discipline.
- tagger un exercice.
- manipler (changer les noeux du graph) le graph savant.
- valider les ressources de la discipline 

# Implementation 

une bonne idée (a valider) c'est d'uiliser un cercle pour implémenter le karma.


<!--
Author : Hugo 
Validator : Jordan
-->

AJETER :

Un inspecteur académique peut décider de donner du karma (entre 0 et 20 points) à un enseignant à n'importe quel moment. L'administrateur se chargera de modifier le karma.


Le karma s'attribut de plusieurs manière, libre à chaque académie de choisir sa méthode. Le karma est par défaut à 0.

Plusieurs enseignants peuvent décider du karma d'un enseignant. (Ensuite attribuer par l'admin)
Exemple: Un groupe d'enseignants décide de donner 15 de karma à un enseignant, l'administrateur se charge donc de mettre 15 points de karma à cet enseignant.

relation (comme linkedin), chacun peut donner du karma.

Un enseignant peut valider un tag ou un exercice proposé par un utilisateur s'il a au minimum 15 points dans la discipline de l'exercice.
Exemple : Un enseignant qui a 15 points de karma en C peut valider les exercices et les tags proposés par des utilisateurs en C.

Le karma n'est pas défintif, il est évolutif. C'est à dire qu'à tout moment son karma peut être modifier avec les méthodes du dessus.

Exemple :

Un inspecteur d'académie décide d'augmenter/diminuer le karma d'un enseignant car il le trouve meilleur/moins bon.

Un enseignant obtient une agrégation de mathématique, son karma va donc augmenter.

<!---






