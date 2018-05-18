# Editer un exercice


Objectif :  Permet à un enseignant d'éditer un exercice présent dans une une de ses disciplines.

Résumé général : S'effectue lorsqu'un enseignant veut modifier un exercice.


# Données :

Acteur Principal : Enseignant

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant veut modifier un exercice.



## Pré-conditions :

### Données d'entrées :

	Avoir un compte enseignant dans la base de données.

	TODO Pouvoir faire une recherche de tous les exercices existants dans une de ses disciplines.

	exercice avant la modification


## Post Conditions :

### Données sortie :

	exercice modifiée

Editer un exercice donne la possibilité de changer son énoncé, sa réponse, le type d'exercice, le tag, son titre, etc.

En cas de succès : On sauvegarde l'exercice modifiée dans la base de données.

En cas d'échec : Grâce à la [sauvegarde continue](/editeur.md) l'enseignant ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée.


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

L'enseignant a choisi d'éditer un exercice, il recherche l'exercice qu'il veut éditer, une fois trouver il arrive  sur une page ou il voit l'exercice dans son état actuel et il peut le modifier grace à l'[éditeur](/editeur.md).


##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'enseignant modifie l'exercice et le valide, l'exercice est sauvegarder dans la base de données.

1    Ce cas d'utilisation commence quand l'enseignant recherche l'exercice qu'il veut modifié et clique sur le bouton "éditer" ou quand on entre l'url d'édition de l'exercice dans un navigateur.

2    On voit dans un éditeur l'exercice dans son état actuel sans modification.

3    L'enseignant peut modifier tout ce qu'il veut dans l'exercice, même le supprimer. (balises, type d'exercice, tag etc...)

4    Il valide ce qu'il a modifié dans l'exercice. (sauvegarde dans la base de données)

5    Ce cas d'utilisation se finit lorsque l'enseignant a validé ses modifications.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'enseignant part avant d'avoir validé ses modifications. Etape 4

na.  Action causing branching:

1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire les informations que l'enseignant a commencé à modifier et les affiches, cependant si l'utilisateur veut annuler ses modifications, il lui suffit de cliqué sur le bouton "Annuler les modifications", ce qui a pour conséquence de supprimé la modification dans la base de données.



# RELATED INFORMATION

Concurrency    Quand un enseignant modifie un exercice, les autres enseignants ne peuvent pas modifier le même exercice.

Include Use Cases    [Editeur](/editeur.md)
 

<!--- 
Author : Jordan
Validator : Raphael
-->

