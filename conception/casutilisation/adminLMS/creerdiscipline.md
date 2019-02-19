# Créer une discipline

1. Acteur Principal : Administrateur LMS


1. Objectif : Permettre à un administrateur LMS de créer une discipline.


1. Résumé général : Lorsque l'administrateur LMS clique sur le bouton création de son tableau de bord, il pourra créer une discipline en lui donnant un nom, une description et un utilisateur référent avec un email. Il peut modifier le nom d'une discipline déjà existante. Une discipline ne peut pas avoir le même nom qu'un cours ou une autre discipline déjà existante. Des cours et des notions pourront ensuite être associé à cette discpline.


1.  Acteurs secondaires : Aucun


1.  Concurrence : Non


1. Déclencheur : Se déclenche lorsqu'un administrateur LMS souhaite créer une discipline.


## Pré-conditions

Etre connecté avec le rôle d'administrateur LMS.

## Post Conditions

Succès : La discipline a été créé par l'administrateur LMS.

Echec : la disicpline existe déjà.

# Navigation / IHM 

L'administrateur LMS clique sur le bouton Création sur son tableau de bord, il pourra ensuite créer une nouvelle discipline ou modifier le nom d'une discipline déjà existante.


## Scénario Principal

Dans le menu administrateur choisir le menu item créer une discipline.

Un champs de saisie est présenter qui fait de la compléssion automatique avec la liste existante des disciplines.
Si il a des caractères non alphanetiques ils sont refusés. 

Une fois que la displine est créée dans la liste des displines, un répertoire correspondant est créer dans l'arbre (avec une version réduite du nom de la discipline: pas d'espaces uniquement des lettres appartenant à [a-z] .








