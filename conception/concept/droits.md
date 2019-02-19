
Seul un administrateur Django a la possibilité de donné, modifié ou supprimé des droits(CRUD) de tous les utilisateurs autres que des administrateurs django. Par défaut l'administrateur Django a tous les droits.

La visibilité totale désigne le fait de voir toutes les informations de tous les utilisateurs avec leurs noms. En visibilité anonyme, le nom de l'utilisateur à qui les informations appartiennent n'est pas visible. Autrement dit, on ne sait pas à qui appartient les données qu'on regarde en visibilité anonyme.

Les droits des utilisateurs seront stockés dans une table de la base de données où le login sera la clé étrangère et les autres champs correspondent à tout les droits possibles. La valeur de ces champs sera à 1 quand le droit lui est attribué et à 0 quand ce n'est pas le cas.

FIXME comment sotn définis les droits sur les ressources, des bits, des entiers un fichier ??? une table ??? quelle solution de stockage des droits ???


# Utilisateur

Un utilisateur a besoin d'avoir accès à toutes les informations le concernant. Il doit avoir accès à ses feuilles, ses exercices, ses réponses, son profil.  
L'utilisateur a accès en lecture seul à :
- ses exercices
- ses feuilles
- ses réponses

Il a accès en lecture/écriture à :
- son profil

En visibilité totale, l'utilisateur a accès à toutes ses informations.  
En anonyme il n'a accès à rien.



# Groupe

Les groupes sont une manière générique de segmenter les utilisateurs afin de pouvoir leur attribuer des permissions ou de les désigner par un nom défini. Un utilisateur peut appartenir à autant de groupes que nécessaire. Un groupe peut lui-même contenir un groupe.  
Un utilisateur d’un groupe reçoit automatiquement les permissions attribuées à ce groupe.  
Un groupe a accès en lecture seul à :
- ses feuilles
- ses exercices
- ses cours

En visibilité totale, un groupe aura la possiblité de voir que son groupe.  
En anonyme, un groupe n'a aucun droits.



# Enseignant

Un enseignant a besoin d'avoir accès aux informations concernant les étudiants de ses groupes ainsi qu'à ses cours.  
Un enseignant a accès en lecture seul à :
Il a accès en lecture/écriture aux :
- feuilles, exercices et cours (s'ils sont créateurs)

Il a accès en lecture seule :
- résultats de ses étudiants
- feuilles, exercices et cours

En visibilité totale il aura accès à tout ses groupes ainsi qu'à ses cours.  
En anonyme il aura accès aux autres groupes.



# Didacticien

Le didacticien a besoin d'avoir accès à toutes les données concernant le taux de réussite d'un exercice, le temps passé, etc.  
Un didacticien a accès en lecture seule :
- à toutes les données de la classe auquel il est associé

Il a accès en lecture/écriture :
- aux indicateurs

En visibilité anonyme, le didacticien va donc avoir accès à toutes les données.  
En visibilité totale il n'aura accès à rien.



# Responsable

Un responsable a besoin d'avoir accès à tout les groupes et cours dont il est reponsable.  
Un responsable a accès en lecture seule :
- à tout les exercices, feuilles et cours dont il est responsable

Il a accès en lecture/écriture :
- aux groupes dont il est reponsable

En visibilité totale il aura accès à tout ses groupes et cours.  
En anonyme il n'aura accès à rien.


