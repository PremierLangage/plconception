# Login


Objectif :  Permettre la connexion d'un utilisateur.

Résumé général : Lorsqu'un utilisateur veux se connecter il clique sur le bouton "Login", il dois alors entrer ses informations de connection (mail/login ou mots de passe). Une fois qu'il a entré les bonnes informations l'utilisateur se retrouve sur son tableau de bord ou sur la dernière page qu'il a ouverte lors de sa précédente connection.

# Données :

Acteur Principal : Utilisateur

Acteurs secondaires : Admin

Fréquence   : fréquence de la connexion

Concurrence : Non

Déclencheur : se déclenche lors de la connexion de l'utilisateur, ou à la fin d'une inscription

## Pré-conditions :

### Données d'entrées :
	login

	mot de passe

Avoir un compte dans la base de donnée, pour cela il dois [s'inscrire](../visiteur/inscription.md).
L'inscription dois être effectué préalablement.

## Post Conditions :

En cas de succès : L'utilisateur a accès à son compte. Une session est créée, l'utilisateur est placé sur sa page d'accueil.

En cas d'échec: affiche d'erreur mot de passe, actualisation de la page de connexion.

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

L'utilisateur ou le visiteur est sur la page de connexion sois en cliquant sur "Se connecter" dans la page d'acceuil sois en entrant directement l'URL, il entre ses informations et tente de se connecter, si ses informations sont valides il aura alors accès à son compte, dans le cas contraire un message d'erreur apparait.

##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'utilisateur est sur la page de connexion, il entre ses données et clique sur le bouton connexion.

1    Ce cas d'utilisation commence quand l'utilisateur clique sur le bouton "Se connecter" ou quand on entre l'url de connexion dans un navigateur.

2    L'utilisateur entre son login et son mot de passe.

3    L'utilisateur clique sur le bouton "Connexion".

4    Ce cas d'utilisation se fini lorsque l'utilisateur a accès à son compte après avoir cliqué sur "Connexion".

EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'utilisateur s'est trompée dans ses informations. Etape 3 du scénario principale.

3	 Lorsque le visiteur n'a pas de compte. Etape 3 du scénario principale.

na.  Action causing branching:

1 : On propose à l'utilisateur d'entrer à nouveau ses informations et on affiche la mention [mot de passe oublié](/oubliemdp.md).

2 : On propose au visiteur de [s'inscrire](../visiteur/inscription.md).


# RELATED INFORMATION

Concurrency    Si un utilisateur tente de se connecter avec une autre instance on ferme la première.

Include Use Cases    [Inscription](../visiteur/inscription.md)


<!--- 
Author : Jordan
Validator : Raphael 
-->
 
