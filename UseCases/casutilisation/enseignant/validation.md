# Valider Tag, exercice, ressource


Objectif :  L'enseignant se doit de valider les tags, les exercices, et les ressources proposé par les utilisateurs non qualifiés (pas de karma dans la discipline).

Résumé général : L'enseignant est un utilisateur d'autorité dans sa discipline, il se doit de valider des tags, des exercices ou des ressources, pour se faire, dans son tableau de bord il a un bouton "Validation". Lorsqu'il clique dessus il obtient une liste des "activités" en attente. Il peut directement les valider ou cliquer dessus pour avoir plus d'informations sur l'activité. Une fois validé l'activité sera disponible au public. 

# Données :

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Oui

Déclencheur : Se déclenche lorsqu'un enseignant clique sur le bouton "Validation".

## Pré-conditions :

### Données d'entrées :

	Les disciplines à fort karma de l'enseignant.
	
	Tags, exercices, ressources de la discipline en attente de validation

Avoir un compte enseignant dans la base de données.

Avoir un bon Karma dans au moins une discipline.

## Post Conditions :

### Données sortie :

	Tags, exercices, ressources ajoutés à la base de données comme étant fiable.

	Ainsi que l'enseignant qui l'a validé.

En cas de succès : L'enseignant voit une liste des tags, exercices, et ressources a valider, dans ses disciplines à fort karma, en cliquant sur le bouton "Validation". Il peut les valider ou les refuser ils seront donc supprimer.

En cas d'échec : L'enseignant n'a rien à valider, soit il n'y a rien en attente de validation, soit l'enseignant n'est qualifié dans aucune discipline.

# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

Dès que l'enseignant clique sur "Validation" dans la page d'acceuil.

## Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'enseignant voit tout les tags, exercices, ressources en attente de validation, cependant toutes ces choses doivent être dans sa discipline.

1    Ce cas d'utilisation commence quand l'enseignant clique sur le bouton "Validation", ou entre directement l'URL de validation dans un navigateur.

2    On affiche alors tout ce que l'enseignant est capable de valider, en fonction de son karma dans les différentes disciplines. Chaque validation en attente est dans le centre de [notification](../../concept/centredenotification.md).

3    Pour chaque tags, exercices, ressources, l'enseignant peut cliquer dessus afin d'obtenir plus de details (voir l'exercice/la ressource en détail).

4    Il a le choix entre valider ou refuser un nouveaux tag, exercice ou une nouvelle ressource.

5    Ce cas d'utilisation se finit lorsque l'enseignant change de page internet ou arrête les validations.

EXTENSION 

Step    Branching Condition

1	 Si l'enseignant ne peut rien valider. Etape 2

na.  Action causing branching:

1 : L'enseignant ne verra rien en cours de validation.


# RELATED INFORMATION

Concurrency    Plusieurs enseignants peuvent valider en même temps, la liste se met a jour. Deux enseignants ne peuvent pas valider la même chose en même temps, l'un des deux ne pourra le faire.

Include Use Cases    [Notification](../../concept/centredenotification.md)
 
<!---
Author : Jordan
Validator : Raphael
-->
