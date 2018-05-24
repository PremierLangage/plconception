# Ouverture de la création de groupe

Objectif : Permettre à un enseignant de notifier au étudiant qu'ils doivent effectuer des groupes.

Résumé général : L'application propose à l'enseignant le nombre d'étudiants possible par groupe l'enseignant valide et ensuite c'est aux étudiants de constituer leurs groupes.

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

En cas de succès : Les étudiants seront notifiés et créeront leurs groupes .

En cas d'échec : Les notifications ne seront pas envoyées.

# Navigation / IHM 

L'enseignant clique sur son cours ensuite il clique sur le bouton "Groupe", il choisi alors une classe parmis celles qui suivent son cours et le nombre d'élève par groupe par ceux proposé par l'appication et la date limite.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant choisi la classe,le nombre d'élève par groupe et la date limite, les étudiants de la classe sont alors notifiés et doivent créer leurs groupes.]

1	[L'enseignant dois cliquer sur le bouton "Groupe".]

2	[Une nouvelle page s'ouvre l'enseignant doit choisir la classe.]

3	[Le nombre d'étudiants possible par groupe apparait pour la classe sélectionnée.]

4 	[Ensuite l'enseignant choisie une date limite pour la consitution des groupes. (Les étudiants sans groupe à la date limite se verront attribués un groupe aléatoirement, si tous les groupes créé sont pleins, on en crée un nouveau.)]

5   Ce cas d'utilisation se fini lorsque l'enseignant change de page internet.


RELATED INFORMATION

Include Use Cases	[Centre de notification](/centredenotification.md)



<!--- 
Author : Jordan
Validator :  
-->
