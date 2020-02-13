# Exercices

## Template `pl.html`

[pl.html](apps/playexo/templates/playexo/pl.html)

* Suppression de l'élément `author`. Création d'un lien *About this exercice* en bas de page qui contiendrait toutes les informations techniques sur l'exercice.
* Simplification des boutons  : on ne garde que le bouton *Valider* avec possibilité de le cacher et de personnaliser son apparence.

## Builder `before` et grader `evaluator`

- Gestion du nombre de tentatives autorisées
- Options de mise en forme du feedback

## Champs de réponse de base

[Exemples](https://pl.u-pem.fr/activity/play/256/)

- Input
- Radio
  - Option AutoSubmit
- Checkbox
  - Barèmes
- MatchList
  - Barèmes
  - Agrandir la zone de drop.
- SortList
  - Barèmes
- DragDrop
- TextSelect
  - Quand on sélectionne un mot, le fond coloré écarte légèrement le texte. Il faurait ajuster ça.
  - Pour une totale flexibilité, il serait préférable que le composant demande un texte indiquant les unités sélectionnables (avec des accolades par exemple ). Ex : `"{N'}{ai}-{je} {donc} {tant} {vécu} {que} {pour} {cette} {infamie} ?"`
  Cela permet de choisir les unités sélectionnables comme on veut. Cela permet aussi d'avoir des balises html pour une mise en forme du texte.
  - Conséquence : suppression de l'option `separator`.
  - Pour faciliter la tâche des créateurs d'exercice, il faudrait bien entendu des méthodes dans le composant (ou des fonctions dans bibliothèque) pour, dans certains cas, mettre automatiquement un texte brut sous cette forme (exemples : texte en français avec chaque mot sélectionnable, texte anglais avec chaque mot sélectionnable, etc.)
  - Il serait très pratique d'avoir une syntaxe et une méthode pour envoyer au composant un texte en indiquant quelles unités sont les bonnes réponses (entre double accolades par exemple). Ex :  `{Arthur} {{a}} {horreur} {de} {la} {marche} {à} {pied}.`
  - Renommer selections -> selection, word/free -> unit/free
  - Il faudrait un mode `single` (true or false) qui ne permet de sélectionner qu'une seule unité (quand on clique sur une unité, l'unité précédemment sélectionée est déselectionnée ; même principe dans le mode free).

## Feuille d'exercices (`pltp`)

- Nom ?
- Apparence et navigation
  - Quand on revien sur un exercice déjà validé, l'ancienne réponse est encore visible mais pas le feedback.
  - Quand on réussit un exercice, cela ne change pas la couleur de l'exercice dans le menu de navigation.
  - Il faudrait alléger le code couleur du menu de navigation.
  - Si on abandonne le bouton nouveau tirage dans l'exercice, il faut pouvoir l'ajouter dans la feuille.
  - Recharchement du bloc exercice seulement.
- Syntaxe de décoration des exercices


## Composants annexes : timer, hint


## Exercices de mathématiques

- Builder et grader spécifiques
- Composant `MathInput`
  - Clavier virtuels de base. Comment insérer facilement son propre clavier.
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

[Exemple avec de l'audio](https://pl.u-pem.fr/filebrowser/option?name=test_pl&path=Yggdrasil/Languages/English/listening_numbers.pl)
- Ca vaudrait le coup de faire un composant Audio pour encapsuler le html, le JS et d'éventuelles méthodes Python.

## Composant `GeoGebra`

- Problème bloquant pour l'instant : évaluation de la réponse de l'élève
