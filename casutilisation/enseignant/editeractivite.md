# Editer une activité


Objectif :  Permet à un enseignant d'éditer des activités (Cours, Feuille d'exercice, Exercice, Tag) uniquement dans sa discipline notament grace à son karma.

Résumé général: S'effectue lorsqu'un enseignant veux modifier une feuille d'exercice, un cours, ou un tag.

# Données :

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant veux modifier une activité.

## Pré-conditions :

### Données d'entrées :

	activité avant la modification

Avoir un compte enseignant dans la base de donnée.

## Post Conditions :

### Données sortie :
	activité modifié


En cas de succès : On sauvegarde l'activité modifié dans la base de donnée.

En cas d'échec : Grâce à la [sauvegarde continue](/editeur.md) l'enseignant ne perd pas les modifications qu'il a effectué en "local".

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

L'enseignant a choisie d'éditer une activité, il arrive donc sur une page ou il voit l'activité dans son état actuel cependant il peut la modifer grace à l'[éditeur](/editeur.md).

##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'enseignant modifie l'activiter et la valide ce qui est sauvegarder dans la base de donnée.

1    Ce cas d'utilisation commence quand l'enseignant clique sur le bouton "éditer" ou quand on entre l'url de connexion dans un navigateur.

2    On voit dans un éditeur l'activité dans son état actuel sans modification.

3    L'enseignant peut modifer tout ce qu'il veux dans l'activier, même la supprimer.

4	 Il valide, ce qui modifie l'activité dans notre base de donnée.

5    Ce cas d'utilisation se fini lorsque l'enseignant a validé ces modifications.

EXTENSION 

Step    Branching Condition

1	 Lorsque l'enseignant part avant d'avoir validé ces modifications. Etape 4

na.  Action causing branching:

1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire les informations que l'enseignants a commencé à modifier et les affiche, cependant si l'utilisateur veux annuler ces modifications, il lui suffit de  cliqué sur le bouton "Annuler les modifications", ce qui a pour conséquence de supprimé la modification dans la base de donnée.


# RELATED INFORMATION

Concurrency    Quand un enseignant modifie une activité, les autres enseignant ne peuvent pas modifier la même activité.

Include Use Cases    [Editeur](/editeur.md)
 
<!--- 
Author : Jordan
Validator :  
-->