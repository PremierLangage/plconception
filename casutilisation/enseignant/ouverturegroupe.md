# Ouverture de la création de groupe

Objectif : Permettre à un enseignant de notifier aux étudiants qu'ils doivent effectuer des groupes.

Résumé général : Lorsque l'enseignant clique sur son cours, si il y a au moins une classe associé, il a un bouton "Groupe" qui lui permet de notifier à une classe qu'ils doivent se mettre en groupe de X élèves. Pour se faire une page s'ouvre où l'enseignant choisie la classe qu'il veut, l'application affiche les différents nombres d'élèves possible par groupe, l'enseignant choisi, défini une date limite à la constitution des groupes et valide. Les étudiants seront alors [notifiés dans les groupes](../../concept/centredenotification.md).

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsque l'enseignant clique sur le bouton "Groupe" de l'un de ses cours.


## Pré-conditions

### Données d'entrées :

	Cours, Classe

	Nombres d'étudiants par groupes

	Date limite de la constitution des groupes

Avoir un compte enseignant dans la base de données.

Avoir au moins un cours et une classe associé.

## Post Conditions

### Données sortie :

	Les Etudiants de la classe selectionné recevront une notification de création de groupe.

En cas de succès : Les étudiants seront notifiés et pourront créer leurs groupes.

En cas d'échec : Les notifications ne seront pas envoyées.

# Navigation / IHM 

L'enseignant clique sur son cours ensuite il clique sur le bouton "Groupe", il choisit alors une classe parmi celles qui suivent son cours, le nombre d'élève par groupe selon ceux proposé par l'application et la date limite.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant choisit la classe, le nombre d'élèves par groupe et la date limite, les étudiants de la classe sont alors notifiés et doivent créer leurs groupes.]

1	[L'enseignant doit cliquer sur le bouton "Groupe".]

2	[Une nouvelle page s'ouvre l'enseignant doit choisir la classe.]

3	[Le nombre d'étudiants possible par groupe apparait pour la classe sélectionnée.]

4 	[Ensuite l'enseignant choisie une date limite pour la consitution des groupes. (Les étudiants sans groupe à la date limite se verront attribués un groupe aléatoirement, si tous les groupes créés sont pleins, on en crée un nouveau.)]

5   	Ce cas d'utilisation se finit lorsque l'enseignant valide.


RELATED INFORMATION

Include Use Cases	[Centre de notification](../../concept/centredenotification.md)



<!--- 
Author : Jordan
Validator : Raphael
-->
