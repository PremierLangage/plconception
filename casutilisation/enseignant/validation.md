# Valider Tag, exercice, ressource


Objectif :  L'enseignant se doit de valider les tags, les exercices, et les ressources proposé par les utilisateurs non qualifiés (pas de karma dans la discipline).

Résumé général: S'effectue lorsqu'un enseignant dois valider un tag un exercice ou une ressource.

# Données :

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Oui

Déclencheur : Se déclenche lorsqu'un enseignant clique sur le bouton "Validation" TODO changer le nom du bouton peut etre Tâches.

## Pré-conditions :

### Données d'entrées :

	Les disciplines a fort karma de l'enseignant.
	
	Tags, exercices, ressources de la discipline en attente de validation

Avoir un compte enseignant dans la base de donnée.
Avoir un bon Karma dans au moins une discipline.

## Post Conditions :

### Données sortie :

	Tags, exercices, ressources ajoutés à la base de donnée comme étant fiable.

	Ainsi que l'enseignant qui l'as validé.

En cas de succès : L'enseignant voit une liste des tags, exercices, et ressources a valider, dans ses disciplines à fort karma, en cliquant sur le bouton "Validation". Il peut les valider ou les refuser ils seront donc supprimer.

En cas d'échec : L'enseignant n'a rien à valider, soit il n'y a rien en attente de validation, soit l'enseignant n'est qualifié dans aucune discipline.

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

Dès que l'enseignant clique sur "Validation" dans la page d'acceuil.

##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'enseignant voit toute les tags, exercices, ressources en cours de validation, cependant toutes ces choses doivent être dans sa discipline.

1    Ce cas d'utilisation commence quand l'enseignant clique sur le bouton "Validation", ou entre directement l'URL de validation dans un navigateur.

2    On affiche alors tout ce que l'enseignant est capable de valider, en fonction de son karma dans les différentes disciplines. Chaque validation en attente est dans le centre de [notification](/notification.md).

3    Pour chaque tags, exercices, ressources, l'enseignant peut cliquer dessus afin d'obtenir, plus de details (voir l'exercice/la ressource en détail).

4	 Il a le choix entre valider ou refuser un nouveaux tag, exercice ou une nouvelle ressource.

5    Ce cas d'utilisation se fini lorsque l'enseignant change de page internet et arrète les validations.

EXTENSION 

Step    Branching Condition

1	 Si l'enseignant ne peut rien valider. Etape 2

na.  Action causing branching:

1 : L'enseignant ne verra rien en cours de validation.


# RELATED INFORMATION

Concurrency    Plusieurs enseignants peuvent valider en même temps, la liste se met a jour. Deux enseignant ne peuvent pas valider la même chose en même temps, l'un des deux ne pourras le faire.

Include Use Cases    [Notification](/notification.md)
 
<!---
Author : Jordan
Validator : 
-->