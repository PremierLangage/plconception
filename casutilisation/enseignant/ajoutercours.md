# Ajouter cours

Objectif : Permettre à un enseignant d'ajouter un cours

Résumé général : L'enseignant clique sur le bouton ajouter un cours, il peut donc entrer toutes les informations nécéssaire à la création d'un cours (Nom, tags associés au cours, professeur responsable, discipline du cours, etc...).


# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur le bouton d'ajout d'un cours dans son [tableau de bord](../utilisateur/tableaudebord.md).


## Pré-conditions

Sur Moodle, le cours et l'activité en lien avec le cours qui sera créer sur PL doivent avoir été crée au préalable.

### Données d'entrées :
	
    Cours et activité créé sur Moodle

    Avoir un login

    Avoir un compte enseignant dans la base de données.

## Post Conditions

### Données sortie :

	Cours

En cas de succès : L'enseignant a ajouté son cours, il est donc désormais visible.

En cas d'échec : Un message d'erreur est affiché si les informations que l'enseignant a entré ne sont pas valides, c'est à dire si  le nom du cours est déjà existant, s'il n'y a pas de professeur responsable, s'il n'y a pas de discipline associé au cours.

# Navigation / IHM 

A partir de son [tableau de bord](../utilisateur/tableaudebord.md), l'enseignant peut cliquer sur le bouton ajouter un cours. Il aura une fenêtre de saisie où il devra entrer différentes informations : le nom du cours, TODO la [discipline](./creerdiscipline.md), les professeurs qui auront le droits d'éditer ce cours, les tags associés au cours.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant ajoute le cours qu'il a créer après validation du formulaire]

1	[L'enseignant clique sur le bouton pour ajouter un cours, il peut ensuite entrer toutes les informations nécessaires à la création d'un cours]

2	[L'enseignant a une fenêtre de saisie dans laquelle il doit entrer le nom du cours, la discipline, le professeur responsable et les professeurs qui pourront éditer le cours]

3	[L'enseignant valide, le cours est stocké dans la base de données et le cours se retrouve disponible dans son [tableau de bord](../utilisateur/tableaudebord.md).]

4   [Ce cas d'utilisation se finit lorsque l'enseignant a finit de créer son cours, ou lorsqu'il change de page, cependant grace à la [sauvegarde continu](../../concept/zonetampon.md), l'enseignant ne perd pas les informations qu'il a déjà entré]


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lors de la validation, un message d'erreur est affiché. Etape 3

na.  Action causing branching:

1 : Si une des informations du formulaire est incorrecte ou manquante (nom du cours déjà existant, pas de professeur responsable, pas de discipline). 




RELATED INFORMATION

Include Use Cases	[Sauvegarde continu](../../concept/zonetampon.md), [Tableau de bord](../utilisateur/tableaudebord.md), [Login](../utilisateur/authentification.md), [Discipline](./creerdiscipline.md)



<!--- 
Author : Raphael
Validator : 
-->
