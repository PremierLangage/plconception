
# Donner exercice
Objectif : Permettre à un étudiant de donner un exercice à un autre étudiant

Résumé général : On veut donner la possibilité à des étudiants de se donner un exercice à faire dans le cadre d'un défi entre étudiant par exemple. Un étudiant peut donner un exercice à un ou plusieurs étudiant. Le ou les étudiants qui ont reçu l'exercice ne sont pas obligés de le faire.


# Données

Acteur Principal : Etudiant

Concurrence : Non



## Pré-conditions

L'étudiant doit être connecté([login.md](../utilisateur/login.md)), être inscrit à un cours, une feuille doit avoir été ajouter et avoir [accès à une feuille](./accesfeuilleexercice.md). L'exercice que l'étudiant veut donner doit avoir été [créer](../createur/createexercice.md) au préalable.


## Post Conditions

En cas de succès : L'étudiant donne un exercice à faire à l'étudiant qu'il a choisit.

En cas d'échec : L'étudiant n'a pas réussi à donner un exercice à un autre étudiant, on lui affiche un message d'erreur.



# Navigation / IHM 

L'étudiant lance une recherche pour trouver l'étudiant à qui il veut envoyer l'exercice. Une fois trouver il choisit l'exercice qu'il veut envoyer et lui envoie.



## Scénarios

MAIN SUCCESS SCENARIO

S	[L'étudiant peut donner un exercice à un autre étudiant]

1	[L'étudiant recherche l'étudiant à qui il veut envoyer l'exercice]

2	[L'étudiant choisit l'exercice qu'il veut donner]

3	[L'étudiant donne l'exercice à l'étudiant qu'il vient de rechercher]



EXTENSION SCENARIOS

1	[L'étudiant ne trouve pas l'étudiant qu'il recherche] Etape 1

[na. Condition causing branching:]

1 : soit il a fait une erreur dans sa recherche, soit l'étudiant qu'il cherche n'existe pas dans la base de données 



RELATED INFORMATION

Include Use Cases	[Login](../utilisateur/login.md), 
	                [Accès feuille/exercice](./accesfeuilleexercice.md), 
	                [créer exercice](../createur/createexercice.md)



<!--- 
Author : Raphael
Validator :  
-->
