# Exercices

## Template `pl.html`

[pl.html](apps/playexo/templates/playexo/pl.html)

* Suppression de l'élément `author`. Création d'un lien *About this exercice* en bas de page qui contiendrait toutes les informations techniques sur l'exercice.
* Simplification des boutons  : on ne garde que le bouton *Valider* avec possibilité de le cacher et de personnaliser son apparence.

## Builder `before` et grader `evaluator`

- Gestion du nombre de tentatives autorisées
- Options de mise en forme du feedback

## Champs de réponse de base

- Input
- Radio
- Checkbox
- MatchList
  - Agrandir la zone de drop.
- SortList
- DragDrop
- TextSelect
  - Quand on sélectionne un mot, le fond coloré fait légèrement bouger le texte. Il faurait ajuster ça.
  - Pour une totale flexibilité, il serait préférable que le composant demande un texte indiquant les unités sélectionnables (avec des accolades par exemple ).
  `"{N'}{ai}-{je} {donc} {tant} {vécu} {que} {pour} {cette} {infamie} ?"`
  Cela permet de choisir les unités sélectionnables comme on veut. Cela permet aussi d'avoir des balises html pour une mise en forme du texte.
  - Pour faciliter la tâche des créateurs d'exercice, il faudrait bien entendu des méthodes dans le composant (ou des fonctions dans bibliothèque) pour, dans certains cas, mettre automatiquement un texte brut sous cette forme (exemples : texte en français avec chaque mot sélectionnable, texte anglais avec chaque mot sélectionnable, etc.)
  - Renommer selections -> selection, word/free -> unit/free
  - Il faudrait un mode `single` (true or false) qui ne permet de sélectionner qu'une seule unité (quand on clique sur une unité, l'unité précédemment sélectionée est déselectionnée ; même principe dans le mode free).

## Feuille d'exercices (`pltp`)

- Nom ?
- Apparence et navigation
- Syntaxe de décoration des exercices

## Composants annexes : timer, hint


## Exercices de mathématiques

- Builder et grader spécifiques
- Composant `MathInput`
- Composant `JSXGraph`
- Utilisation de Matplotlib pour produire des graphiques.
- Bibliothèque `utilsmath`

## Exercices de programmation Python

- Builder et grader spécifiques ? Bibliothèques ?

## Exercices à étapes

- Builder et grader spécifiques ?

## Exercices répétés ou Quiz

- Enjeux : tirage d'exercices différents dans une série, intégration possible dans une activité de type ancrage mémoriel

## Exercices avec des images ou de l'audio

## Composant `GeoGebra`

- Problème bloquant pour l'instant : évaluation de la réponse de l'élève
