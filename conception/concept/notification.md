#  Notification

Une notification est un message qui alerte l'utilisateur.

Chaque notification apparaît dans le [centre de notification](centredenotification.md),avec un message indiquant ce pourquoi on a été notifé.

La création d'une notification ce fait sur deux types de receveurs:
IDENTIFIE - soit le mode mail avec  un (ou plusieurs) utilisateur(s) en particulier , soit une mailling liste comme  une classe, les profs d'une classe, utilisateurs,etc.
GENERAUX - soit n'importe quel utilisateur ayant une certaine propriété, karma>3, reputation >300, cercle=uncercle ou else. Dans ce cas, quand on calcule les notifications d'une personne (pour l'affichage) alors on vérifie ce type de notification, l'idée est que cela doit prévenir quelqu'un qui est sur la plateforme mais pas embêter les non connectés.


On peut définir une cause de notification.
-> les causes doivent fournir un lien vers l'action à faire, les notifications sont des éléments de workflow. C'est pourquoi les types GENERAUX sont définis de façon à trouver quelqu'un qui a l'autorité pour faire l'action sans qu'il soit précisé lequel parmis ceux là.



Exemple :
Pour un étudiant : Ajout d'un nouveau cours, d'une nouvelle feuille d'exercice.
Pour un enseignant : exercices à valider, tags à valider, exercice à tagger, ajout d'un avis sur ses exercices/cours, évènement sur un cours (obtention d'un badge par un élève, proportion d'élève ayant fini la feuille atteinte, etc)

Quand on valide le code de la construction d'une notification le fait qu'il y ait un lien vers l'action.

<!---
Author : Hugo
Validator : Jordan
-->

