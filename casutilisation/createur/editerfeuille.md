# Editer une feuille d'exercice


Objectif :  Permet à un enseignant d'éditer une feuille d'exercices présent dans une de ses disciplines.

Résumé général : S'effectue lorsqu'un enseignant veut modifier une feuille.


# Données :

Acteur Principal : Enseignant

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant veut modifier une feuille.



## Pré-conditions :

### Données d'entrées :

	Avoir un compte enseignant dans la base de données.

	TODO Pouvoir faire une recherche de toutes les feuilles existantes dans une de ses disciplines.

	la feuille avant les modifications


## Post Conditions :

### Données sortie :

	feuille modifiée

Editer une feuille revient à modifier l'ordre des exercices dans une feuille, changer les exercices présent dans la feuille ou supprimer des exercices de la feuille.

En cas de succès : On sauvegarde la feuille modifiée dans la base de données.

En cas d'échec : Grâce à la [sauvegarde continue](/editeur.md) l'enseignant ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée.


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

L'enseignant a choisi d'éditer une feuille d'exercice, il recherche la feuille qu'il veut éditer, une fois trouver il arrive sur une page ou il voit la feuille d'exercice dans son état actuel (les exercices, l'ordre des exercices, etc..), il peut la modifier en changeant l'ordre des exercices, en supprimant un exercice, ou encore en ajoutant un exercice.

L'enseignant peut aussi [modifer un exercice](/editerexercice.md).


##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'enseignant modifie la feuille et le valide, la feuille est sauvegarder dans la base de données.

1    Ce cas d'utilisation commence quand l'enseignant recherche la feuille qu'il veut modifié et clique sur le bouton "éditer" ou quand on entre l'url d'édition de la feuille dans un navigateur.

2    On voit dans un éditeur la feuille dans son état actuel sans modification.

3    L'enseignant peut modifier tout ce qu'il veut dans la feuille, même la supprimer. (changer l'ordre des exercices, les exercices contenus dans la feuille)

4    Il valide, ce qu'il a modifié dans la feuille. (sauvegarde dans la base de données)

5    Ce cas d'utilisation se finit lorsque l'enseignant a validé ses modifications.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'enseignant part avant d'avoir validé ses modifications. Etape 4

na.  Action causing branching:

1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire les informations que l'enseignant a commencé à modifier et les affiches, cependant si l'utilisateur veut annuler ses modifications, il lui suffit de cliqué sur le bouton "Annuler les modifications", ce qui a pour conséquence de supprimé la modification dans la base de données.


# RELATED INFORMATION

Concurrency    Quand un enseignant modifie une feuille, les autres enseignants ne peuvent pas modifier la même feuille.

Include Use Cases    [Editeur](/editeur.md)
		     [modifer un exercice](/editerexercice.md)
 

<!--- 
Author : Jordan
Validator : Raphael
-->

