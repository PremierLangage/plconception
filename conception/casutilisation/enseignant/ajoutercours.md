# Ajouter cours sur un site d'asset

Version 1.0: Ce cas d'utilisation est réalisé par LTI a travers le LMS. 




Le cas d'utilisation ici est uniquement pour créer l'instance du cours pour en suite pouvoir le modifier, l'étendre etc.
Attention la création d'un cours est une activité coté ressource et pas coté asset (voir le cas d'utilisation [createcourse.md](createcourse.md)). 

Objectif : Créer les données lians les utilisateurs (enseignants et apprenants) et les assets. 



Résumé: Quand un enseignant ajoute un lien de cours LTI ( dans son LMS moodle ou autre) à la première connection LTI le cours PL correspondant est créé que se soit une connection élève ou professeur.

Le résultat est de créer un asset de cours vide (cf. [coursvide.md](../../concept/coursvide.md)) qui dans la zone activité pour l'enseignant ne contient qu'un seul bouton qui est "ajouter une ressource de type cours". 


Le bouton permet de se connecter au serveur de ressources, en mode search & compose, avec le cours courrant comme cible. 
