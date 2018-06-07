#  Sandbox

Une sandbox est un mécanisme qui permet d'éxecuter du code avec moins de risque pour le serveur. Son rôle dans PL est d'éxecuter le code écrit par les étudiants dans les exercices.
Il existe plusieurs sandbox associé à une priorité (pour éviter les pannes...). La sandbox ayant la priorité la plus petite est prioritaire et sera choisit pour recevoir les données du serveur, c'est à dire :
* Le code que les utilisateurs ont écrit pour résoudre les exercices
* Le docker file
* Le langage (C, python ...)

La sandbox doit renvoyer au serveur qui lui a envoyé les programmes à tester :
* le temps d'éxecution du programme
* la valeur de retour du programme
* les warnings s'il existe

<!---
Author : Hugo
Validator :
-->
