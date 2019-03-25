



# Feuille de Route

Trois parties :

 [T0](./feuillederoute.md#t0) ce qui existe aujourd'hui  
 [T1](./feuillederoute.md#t1) Objectif de la prochaine version (1.0)  
 [T2](./feuillederoute.md#t2) Objectif de la version (2.0)   


# T0 

Dernière modification : 13 mars 2019


## Partage des ressources pédagogiques entre enseignants éditeurs (Module GitLoad)

* Possibilité de brancher autant de dépôts git que possible
  (techniquement ça fonctionne mais pas forcement souhaitable au long terme...)
* Conceptexo : dépôt git officiel du projet pour les ressources
  pédagogiques produites par des enseignants éditeurs (pas des
  développeurs).
* Librairie plus technique de fonctionnalités génériques
  multi-matières (QCM, textes à trou, ...) produite par les
  core-développeurs de PL ou des enseignants éditeurs chevronnés qui
  ont produit des modules fonctionnels génériques.


## Gestion de classes (Module ClasseManagement)

* Écran de listage de toutes les ressources PL accessible à
  l'utilisateur identifié par L.T.I.
* Utilisateur Prof : visualisation synthétique par code couleur de
  l'état d'avancement des participant sur la ressource résumée
  (tableau à double entrées indexé par les utilisateurs L.T.I. de la
  ressources et dont les colonnes indexent les ressources de type
  exercices/activités).


## Éditeur en ligne des ressources pédagogiques (Module Editor)

* Navigation dans l'arborescence (dépôt par dépôt) des ressources pédagogiques
* Arborescence réductible répertoire par répertoire (gain de place, commodité d'affichage)
* Onglets d'édition comme les navigateurs modernes (ouvrir un nouveau
  fichier rajoute un onglet sans toucher les autres onglets)
* Multiples raccourcis d'édition:
    - Liens automatiques d'ouverture des ressources citées/utilisées
      dans d'autres ressources
    - Coloration syntaxique des ressources PL
    - Raccourci clavier (Ctrl+S pour la sauvegarde)
* Onglet de preview pour simuler la mise en oeuvre d'une ressource en
  cours d'édition (onglet qui reste local à l'éditeur)


## Éxerciseur (Module PlayExo)

* Mise en oeuvre des ressources de type exercices
* Parsing des ressources et contrôle de leur validité (notament syntaxique, enrichissable)
* Utilise des builders (préparation logique et pédagogique des ressources avant jeu)
    - before : monkey insertion de code Python pour la génération de l'énoncé
    - générateur d'objets aléatoires divers
    - QCM : choisir une question parmi un ensemble fini
* Utilise des graders (délibération logique et pédagogique des réponses élèves, re-médiation possible pour re-jeu)
    - Python : contrôle du code élève avec des doctest
    - C : compilation et exécution du code élève avec comparaison avec l'attendu (arguments, stdin, expected stdout)
    - nombreux petits graders dédiés à des situations spécifiques
* Tests automatiques (simulation de jeu, de construction d'exercices(builder) et de correction d'exercices(grader) )



## Sécurisation des exécutions (Sandbox Docker)

* PL a vocation à exécuter massivement du code produit par des personnes faillibles.
     - Erreur de code en production d'exercice (les enseignants se trompent aussi...)
     - Erreur dangeureuse des élèves en utilisation normale
     - Erreur dûes à des utilsations de personnes mal intentionnées
* Mise en place d'une sandbox utilisant docker fonctionnelle mais non fluide pour le moment. 
  Lenteurs, trop lourd, manque un jail.
  

## Connecteur LTI 

Le connecteur lti permet de connecter une feuille d'exercice dans un LMS. Une fois que c'est fait les personnes se connectant par le biais du LMS sont créées sur PL, ainsi que le cours.
Il manque un retour de notes.



## Q&A 

Un module de Q&A est installé fait partie des applications django du projet. Cela permet de faire du stack-averflow. En particulier des donner des points de participation.
Il manque la possibilité de faire référence a des exercices et la possibillité de faire référence a des questions dans les exercices.


## Documentation 
De grosses lacunes dans la documentation. La séparation des projets va permettre de mettre la documentation sur la programmation des exercices dans les projets disciplinaires.


## ACTIVITE  

Une seule activité le pltp (feuille de tp contenant une liste d'exercices et proposée avec un menu navigable sur le coté gauche).


## TESTs 

La couverture de test du code existant est pas mal mais il manque des tests fonctionnels. 
test fonctionnels permettant de valider en pré-prod la qualité d'une realease. 



## Déploiement 

Le déploiement n'a pas été une réussite les dernière fois de nombreux oublis dans le procedure, et un manque d'industrialisation dans la création d'un document de déploiement.
Il faut que les prochains déploiements ce fasse avec une prise de note et de décission plus clair. 




## EXERCICES 

La quantité d'exercices pour playexo avance avec le nombre de "programmeurs" d'exercice qui tourne autour de 5 ... 
Le nombre d'utilisateur d'exercices est encore faible ...


## TRACES

- la table Answers, une seule table qui doit permettre de tout faire
La structure de la table à été fournis à différenttes personnes et groupes projets pour proposer à termes des statistiques.




# T1

Dans cette deuxième itération, nous souhatons en mai/juin/juillet pouvoir acjouter les fonctionnalités suivantes sur les différents postes.



## Activity Plugins 

- **le gros morceau**  
    - plugins
    - activités
    - langage d'activités programmables
    - Tableaux de bord


## PARTAGE 
- version des fichiers 

Point le plus important avec les activités. 

Toutes les sauvegardes faites sur l'editeur doivent être enregostrées et qu'il soit possible de remonter dans les versions.

De plus il faut permettre de faire des référence dans un fichier pl a une version spécifique. 
Et que le compilateur soit capable de récupérer la version spécifique, avec un système de warning et la possibilité de choisir de changer la version pour la dernière (par exemple).
IL faut que l'on affiche les diff et que l'on porpose la possibilité de changer de version.



## Editeur 

- edition "à la" framapad des exos. L'idée est de voir qui modifie en même temps le fichier.



## INDICATEURS

- Index sur la table answer: index users, pl, activité 
- API d'accès a des données sur les types pl et users pout accèder rapidement à des statistiques.


## Connecteur LTI 

- Remonté de notes d'activité dans moodle 

## Exercices 

- Frankenswims 
- un cours effectivement fait sur la plateforme 



# T2




## Serveurs ASSETS serveur RESSOURCES 

Pour supporter la monté en charge il faut organiser deux types de serveurs.
Le serveur de ressources qui est partagée par tout le monde. 
Les serveur d'assets qui est un serveur de classes.
L'opération que l'on doit mettre en place est le transfert d'une ressource du serveur de ressource vers le serveur d'assets.
Rappatriment sur le serveur d'assets des fichiers et des donnéees une fois qu'une activité à été choisie sur le serveur de ressource.



## TRACES 

- compatibilité xAPI 
- possibilités anonymisation automatique

