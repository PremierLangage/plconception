# Editer un graphe

Objectif : Permettre à un enseignant de modifer un graphe de notion, d'objectif et de l'associer à un cours.

Résumé général : L'enseignant choisit le cours qu'il veut, et s'il a les droits, il a un bouton "Graphe" qui lui permet de modifier le graphe associé au cours qu'il a choisi. L'application lui propose de modifer ou de créer son propre [graphe orienté](../../concept/graph.md) de [grain](../../concept/grain.md), il valide et le graphe sera sauvegardé dans la base de données et associé au cours.

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsque l'enseignant clique sur le bouton "Graphe" de l'un de ses cours.


## Pré-conditions

### Données d'entrées :

	Cours

Avoir un compte enseignant dans la base de données.

Avoir au moins un cours.

Avoir les droits nécéssaire à la modification du graphe de cours.

## Post Conditions

### Données sortie :

	Graphe orienté des notions / des objectifs pédagogiques.

En cas de succès : L'enseignant associe à son cours, un graphe orienté de notions ou d'objectifs pédagogiques a atteindre à la fin du cours. Il n'y a qu'un seul graphe par cours.

En cas d'échec : Le cours n'aura pas de graphe associé.

# Navigation / IHM 

L'enseignant clique sur son cours ensuite il clique sur le bouton "Graphe", il voit alors dans la partie gauche de l'écran son cours et dans la partie droite, il peut éditer un graphe.

L'enseignant a le choix entre reprendre un graphe qui existe déjà et le modifié si il est modifiable, ou de construire sont propre graphe de A à Z en recherchant les [grains](../../concept/grain.md) qu'il veut.

L'application fournira alors des exercices validateur, et les ressources associées au grain. 

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant choisit le cours qu'il veut, et s'il a les droits il a un bouton graphe qui lui permet de modifier le graphe associé au cours qu'il a choisi.]

1	[L'enseignant clique sur le bouton "Graphe".]

2	[Une nouvelle page s'ouvre l'enseignant voit le cours à gauche et le graphe associé à droite.]

3	[Il peut donc éditer le graphe, [modifier chaque grain](../createur/editergrain.md), chaque liaisons. Grâce à la [sauvegarde continu](../../concept/zonetampon.md) les modifications sont conservées jusqu'à validation ou abandon.]

4 	[Ensuite l'enseignant valide les modifications, ou les abandonnes.]

5   	Ce cas d'utilisation se finit lorsque l'enseignant change de page internet, valide ou abandonne.


RELATED INFORMATION

Include Use Cases	[Editer grain](../../concept/editergrain.md), [Sauvegarde continu](../../concept/zonetampon.md)


 
<!--- 
Author : Jordan
Validator : Raphael
-->
