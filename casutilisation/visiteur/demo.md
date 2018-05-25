# Faire une démonstration


Objectif :  Permettre à un visiteur de faire un test de l'application.

Résumé général: Lorsqu'un visiteur est sur l'application on lui propose de faire une petite démonstrations ou il pourras effectuer quelques exercices dans le but de lui montrer les différentes fonctionnalité de l'application et qu'il puisses les tester.

# Données :

Acteur Principal : Visiteur

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un visiteur clique sur le bouton faire une demo.

## Pré-conditions :

Avoir une connexion internet.

Au moins une feuille d'exercices disponible.

## Post Conditions :

### Données sortie :
	TODO


En cas de succès : Le visiteur fini la [démonstration](/acessfeuilleexercice.md), on lui propose donc de [s'inscrire](/inscription.md) sur l'application.


En cas d'échec : Si le visiteur quitte la démo on reviens sur la page d'acceuil des visteurs.

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.
Le visiteur choisi de faire une demo et se lance dans une feuille d'exercice aléatoire de différente discipline.

## Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    Le visiteur est sur la page d'acceuil et choisie de faire une démo.

1    Ce cas d'utilisation commence quand le visiteur clique sur le bouton "Faire une démo" ou quand on entre l'url de démo dans un navigateur.

2    Il a accès à une feuille d'exercice qu'il peut faire.

3    Une fois la feuille finie il a la possibilité de s'inscrire sur le site.

4    Ce cas d'utilisation se finit lorsque le visiteur s'inscrit sur l'application ou quitte le site.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque le visiteur ne finit pas la feuille et quitte avant. Etape 3 du scénario principale.

na.  Action causing branching:

1 : On reviens à la page d'acceuil des visiteurs.

# RELATED INFORMATION

Include Use Cases    [Inscription](/inscription.md) [Excercice](/acessfeuilleexercice.md)

## Qualités de la feuille d'exercice utilisé dans la démo 

La feuille d'exercice doit parcourrir des exemples tirés de plusieurs disciplines :
 programmation, math, anglais, grammaireCM1, c2i
avec des exemple des type d'exercices différents 
Quelle stratégie ?


<!--- 
Author : Jordan
Validator : Raphael
-->

