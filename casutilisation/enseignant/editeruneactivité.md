# Publier/Charger/editer activité

Objectif : Permettre à une enseignant de prendre le code actuelle d'un ou plusieurs exercice et de le/les mettre dans une activité.

Résumé général : L'enseignant sélectionne une activité à modifier. Il clique sur le bouton "+", pour ajouter un exercice à une activité. Il doit rechercher un ou plusieurs exercices, ou voir les exercices de son panier. Puis il sélectionne un ou plusieurs exercice. Il clique sur "Charger" pour finir.

# Données

Acteurs Principal : Enseignant

Acteurs secondaire : Admin

Concurence : Non

Déclencheur : Se déclenche lorsqu'un enseignant veut ajouter un nouvel exercice à une activité, quand l'enseignant clique sur le bouton "Recharger"

## Pré-conditions

Etre connecté sur PL

Avoir un compte enseignant

Etre responsable de l'activité qu'il souhaite modifié

### Données d'entrées

    L'activité à mettre à jour
    
    Le panier de l'enseignant
    
## Post conditions

### Données de sortie

    L'activité avec le/les nouveaux exercices

En cas de succès : Les nouveaux exercices sont ajouter à l'activité.

En cas d'échec : L'activité reste dans son état actuel c'est à dire avant toute modification.

# Navigation / IHM

L'enseignant clique sur le plus, puis il recherche les exercices qu'il veut ajouter ou les sélectionnes depuis son panier. Il clique sur "Charger" pour ajouter les exercices à l'activité.

## Scénarios

MAIN SUCCESS SCENARIO

S   [L'enseignant ajoute des exercices à son activité]

1   [L'enseignant sélectionne un ou plusieurs exercices depuis la recherche ou son panier pour les ajouter à l'activité]

2   [L'enseignant clique sur le bouton "Charger", les exercices sont donc ajoutés à l'activité]

<!---
Author : Jordan, Hugo, Raphael
Validator :
-->

