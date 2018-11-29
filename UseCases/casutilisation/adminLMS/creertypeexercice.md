# Créer ou rechercher un type d'exercice

Objectif : Permettre à un créateur de rechercher un type d'exercice ou  de créer un type qui peut être associer à un exercice si la recherche n'a rien donné

Résumé général :

Un type d'exercice permet de réprésenter la catégorie d'un exercice.
Il est possible de créer un type seulement s'il n'existe pas.
Chaque type d'exercice est obligatoirement associé à un dockerfile.
Pour créer un nouveau type, il doit se rendre dans son tableau de bord, il rentre dans le menu "type" et il clique sur le bouton ajouter un type.
Il doit ensuite saisir un nom qui n'est pas déjà pris et y associer un dockerfile.
Il lui reste ensuite qu'à cliquer sur valider.
Exemple de type d'exercice : python, C


# Données :

Acteur Principal : AdminLMS

## Pré-conditions :

Etre un adminLMS, avoir un docker à associer au type d'exercice que le créateur veut créer.

### Données d'entrées

### Données de sorties :

* Création d'un nouveau type d'exercice

En cas de succès : Le nouveau type est sauvegardé dans la base de données.

En cas d'échec : aucun changement dans la base de données

# Scénario

## Main success scenario

Step : Action

* S : Le créateur crée le type d'exercice après avoir remplit les champs nécessaire. Le type est ainsi sauvegardé dans la base de données.
* 1 : Le cas d'utilisation commence quand le créateur veut créer un nouveau type d'exercice ou quand il rentre l'URL dans son navigateur.
* 2 : Il remplit le champs "nom".
* 3 : Il sélectionne le dockerfile correspondant.
* 4 : Le cas d'utilisation se termine lorsque le créateur a validé son type d'exercice, et qu'il est valide c'est à dire qu'il n'y a pas d'erreur (nom qui existe déjà, dockerfile absent).

Step : Branching Condition

* 1 : Lorsque le créateur part avant d'avoir validé sa création. Etape 4
* 2 : Lorsque le créateur veut chercher un type d'exercice. Etape 1
* 3 : Lorsque le créateur crée un type d'exercice qui existe déjà ou sans dockerfile. Etape 4

na.  Action causing branching :

* 1 : Le cas d'utilisation est annulé.
* 2 : Le créateur trouve le type qu'il cherche et le cas d'utilisation se termine.
* 3 : Il retourne à l'étape 2 ou 3.

# Related information

<!---
Author : Hugo
Validator :
-->

