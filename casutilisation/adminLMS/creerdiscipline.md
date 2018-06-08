# Créer une discipline

Objectif : Permettre à un administrateur LMS de créer une discipline.

Résumé général : Lorsque l'administrateur LMS clique sur le bouton création de son tableau de bord, il pourra créer une discipline en lui donnant un nom, une description et un utilisateur référent avec un email. Il peut modifier le nom d'une discipline déjà existante. Une discipline ne peut pas avoir le même nom qu'un cours ou une autre discipline déjà existante. Des cours et des notions pourront ensuite être associé à cette discpline.

# Données

Acteur Principal : Administrateur LMS

Acteurs secondaires : Aucun

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un administrateur LMS souhaite créer une discipline.


## Pré-conditions

### Données d'entrées :

    Avoir un le rôle d'administrateur LMS.

## Post Conditions

En cas de succès : La discipline a été créé par l'administrateur LMS.

En cas d'échec : Un message d'erreur est affiché dans le cas où le nom la discpline que l'administrateur LMS a choisit est déjà existant.

# Navigation / IHM 

L'administrateur LMS clique sur le bouton Création sur son tableau de bord, il pourra ensuite créer une nouvelle discipline ou modifier le nom d'une discipline déjà existante.


## Scénarios

MAIN SUCCESS SCENARIO

S	[L'administrateur LMS créé une nouvelle discipline ou modifie le nom d'une discipline déjà existante.]

1	[Il clique sur le bouton Création sur son tableau de bord.]

2	[Il doit entrer un nom valide (c'est-à-dire un nom qui n'est pas déjà utilisé par une autre discipline ou un cours), une description et un utilisateur référent avec un email pour la discipline qu'il veut créer.]

3   [Ce cas d'utilisation se finit lorsque l'administrateur LMS a créer une discpline ou modifié le nom d'une discipline existante.]


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque le nom de la discipline est déjà utilisé. Etape 2

na.  Action causing branching:

1 : Un message d'erreur est affiché à l'administrateur LMS, il peut ensuite de nouveau entré un nom pour la discipline.





<!--- 
Author : Raphael
Validator : TODO
-->
