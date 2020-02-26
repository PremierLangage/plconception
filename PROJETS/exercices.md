# Exercices

- Problème de fluidité lors des validations/actualisations.

## Template `pl.html`

* Titre avec une police plus petite.
* Feedback sous forme de popover ?
* Regrouper tous les boutons et toutes les infos dans une barre de navigation (sticky ?) sur le côté ou en bas :
  * Bouton `Valider`
  * Score
  * Nombre de tentatives restantes (optionnel)
  * Countdown (optionnel)
  * Bouton `Nouveau tirage`(optionnel)
  * Bouton `Indication`(optionnel)
  * Bouton `Aide` (optionnel)
  * Bouton `Feedback` (pour revoir le feedback si après avoir fermé le popover feedback)
  * Bouton `A propos` (optionnel)

Pour donner une idée, voilà une démo très simple (qui s'adapte aux petits écrans en collapsant les boutons de droite).

[Démo de barre de navigation](https://pl.u-pem.fr/filebrowser/option?name=test_pl&path=Yggdrasil/template/basic2.pl)

## Builder `before` et grader `evaluator`

- Gestion du nombre de tentatives autorisées
- Options de mise en forme du feedback.
- Possibilité de définir un environnement pour les exec de before et evaluator.
- Possibilité de définir des fonctions de sérialisation/désérialisation.

## Champs de réponse de base

- Créer des groupes de composants
- Options génériques de style pour les composants.
- Options inline/alignement plus claires.
- Synchronisation des composants lorsqu'ils sont dans des listes.

[Exemples](https://pl.u-pem.fr/activity/play/256/)

- Input
  - Statut de la chaîne vide dans le mode numérique : acceptée ou pas ?
  - Prefix (et bien aligné verticalement)
- Radio
  - Option AutoSubmit
- Checkbox
  - Barèmes : ajouter un barème "un item coché parmi les bons items"
  - Retour à la ligne sur le mode horizontal.
  - Formule de score personnalisable (pareil pour les composants MatchList et DragDrop)
- MatchList
  - Barèmes
  - Agrandir la zone de drop.
- SortList
  - Barèmes
- DragDrop
  - Option qui force les étiquettes à s'ajuster à la taille de la zone de drop quand on les droppent.
  - Le focus quand on passe la souris sur une zone de drop fait bouger les éléments.
  - Pas de focus lors qu'on passe sur une zone de drop quand on n'a pas d'étiquettes sélectionnée.
  - Une étiquette posée sur une zone de drop peut-être déplacée vers une autre zone mais pas dédoublée.
  - Mode avec étiquette à usage unique.
  - Trouver un mécanisme pour gérer facilement l'ensemble des drags et drops.
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
  - Quand on revieny sur un exercice déjà validé, l'ancienne réponse est encore visible mais pas le feedback.
  - Quand on réussit un exercice, cela ne change pas la couleur de l'exercice dans le menu de navigation.
  - Il faudrait alléger le code couleur du menu de navigation.
  - Tronquer le titre des exercices dans le menu de navigation quand ils sont trop longs.
  - Si on abandonne le bouton nouveau tirage dans l'exercice, il faut pouvoir l'ajouter dans la feuille.
  - Recharchement du bloc exercice seulement.
- Syntaxe de décoration des exercices


## Composants annexes : countdown, hint

- Une place réservée pour le countdown dans le template.

## Exercices de mathématiques

- Environnement pour les exec + fonctions de sérialisation/désérialisation des objets sympy
- Composant `MathInput`
  - Claviers virtuels de base. Comment insérer facilement son propre clavier.
  - Problème de focus: cliquer sur le champ doit suffire, sans besoin de cliquer sur le clavier.
- Composant `JSXGraph`
  - Responsive
- Composant MathMatrix
  - Classe avec constructeur du composant à partir d'une matrice (dans différents formats), valeur de la matrice dans différents formats.
  - Champs MathInput pour les coefficients.
  - Philosophie du resize : on voit une sous-matrice d'une plus grande matrice déjà définie.
  
- Utilisation de Matplotlib pour produire des graphiques. Regarder mpl3d
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
