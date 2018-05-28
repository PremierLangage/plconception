# Editer un grain


Objectif : Permet à un enseignant d'éditer un grain présent dans une de ses disciplines.

Résumé général : S'effectue lorsqu'un enseignant veut modifier un grain. Editer un grain revient à modifier le contenu associé au grain, les exercices, les feuilles ou les cours. Le créateur peut également modifié le nom du grain, sa description et sa discipline associé. Il peut aussi supprimer un grain.


# Données :

Acteur Principal : Créateur

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant veut modifier un grain.



## Pré-conditions :

### Données d'entrées :

	Avoir le rôle de créateur dans la base de données.

	TODO Pouvoir faire une recherche de tous les grains existant dans une de ses disciplines.

	Le grain avant les modifications


## Post Conditions :

### Données sortie :

	grain modifié


En cas de succès : On sauvegarde le grain modifié dans la base de données.

En cas d'échec : Grâce à la [sauvegarde continue](/editeur.md) l'enseignant ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée.


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

Le créateur a choisi d'éditer un grain, il recherche le grain qu'il veut éditer, une fois trouver il arrive sur une page où il voit le grain dans son état actuel (avec la description, la discipline, les exercices et les cours qui lui sont associés). Il peut le modifier en changeant le nom, la description, la discipline associé, en ajoutant ou en supprimant les exercices et/ou les cours qui lui sont associés ou en supprimant totalement le grain.


##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    Le créateur modifie le grain et le valide, le grain est sauvegarder dans la base de données.

1    Ce cas d'utilisation commence quand le créateur recherche le grain qu'il veut modifié et clique sur le bouton "éditer" ou quand on entre l'url d'édition du grain dans un navigateur.

2    On voit dans un éditeur le grain dans son état actuel sans modification.

3    Le créateur peut modifier tout ce qu'il veut dans le grain, même le supprimer. (changer le nom, la description, la discipline, les exercices, les cours associés)

4    Il valide ce qu'il a modifié dans le grain. (sauvegarde dans la base de données)

5    Ce cas d'utilisation se finit lorsque le créateur a validé ses modifications.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque le créateur part avant d'avoir validé ses modifications. Etape 4

na.  Action causing branching:

1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire les informations que le créateur a commencé à modifier et les affiches, cependant si l'utilisateur veut annuler ses modifications, il lui suffit de cliqué sur le bouton "Annuler les modifications", ce qui a pour conséquence de supprimé la modification dans la base de données.


# RELATED INFORMATION

Concurrency    Quand un créateur modifie un grain, les autres créateurs ne peuvent pas modifier le même grain.

Include Use Cases    [Editeur](/editeur.md)
 

<!--- 
Author : Raphael
Validator :
-->

