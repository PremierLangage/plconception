# Création d'un exercice


Objectif : Permet à un créateur trouver (ou créer) l'exercice dont il a besoin.

Résumé général : 
- chercher un exercice qui réponde au besoin de l'acteur  
	cette recherche est multicritère niveaux, discipline, grains, thématique, difficulté et plain text
	Si l'exercice est trouvé fin du cas d'utilisation
Sinon 
Soit on fait une demande la création d'un exercice avec tout les bon TAGS, si la demande existe déjà elle gagne un point de priorité (likée) (on sera prévenu quand un exercice de la catégorie sera crée). 
Soit on essaye d'écrire l'exercice  phase de conception et d'édition du source de l'exercice qui utilise l'éditeur en ligne et la prévisualisation.
- phase de validation qui consiste à proposer l'exercice pour qu'il soit public.
FIXME Lorsque le créateur sauvegarde un exercice, si son karma est suffisant l'exercice est directement validé. Sinon un enseignant avec un karma suffisant devra valider l'exercice.
Dans la page d'edition on trouve en plus de l'éditeur et de la prévisualisation, deux boutons, preview qui permet de tester l'exercice et sauvegarde qui permet de sauvegarder le fichier. La preview permet de vérifier le bon fonctionnement de l'exercice. 



# Données :

Acteur Principal : Créateur

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un créateur veut créer un exercice.



## Pré-conditions :

### Données d'entrées :

	Avoir le rôle de créateur dans la base de données.


## Post Conditions :

### Données sortie :

	Exercice crée

En cas de succès : On sauvegarde l'exercice crée dans la base de données. Ici un succès est déterminé par l'absence d'erreurs de syntaxe dans l'énoncé de l'exercice. Le fichier en cours d'édition sera sauvegardé toutes les X=10 secondes et si il y a une modification ou si il y a un signal de l'éditeur. Dans le cas ou le fichier n'a pas de répertoire de stockage (il est uniquement dans la zone tampon) il faut demander dans quel répertoire le sauvegarder en proposant un navigateur de répertoires et en demandant le nom du fichier. Le créateur peut donner à l'exercice un ou plusieurs tag(pas obligatoire), s'il ne le fait pas l'exercice sera moins bien répertorié lors d'une recherche d'exercice.

En cas d'échec : Grâce à la [sauvegarde continue](/editeur.md) l'enseignant ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée. 


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

La phase de conception commence quand on clique dans l'interface sur le menu créer exercice.
Le système ouvre la page edition avec un fichier untitled.pl 
La preview permet de vérifier le bon fonctionnement de l'exercice. 

##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    Le créateur créer l'exercice et le sauvegarde, l'exercice est en attente de validation(si son karma est insuffisant).

1    Ce cas d'utilisation commence quand le créateur veut créé un exercice et clique sur le menu créer exercice ou quand on entre l'url d'édition de l'exercice dans un navigateur.

2    Le créateur peut prévisualiser l'exercice qu'il est en train de créer.

3    Le créateur peut ajouter un ou plusieurs tags à l'exercice(pas obligatoire).

4    Ce cas d'utilisation se finit lorsque le créateur a sauvegardé son exercice.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque le créateur part avant d'avoir validé ses modifications. Etape 4

na.  Action causing branching:

1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire l'exercice que le créateur a commencé à écrire et les affiches.



# RELATED INFORMATION

Include Use Cases    [Editeur](/editeur.md)
 

<!--- 
Author : Raphael
Validator : 
-->
