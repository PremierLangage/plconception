
# Activité Programmée

La création d’activité se fait avec la syntaxe pl pour exprimer des paires clefs/valeurs.

Clés nécessaires :
```PL
groupe=Id groupe   # Un entier représentant l’identifiant d’un groupe.

strategy=xxx .py  
# String qui représente le nom d’un fichier .py représentant une stratégie. Les stratégies sont tous stockés dans un même dossier. Si aucune stratégie n'est mise, la stratégie par défaut est choisit automatiquement.

# Un ou plusieurs chemin menant à un ou plusieurs fichier .pltp
# liens vers des ressources 
@ anotherpath/bob.pl 
@ path/monpltp.pltp  
@ path/monpltp2.pltp


dashboard.student=@ path/dashboard_student.html  
#Chemin vers la page HTML du dashboard de l' étudiant qui clique.
# Default value : la Note actuelle
dashboard.teacher=@ path/dashboard_teacher.html  
#Chemin vers la page HTML du dashboard d’un enseignant.
# Default value : proportion des eleves ayant commencés 

navigation=@ path/xxx.html  
#Chemin vers une page HTML contenant la navigation. (Barre de navigation)
# Default value 


htmltemplate=@ path/xxx.html  
#Chemin vers la page HTML du template de l’activité en question.

barem=@ path/ducode.py  
# Chemin vers un fichier .py représentant un barème pour l'activité.
```
