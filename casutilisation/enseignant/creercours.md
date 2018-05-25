# Créer un cours

Objectif : Permettre à un enseignant de créer un cours.

Résumé général : L'enseignant clique donc sur le bouton pour crée un cours, il peut donc entrer toute les informations nécéssaire à la création d'un cours (graphe de grain, énoncé du cours, niveau d'étude etc...), une fois validé ce cours seras disposnible à l'apprentissage.


# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur l'ajout d'un cours dans son [tableau de bord](/tableaudebord.md).


## Pré-conditions

### Données d'entrées :
	
	Graphe de grain

	Enoncé du cours

Avoir un compte enseignant dans la base de donnée.

## Post Conditions

### Données sortie :

	Cours

En cas de succès : L'enseignant a créé son cours, il est donc désormais visible.

En cas d'échec : Le cours n'est pas créé.

# Navigation / IHM 

A partir de son [tableau de bord](/tableaudebord.md), l'enseignant peut cliquer sur le bouton créer un cours.

## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant clique donc sur le bouton pour crée un cours, il peut donc entrer toute les informations nécéssaire à la création d'un cours (graphe de grain, énoncé du cours etc...)]

1	[L'enseignant a la possibilité d'écrire l'énoncer du cours dans l'[éditeur](/editeur.md), ensuite l'enseignant valide.]

2	[Il a ensuite la posibilité de faire un graphe de grain qui seras associé au cours, pour cela l'enseignant peut rechercher et [éditer un graphe](/editergraphe.md) de grain qui existe déja, ou alors créer son propre graphe de grain.]

3	[L'enseignant valide tout ceci, et le cours se retrouve disponible dans son [tableau de bord](/tableaudebord.md).]

4   Ce cas d'utilisation se fini lorsque l'enseignant a fini de créer son cours, ou lorsqu'il change de page cependant grace à la [sauvegarde continu](/sauvegardecontinu.md), l'enseignant ne perd pas les informations qu'il a déjà entré.


RELATED INFORMATION

Include Use Cases	[Editer un graphe](/editergraphe.md), [Sauvegarde continu](/sauvegardecontinu.md), [Editeur](/editeur.md), [Tableau de bord](/tableaudebord.md)



<!--- 
Author : Jordan
Validator :  
-->
