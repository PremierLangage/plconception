
# Etudier

Objectif : Permettre à l'étudiant d'assimiler des nouvelles notions. Pour cela il doit faire des exercices.

Résumé général : L'etudiant se connect par LTI en passant par le LMS sur lequel il est inscrit. 
L'etudiant est envoyé sur l'activité sur laquelle il était actif la première fois.  
    Si il ne s'était jamais connecté il est placé sur son tableau de bord général ou il vois les cours auquels il est inscrit.
L'etudiant interagit avec l'activité. Quand il a assez étudié il s'arrête. 


# Données

Acteur Principal : Etudiant



## Pré-conditions

L'étudiant doit être connecté
le cours dans lequel il est inscrit doit avoir été créé  sur PL (en effet le cours peut exister sur moodle et pas sur PL).
l'activité qu'il a choisi sur moodle doit avoir été créée sur PL (idem).


## Post Conditions
Toutes les interactions de l'etudiant avec la platforme (success et erreurs) on été enregistrées dans PL. 
les notes de l'élève sont enregistrée et transmise à moodle.
la dernière activité est enregistrée dans le profile de l'élève pour son retour sur PL.

# Navigation / IHM 

L'étudiant peut étudier en cliquant sur le cours qu'il veut étudier sur son tableau de bord, il a ainsi accès à toutes les activités de ce cours. Il peut rechercher des cours et exercices voulus dans la base de données s'ils sont présents.



## Scénarios

MAIN SUCCESS SCENARIO

1) l'etudiant choisi le cours et l'activité avec laquelle il veut étudier (ou il est automatiquement placé dessus, soit par le lien LTI, soit car il est automatiquement remis sur la dernière activité.
2) L'activité par le biais de la stratégie propose un exercice qui est affiché. 
3) l'etudiant propose une réponse. 
4) l'exercice en fonction de la réponse et de son comportement (nombre d'essais autorisés) valide ou fait échoué l'exercice,
ce qui est enregistré en base. 
   si ce n'est pas le dernier exercice de l'activité retour en 2) 
5) Fin de l'activité. Affichage du Bilan de l'activité. Retour au tableau de bord général.


RELATED INFORMATION

Include Use Cases	[Login](../utilisateur/login.md)



<!--- 
Author : Raphael
Validator : Hugo
-->

