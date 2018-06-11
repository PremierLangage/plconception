# Recharger activité

Objectif : Permettre à un utilisateur de mettre à jour un ou plusieurs exercices d'une activité.

Résumé général : L'enseignant sélectionne une activité, puis il peut appuyer sur le bouton "Mettre à jour". Ce bouton le conduit vers une page qui lui affiche tous les exercices de l'activité. Il peut voir la version actuelle des exercices ainsi que la dernière version disponible de l'exercice. A coté de chaque exercice n'ayant pas la version la plus récente, il peut cliquer sur un bouton pour voir les détails de la mise à jour.
Il peut aussi cocher directement les exercices qu'il veut mettre à jour. Pour finir, il a juste à cliquer sur le bouton "recharger" en bas de la page. Les exercices seront ainsi charger avec leur dernière version.

# Données

Acteurs Principal : Enseignant

Acteurs secondaire : Admin

Concurence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur le bouton "Mettre à jour" d'une activité.

## Pré-conditions

Etre un utilisateurs connecté à PL

Avoir un compte enseignant

Etre responsable de l'activité qu'il souhaite modifié

### Données d'entrées

    L'activité à mettre à jour
    
    La nouvelle version des exercice de l'activité
    
    La version actuelle des exercices de l'activité
    
## Post conditions

### Données de sortie

    L'activité à jour

En cas de succès : Les exercices de l'activité sont mis à jour.

En cas d'échec : L'activité reste dans son état actuel c'est à dire avant toute modification.

# Navigation / IHM

L'enseignant sur mettre à jour, il voit les exercices de l'activité avec la version actuelle et la dernière version, puis il peut soit cliquer sur un bouton pour voir les détails des modifications soit cocher l'exercice. Puis il clique sur Recharger pour charger les exercices cocher.

## Scénarios

MAIN SUCCESS SCENARIO

S   [L'enseignant à mis à jour l'activité]

1   [L'enseignant sélectionne une activité qu'il veut mettre à jour]

2   [L'enseignant clique sur le bouton "Mettre à jour"]

3   [Il voit la liste des exercices de l'activité, il peut cliquer sur "détails" pour voir le détails des modifications ou il peut cocher l'exercice s'il souhaite qu'il soit mis à jour]

4   [Il clique sur le bouton "Recharger" pour charger les exercices avec leurs dernières versions]

Include Use Cases   [Charger un exercice](chargeractivite.md)

<!---
Author : Jordan, Hugo, Raphael
Validator :
-->

