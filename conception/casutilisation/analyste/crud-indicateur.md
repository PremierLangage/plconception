
# CRUD indicateurs 

Objectif : Le cas d'utilisation crud indicateur permet à un didactitien de créer un élément de tableau de bord.


Résumé général : Les indicateurs sont stockés dans la base cf. [Indicateur](../../concept/indicateur.md).

Les indicateurs sont définis par :
- les objets (answer, user, exo , feuilles, activity, etc )
- les champs (success, %age, temps, sondage, nombre d'usage etc)
- les filtres  (classe, groupe,date,cours,type, what ever) 
- le format d'affichage (camembert, hystogramme, potentiomêtre)

Les données sont une sélection des informations contenus dans les answers filtrés et affichées selon un type d'affichage graphique.


# Données

Acteur Principal : Analyste

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un analyste veut créer un indicateur.


## Pré-conditions

Le use case [Authentification](../utilisateur/authentification.md)
Le use case choisir son rôle.
Le use case [d'analyse des données](./analysedestraces.md)


## Post Conditions

En cas de succès : A partir de [l'analyse des données](./analysedestraces.md), l'analyste crée un indicateur en fonction des paramètres qu'il a choisit (objets, champs, format d'affichage). L'indicateur crée est stocké dans la base de données.

En cas d'échec : L'analyste ne peut pas créé d'indicateur, un message d'erreur lui est affiché.


# Navigation / IHM 

Lorsque l'analyste clique sur le bouton créer indicateur, il sera sur une page où il aura accès à un menu pour choisir les différents paramètres de son indicateur en fonction de ce qui est disponible à partir de l'analyse des données qu'il a faite auparavant.


## Scénarios

MAIN SUCCESS SCENARIO
S	[Création d'un indicateur selon les paramètres choisit par l'analyste à partir de l'analyse des données]
1	[Commence lorsque l'analyste souhaite créer un indicateur]
2   [L'analyste choisit les paramètres (objets, champs, filtres, format d'affichage) qu'il veut pour son indicateur en fonction des résultats de l'analyse des données]
3	[L'indicateur est crée et stocké dans la base de données]


# RELATED INFORMATION

Include Use Cases    [Authentification](../utilisateur/authentification.md)
                     [Analyse des données](./analysedestraces.md)


<!--- 
Author : Raphael
Validator : TODO
-->
