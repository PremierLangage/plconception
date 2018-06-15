# Ajouter une activité à un cours


Objectif : Permettre à un enseignant d'ajouter des activités à un cours.

Résumé général : L'enseignant clique sur l'un de ses cours,
                 s'il en a les droits, il peut alors cliquer sur le bouton "activité", c'est alors qu'une page contenant une liste de toutes les activités déjà créée s'ouvre.
                 L'enseignant voit les activités déjà créés, il peut cliquer sur celle qu'il veux et ainsi commence l'[édition](../../concept/editeurdechamps.md) de l'activité sélectionnée.
                 Si l'enseignant veut ajouter une nouvelle activité, il clique sur le bouton "Nouvelle activité", ensuite l'enseignant doit rechercher son activité si celle-ci existe. L'on peut cherche une activité grâce à son type (DM,Feuille,Défi etc..), sa discipline, son niveau et/ou son nom.
                 Cependant si l'activité que l'enseignant recherche n'existe pas, il peut en [crée](../createur/creeractivite.md) une nouvelle.

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur le bouton "Activité" dans son cours s'il en a les droits.


## Pré-conditions

### Données d'entrées :

	Cours

	Droits

	Enseignant

Avoir un compte enseignant dans la base de données.

Avoir les droits nécessaires sur le cours.


## Post Conditions

### Données sortie :

	Activités

	Cours

En cas de succès : L'enseignant associe une activité à son cours, cette activité est rendu visible pour les étudiants, ou les modifications sont sauvegardées.

En cas d'échec : S'il y a un échec dans l'édition d'une activité, les modifications sont sauvegardés mais visible uniquement par l'enseignant grâce à la [zone tampon](../../concept/zonetampon.md)

# Navigation / IHM

A partir de son [tableau de bord](../utilisateur/tableaudebord.md), l'enseignant peut cliquer sur un cours, s'il a les droits il a un bouton "Activité" qui lui permet de gérer les activités du cours.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant clique donc sur le bouton pour créer un cours, il peut donc entrer toutes les informations nécessaires à la création d'un cours (graphe de grain, énoncé du cours etc...)]

1	[L'enseignant clique sur l'un de ses cours]

2	[S'il en a les droits, il peut alors cliquer sur le bouton "activité"]

3	[C'est alors qu'une page contenant une liste de toutes les activités déjà créée s'ouvre. L'enseignant voit les activités déjà créés]

4   [Si l'enseignant veut ajouter une nouvelle activité, il clique sur le bouton "Nouvelle activité"]

5   [Ensuite l'enseignant doit rechercher son ou les activités si celles-ci existent. L'on peut cherche une activité grâce à son type (DM,Feuille,Défi etc..), sa discipline, son niveau et/ou son nom.]

6   Ce cas d'utilisation se finit lorsque l'enseignant a fini d'associer l'activité, ou lorsqu'il change de page, cependant grace à la [sauvegarde continue](../../concept/zonetampon.md), l'enseignant ne perd pas les informations qu'il a déjà entré.


EXTENSION


Step    Branching Condition

1	 Si l'enseignant veut modifier une activité déjà existante. Etape 3

2    Si l'activé que cherche l'enseignant n'existe pas. Etape 5

na.  Action causing branching:

1 : L'enseignant peut cliquer sur l'activité qu'il veux et ainsi commence l'[édition](../../concept/editeurdechamps.md) de l'activité sélectionnée.

2 : Si l'activité que l'enseignant recherche n'existe pas, il est redirigé vers [crée une activité](../createur/creeractivite.md) qui sera ensuite associé au cours.



RELATED INFORMATION

Include Use Cases	[Zone tampon](../../concept/zonetampon.md), [Editeur](../../concept/editeurdechamps.md), [Tableau de bord](../utilisateur/tableaudebord.md), [Crée une activité](../createur/creeractivite.md)



<!---
Author : Jordan
Validator :
-->
