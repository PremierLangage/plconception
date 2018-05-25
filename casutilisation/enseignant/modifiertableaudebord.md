# Modifier tableau de bord

Objectif : Permettre à un enseignant d'afficher les indicateurs qu'il aura choisi directement dans son tableau de bord et/ou de modifier l'ordre d'affichage des cours.

Résumé général : Lorsque l'enseignant est sur son tableau de bord il peut vouloir voir des informations précises en priorité, il peut alors trier la liste des cours qu'il a par date d'utilisation, date de création, etc ou encore les trier lui même en les deplaçants. Il pourra aussi afficher des indicateurs sur son tableau de bord, dans ce cas la il aura un choix d'indicateur selon les classes, les cours, etc.., qu'il pourra épingler sur son tableau de bord.

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsque l'enseignant est dans son tableau de bord.


## Pré-conditions

### Données d'entrées :

	Tous les indicateurs disponible

	Tous les cours associés à l'enseignant

Avoir un compte enseignant dans la base de données.

## Post Conditions

### Données sortie :

	Indicateur (Classe, Exercice, Étudiant, etc...)

	Ordre des cours

En cas de succès : Les indicateurs choisis s'affichent directement dans le [tableau de bord](/tableaudebord.md), et l'enseignant voit ses cours dans l'ordre dans lequel il les a demandé.

En cas d'échec : L'indicateur ne s'affiche pas et les cours sont trier par ordre d'utilisation par defaut.

# Navigation / IHM 

A partir de son [tableau de bord](/tableaudebord.md), l'enseignant peut afficher des indicateurs directement sur son tableau de bord.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant a un choix de trie à sa disposition, ainsi qu'un choix d'indicateur]

1	[L'enseignant doit cliquer sur le bouton "trier", afin de trier ses cours.]

2	[Un choix se présente alors à lui, trier par ordre alphabétique, par ordre d'utilisation, etc.., ce choix sera conservé dans le profil de l'enseignant.]

3	[Ensuite l'enseignant peut choisir certains indicateurs, qu'il veut placer dans son tableau de bord. Ces choix seront conservés dans le profil de l'enseignant.]

4   Ce cas d'utilisation se finit lorsque l'enseignant change de page internet. A chaque fois que l'enseignant ira sur son tableau de bord, il le retrouvera agencé comme il l'a prédefinit précedemment.


RELATED INFORMATION

Include Use Cases	[Tableau de bord](/tableaudebord.md)



<!--- 
Author : Jordan
Validator : Raphael/Hugo
-->
