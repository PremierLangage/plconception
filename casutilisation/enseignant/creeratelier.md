# Créer un atelier

Objectif : Permettre à un enseignant de créer un [atelier](../../concept/atelier.md).

Résumé général : Lorsque l'enseignant est sur son tableau de bord il peut cliquer sur un de ses cours, ce qui lui ouvre une page avec des indications sur le cours ainsi qu'un menu qui possède un bouton "Atelier" qui permet de voir les ateliers deja effectués et d'en créer de nouveau.
Un atelier est exportable, l'enseignant peut reprendre un atelier qu'il a déjà fait pour en créer un nouveau et modifer les dates, le nombre d'élève à corriger etc...
Une fois toutes les informations pour créer un atelier remplis et validées, les étudiants recoivent une notification, et doivent donc effectuer le travail demander, puis corriger le travail des autres et ensuite recevoir une note, il y a 3 phases.

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsque l'enseignant clique sur le bouton "Atelier".


## Pré-conditions

### Données d'entrées :

	Cours

	Classe

	les différentes informations pour faire un atelier (Nom, date des différentes phases, nombre d'élève à corriger etc...)

Avoir un compte enseignant dans la base de données.

Avoir un cours

Avoir au moins une classe qui suit ce cours.

## Post Conditions

### Données sortie :

	Atelier

En cas de succès : Les étudiants sont notifiés et doivent suivrent les phases pré-définies dans l'atelier.

En cas d'échec : L'atelier n'est pas créer, personne est notifié.

# Navigation / IHM 

A partir de son [tableau de bord](../utilisateur/tableaudebord.md), l'enseignant clique sur un de ses cours, puis clique sur le bouton "Atelier", il doit ensuite choisir une classe, et créer son atelier.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant créer son atelier, il y a différente manière de créer un atelier et plusieur paramètre nécéssaire a sa création.]

1	[L'enseignant dois cliquer sur le bouton "Atelier", afin de voir les différents ateliers déjà créé.]

2	[Lors de l'affichage de ces ateliers l'enseignant peut copier coller un atelier, qu'il pourra réutiliser à la création de son nouvel atelier.]

3	[Ensuite l'enseignant doit modifier certaines informations, comme le nom de l'atelier, la date, le nombre d'élève etc.. Un atelier a plusieurs modes de répartition des corrections, il y a le mode aléatoire et le mode manuel, dans lequel l'enseignant décide de qui corrige qui.]

4	Ce cas d'utilisation se finit lorsque l'enseignant valide la création de son atelier, les étudiants sont alors notifiés.


EXTENSION 

Step    Branching Condition

1	 L'enseignant crée de A à Z son atelier. Etape 2

na.  Action causing branching:

1 : Dans ce cas l'atelier aura des paramètres par défaut, que l'enseignant devra modifier si cela ne lui convient pas.

RELATED INFORMATION

Include Use Cases	[Tableau de bord](../utilisateur/tableaudebord.md), [Centre de notification](../../concept/centredenotification.md), [Editeur](../../concept/editeurdechamps.md), [Atelier](../../concept/atelier.md)



<!--- 
Author : Jordan
Validator : Raphael
-->
