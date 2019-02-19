# Créer Editer une discipline

1. Acteur Principal : [Administrateur LMS](../../acteurs/adminLMS.md)


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

Un formulaire de saisie est présenté :
- Nom de discipline
- nomcour de la disicpline (identifiant unique uniquement en minuscules) 
- description de la discipline (1500 char max), 
- dictateur bienveillant (nom, email, vérifier),
- 
Pour le nom de la discipline le champs de saisi fait de la compléssion automatique avec la liste existante des disciplines.
Si il a des caractères non alphanetiques ils sont refusés. 
Pour le nom cours si il existe déjà une discipline avec ce  nom la c'est une édition. 
Une fois que la displine est créée dans la liste des displines, un répertoire correspondant est créer dans l'arbre *Yggdrasil* (avec une version réduite du nom de la discipline: pas d'espaces uniquement des lettres appartenant à [a-z] .

La discipline à un nom (clef unique==répertroire dans Yggdrasil), une description, un utilisateur référent (dictateur bienveillant) avec un email et des membres (utilisateurs identifiés).


## Liens
[Yggdrasil](../../concept/yggdrasil.md)






