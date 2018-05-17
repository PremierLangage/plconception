# Modification/ Affichage profil-reglage

Objectif :  Permettre à un utilisateur d'afficher et/ou de modifier les informations le concernant dans la base de données, ou de réglé ses paramètres application (mode daltonien etc.. TODO).

Résumé général: On affiche son profil et les réglages actuels, et on permet la modification

# Données


Acteur Principal : Utilisateur

Acteurs secondaires : Admin

Fréquence   : fréquence de la connexion

Concurrence : Non

Déclencheur : se déclenche lors d'un clique bouton sur "profil" ou de l'entré de l'URL dans le navigateur.


## Pré-conditions

### Données d'entrées :

    compte utilisateur (login)

Avoir un compte dans la base de donnée, pour cela il dois [s'inscrire](/inscription.md).
L'inscription dois être effectué préalablement et donc avoir rempli les informations d'inscription.


## Post Conditions

### Donnée sortie :

    login

	nom (impossibilité de modification)

	prenom (impossibilité de modification)

	genre (homme/femme) (impossibilité de modification)

	date de naissance

	langue

	mail

	mot de passe (caché, possibilité de la modif)

	mode daltonien

	mode nuit

	notification oui/non

	TODO


En cas de succès : L'utilisateur a accès à la modification de son profil, il peut donc modifié ou juste voir ses informations et réglé ses paramètres application.

En cas d'échec : S'il y a échec cela veut dire que "l'utilisateur" n'as pas de compte, il est donc un visiteur et on le redirige vers la page où il pourra s'inscrire.


# Navigation / IHM 

Principe de navigation du scénario principal, organisation de l'IHM.

L'utilisateur clique sur le bouton profil, ou entre l'url de la page profil, il voit ses informations et ses réglages en modifiant directement l'affichage, sauf pour le mot de passe où il doit entrer le mot de passe actuel et en écrire un nouveau deux fois. il peut aussi modifier ses paramètres en cochant les bonnes cases.

## Scénarios

# MAIN SUCCESS SCENARIO

Step	Action

S	[L'utilisateur voit ses informations et les modifies]

1	[Ce cas d'utilisation commence quand l'utilisateur clique sur le bouton "Profil" ou entre l'url de la page profil]

2	[Il voit dans un premier temps ses informations, puis ses réglages applications.]

3	[Si il veut il peut modifer l'affichage qu'il devra ensuite confirmé pour que la modification soit effective dans la base de données.]

4	[Ce cas d'utilisation se termine quand l'utilisateur change de page internet.]


EXTENSION SCENARIOS

Step	Branching Action

1	L'utilisateur veut modifier ses réglages applications. Etape 3.

2   L'utilisateur n'est pas connecté. Etape 2.

[na.  Condition causing branching:] 

1 : L'utilisateur doit juste cocher les cases qu'il veut et ses paramètres seront instantanément pris en compte.

2 : Si il n'est pas connecté on le redirige vers une page de connexion ou vers une page visiteur, ou il pourra [s'inscrire](/inscription.md).
	


RELATED INFORMATION

Include Use Cases	[Inscription](/inscription.md)


<!--- 
Author : Jordan
Validator : Raphael 
-->


