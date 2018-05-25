# Oublie de mot de passe


Objectif :  Si un utilisateur perd ses informations de connexion, on donne une solution notamment grace à un mail de reinitialisation de mot de passe, cela permet de réduire le nombre de compte inutilisé et de na pas perdre inutilement des utilisateurs.

Résumé général : Lorsqu'un utilisateur oublie son mot de passe mais qu'il dispose de son login et de son adresse mail. Il clique sur le bouton "Oublie de mot de passe", il entre son login et l'adresse mail associé au compte, un mail lui seras envoyé, grâce au quel l'utilisateur peut réinitialiser son mot de passe, il seras alors modifé dans la base de données et l'utilisateur pourras se connecter avec son nouveau mot de passe.

# Données :

Acteur Principal : Utilisateur

Acteurs secondaires : Admin

Fréquence   : fréquence de la connexion

Concurrence : Non

Déclencheur : se déclenche lorsque l'utilisateur veux se connecter mais qu'il a perdu ces informations de connexion.

## Pré-conditions :

### Données d'entrées :
	login

	mail

Avoir un compte dans la base de donnée, pour cela il dois [s'inscrire](/inscription.md).
L'inscription dois être effectué préalablement.
Connaitre au minimun son login et l'adresse mail associé.

## Post Conditions :

### Donnée sortie :
	
	envoie de mail

	nouveau mot de passe

En cas de succès : L'utilisateur dois rentrer son login ainsi que l'adresse mail associé, un mail de reinitialisation de mot de passe sera envoyé.

En cas d'échec : affichage d'erreur de login ou d'adresse mail, on réactualise la page.

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

L'utilisateur est sur la page de connexion, il clique sur "oublie de mot de passe" une fenêtre s'ouvre ou il dois entrer un login correct et l'adresse mail associé à ce login.
Ceci sera vérifié grace à la base de données, un mail sera envoyé, pour réinitialiser la mot de passe.

## Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'utilisateur est sur la page de connexion, il clique sur "oublie de mot de passe".

1    Ce cas d'utilisation commence quand l'utilisateur clique sur le bouton "oublie de mot de passe" ou quand on entre l'url dans un navigateur.

2    L'utilisateur entre son login et l'adresse mail associé à ce login.

3    L'utilisateur clique sur le bouton "Reinitialiser mon mot de passe".

4	 Un mail est envoyé à l'utilisateur.

5	 il dois à nouveau entrer son login, et confirmer 2 fois son nouveau mot de passe si il souhaite le changer.

4    Ce cas d'utilisation se finit lorsque l'utilisateur a accès à son compte après s'etre connecté.

EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'utilisateur s'est trompée dans ses informations (login ou adresse mail). Etape 2 du scénario principale.

na.  Action causing branching:

1 : On propose à l'utilisateur d'entrer à nouveau ses informations, si il continue de se tromper on affiche la mention [inscription](/inscription.md).


# RELATED INFORMATION

Include Use Cases    [Inscription](/inscription.md)


<!--- 
Author : Jordan
Validator : Raphael 
-->
 
