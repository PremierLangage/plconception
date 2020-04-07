
# Création d'un AAV

acteur : créateur, enseignant
Objectif: Créer un AAV et le placer dans l'ensemble des AAV existant.

Remarques: Nous souhaitons que les AAV soit le plus unique possible et qu'il n'y ai pas plusieurs aav pour la même sémentique.
Pour cela nous allons utiliser de la reconnaissance de texte. Et nous allons utiliser un maximum les etiquettes conceptuelles pour s'assurer que si l'AAV existe déjà nous le trouverons avant d'avoir à en créer un autre.

Résumé: 
Un aav doit être créé dans le contexte d'une formation ou d'un cours. Sinon il faut remplir un formulaire de contexte. 

Le cours/la formation ou le contexte fournissent une liste d'étiquettes et de valeurs:
- discipline=valeur
- thématique=valeur
- type scolaire visé= ceci est une liste de tous les type scolaires compatibles avec l'aav.

L'aav est initialisé avec cette liste d'étiquettes, il est possible d'en ajouter.

Un éditeur de phrase est proposé au créateur. L'éditeur de phrase de texte d'aav. Voir le cas d'utilisation [Editer un texte d'aav](edittextaav.md).

Une fois le texte édité, le créateut doit fournir une description plus longue de l'aav, description qui doit donner la motivation pour l'aav, et eventuellement faire des demandes d'exercice ou d'activités correpondant à l'aav.

En suite soit le créateur abandonne sa création,
soit le créateur valide son aav :
- une notification est faite sur le tableau d'acconce des cercles correspondants aux étiquettes du contexte.
- une notification est faites aux utilisateurs qui sont sur la liste de notification des étiquettes du contexte. 

C'est la fin du cas d'utilisation et l'aav est créer. Il est visible mais avec le statut nouveau/invalide.
Il peut être utilisé pour étiqueter une ressource et participer comme pré-requis ou participant d'un autre aav.


