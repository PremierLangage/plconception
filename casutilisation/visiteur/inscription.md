# Inscription


Objectif :  Permettre l'inscription d'un visiteur.

Résumé général : S'effectue lorsqu'un visiteur clique sur le bouton "S'inscrire", il lui suffit donc d'entrer les informations demandé.

# Données :

Acteur Principal : Visiteur

Acteurs secondaires : Admin

Fréquence   : 1 fois

Concurrence : Non

Déclencheur : se déclenche lorsqu'un visiteur clique sur le bouton "S'inscrire", ou qu'il entre directement l'URL d'inscription

## Pré-conditions :

### Données d'entrées :
	nom 

	prenom

	genre (Homme ou Femme)

	date de naissance

	login

	mail

	mot de passe

Avoir une connexion internet.

## Post Conditions :

### Données sortie :
	
	ajout dans la base de données si mail vérifié, connexion du nouvel utilisateur.


En cas de succès : Le visiteur a accès à un compte utilisateur. Une session est créée, l'utilisateur est placé sur son Tableaudebord.


En cas d'échec: affiche l'erreur à l'endroit ou la donnée est défectueuse.


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

Le visiteur se voit afficher un formulaire qu'il doit remplir, il doit ensuite valider son adresse mail.


##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    Le visiteur est sur la page d'inscription, il entre ses données et clique sur le bouton inscription.

1    Ce cas d'utilisation commence quand le visiteur clique sur le bouton "S'incrire" présent sur la page visiteur ou quand on entre l'URL d'inscription dans un navigateur.

2    On entre son login, son nom, prénom, sa date de naissance, Homme ou Femme, une adresse mail valide et son mot de passe qu'il faudra confirmer deux fois.

3    On clique sur le bouton "S'inscrire".

4 	 Un mail lui est envoyé.

5	 Il doit valider son adresse mail. (ajout des données dans la base de donnée)

6	 Il se retrouve sur l'application en tant qu' [utilisateur](/tableaudebord.md). 

7	 Désormais il pourra se connecter avec son login ou son adresse mail et son mot de passe.

8    	 Ce cas d'utilisation se finit lorsque le visiteur a accès à son compte utilisateur.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'utilisateur s'est trompé dans ses informations ou qu'il entre de mauvaise information. Etape 2 du scénario principale.

2	 Lorsque le visiteur n'a pas validé son email. Etape 5 du scénario principale.

na.  Action causing branching:

1 : on affiche un message d'erreur à l'endroit ou il s'est trompé

2 : On lui propose de renvoyer le mail ou de modifer son adresse mail.


# RELATED INFORMATION

Include Use Cases    [Tableau de bord](/tableaudebord.md) [Login](/login.md) 


<!--- 
Author : Jordan
Validator : Raphael
-->
 
