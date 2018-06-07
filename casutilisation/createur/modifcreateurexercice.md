# Modifier le créateur d'un exercice

Objectif : Permettre à un créateur d'exercice de déléguer son rôle à un autre créateur.

Résumé général : Lors de l'édition de son exercice le créateur voit qu'il en est l'auteur, s'il clique sur le bouton permettant de déléguer son rôle de créateur,
une liste de tout les créateurs possibles s'ouvre avec une barre de recherche, permettant au créateur de chercher précisément le créateur qu'il veux.

Une fois le créateur choisi, l'application lui envoie une notification lui disant qu'on lui demande d'être le propriétaire de l'exercice.

Si il accepte il devient officiellement le créateur de l'exercice, l'ancien créateur en est notifié et il n'a plus accès à l'édition de ce même exercice.

Cependant si le créateur choisit refuse d'être le nouveau propriétaire de l'exercice le créateur actuel sera notifié et pourra donc en choisir un nouveau.

# Données

Acteur Principal : Créateur

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsque le créateur d'un exercice clique sur son nom dans la catégorie auteur de l'exercice en mode édition.


## Pré-conditions

### Données d'entrées :

	Exercice

	Nouveau créateur

Etre le créateur de l'exercice.

Avoir au moins un autre créateur possible.


## Post Conditions

### Données sortie :

	Nouveau créateur relié à l'exercice

En cas de succès : Le nouveau créateur devient propriétaire de l'exercice et l'ancien n'a plus accès au mode édition de l'exercice.

En cas d'échec : Le créateur choisi a refusé d'être propriétaire, dans ce cas la on notifie le créateur qui a fait la requête, il pourra choisir un autre créateur.

# Navigation / IHM

Le créateur clique sur son nom dans la catégorie auteur en mode édition d'un exercice, une liste de créateurs possibles s'affiche, il en choisit un et valide.
Celui ci sera notifié, il pourra accepter ou refuser de devenir propriétaire.

## Scénarios

MAIN SUCCESS SCENARIO

S	[Le créateur clique sur son nom dans la catégorie auteur de l'édition d'exercice, et une liste de créateurs s'ouvre.]

1	[Le créateur choisit à qui il veux déléguer son rôle.]

2	[Le créateur choisi recevra une notification, lui proposant d'accepter ou de refuser d'être le propriétaire de l'exercice. Il peut voir l'exercice en détail s'il le souhaite.]

3	[S'il accepte il devient le seul créateur de l'exercice.]

5   Ce cas d'utilisation se finit lorsque le créateur accepte ou refuse d'être le propriétaire.


EXTENSION

Step    Branching Condition

1	 Si il n'y a qu'une seule feuille à corriger. Etape 2

na.  Action causing branching:

1 : Dans ce cas l'enseignant voit les exercices les un apres les autres.


RELATED INFORMATION

Include Use Cases	[Editer grain](../createur/editergrain.md), [Sauvegarde continu](../../concept/zonetampon.md)



<!---
Author : Jordan
Validator : Raphael
-->
