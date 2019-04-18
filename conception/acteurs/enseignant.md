# Enseignant

Acteur primaire

Utilisateur primaire

## Fonctionnalités demandées.

Les enseignants utilisent la plateforme pour faire leurs enseignements, ils ont besoin de :

* CRUD (create read update delete) un cours dans une classe
  * les objectifs d'apprentissage visés pour le cours (compétences)
  * une ontologie 
  * affecter des activités (permettant d'apprendre) au cours.
  * affecter des ressources a un cours.
  * définir des modalités de validation de ces objectifs
  * ajouter une feuille d'exercices (pltp) à un cours.
  * ajouter un exercice à une feuille d'exercice.
* Gérer la Classe
  * Inscrire des élèves(Etudiant). (Possibilité de connecter des élèves par LTI a partir d'un LMS).
  * Suivre un groupe d'élèves.
* Animer la classe
  * modifier des dates d'ouverture fermeture d'activité
  * donner du f les étudiants
  * Demander la création de groupe
* Valider un tag, un exercice ou une ressource (change de rôle et devient taggeur)

### Données primaires

login, mot de passe, adresse email

### Données secondaires

Nom, prénom, âge, classe etc...

### Données générées

Cours, feuille d'exercice, exercice

## Cas d'utilisation associées

[Corriger une feuille](../casutilisation/enseignant/corrigerfeuilles.md)

[Créer un cours](../casutilisation/enseignant/creercours.md)

[Créer un atelier](../casutilisation/enseignant/creeratelier.md)

[Editer graphe](../casutilisation/enseignant/editergraphe.md)

[Donner un exercice](../casutilisation/enseignant/donnerexercices.md)

[Modifier son tableau de bord](../casutilisation/enseignant/modifiertableaudebord.md)

[Demander la création de groupe](../casutilisation/enseignant/ouverturegroupe.md)

[Suivre une classe](../casutilisation/enseignant/suivreclasse.md)

[Suivre un élève](../casutilisation/enseignant/suivreeleve.md)

[Valider un tag, un exercice ou une ressource](../casutilisation/enseignant/validation.md)


<!--- 
Author : Hugo 
Validator : Raphael
-->

