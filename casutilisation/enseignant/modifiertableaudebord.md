# Modifier tableau de bord

Objectif : Permettre à un enseignant d'afficher les indicateurs qu'il aura choisi directement dans son tableau de bord et/ou de modifier l'odre d'affichage des cours.

Résumé général : Un enseignant peut afficher les résumés d'information qu'il veux dans son [tableau de bord](/tableaudebord.md) et il peux vouloir modifier l'ordre d'affichage des cours.


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

	Indicateur (Classe, Exercice, Étudiant etc...)

	Ordre des cours

En cas de succès : Les indicateurs choisi s'affichent directement dans le [tableau de bord](/tableaudebord.md), et l'enseignant voit ses cours dans l'ordre dans lequel il les a demandé.

En cas d'échec : L'indicateur ne s'affiche pas et les cours son trier par ordre d'utilisation par defauts.

# Navigation / IHM 

A partir de son [tableau de bord](/tableaudebord.md), l'enseignant peut afficher des indicateurs directement sur son tableau de bord.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant a un choix de trie à sa disposition, ainsi qu'un choix d'indicateur]

1	[L'enseignant dois cliquer sur le bouton "trier", afin de trier ses cours.]

2	[Un choix se présente alors à lui, "trier par ordre alphabétique",par ordre d'utilisation etc.., ce choix seras conservé dans le profil de l'enseignant.]

3	[Ensuite l'enseignant peut choisir certain indicateur, qu'il veux placer dans son tableau de bord. Ces choix seront conservé dans le profil de l'enseignant.]

4   Ce cas d'utilisation se fini lorsque l'enseignant change de page internet, à chaque fois que l'enseignant iras sur son tableau de bord, il le retrouveras agencé comme il l'as prédefini précedemment.


RELATED INFORMATION

Include Use Cases	[Tableau de bord](/tableaudebord.md)



<!--- 
Author : Jordan
Validator :  
-->
