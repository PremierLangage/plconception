



# Feuille de Route


# T0


## PARTAGE

Actuellement tout les utiisateurs de l'editeur (c-a-d des ensegiganntas) partagent un répertoire home.
avec le risque que l'on efface ou modifie le travail de quelqu'un d'autre.
Il est possible d'utiliser un git dans ce répertoire partagé pour se proteger en conservant à distance une copie de sauvegarde sur (par exemple) github .
C'est le cas du dossier conceptexo qui est un repository officiel du projet.



## Le module ClasseManagement 

Le module classmanagement permet d'afficher (prof/elève) la liste des cours crés par le module LTI.
Il y a un affichage de l'avancement des activités du cours, sous forme d'un tableau avec des couleurs indiquant le statut de l'exercice (commencé, abandonné, échoué, réussi)

## EDITEUR

* Navigateur dans l'arborescence des ressources réductible répertoire
  par répertoire
* Onglets d'édition comme les navigateurs modernes (ouvrir un nouveau
  fichier rajoute un onglet sans toucher les autres onglets)
* Multiples raccourcis d'édition:
    - Liens automatiques d'ouverture des ressources citées/utilisées
      dans d'autres ressources
    - Coloration syntaxique des ressources PL
    - Raccourci clavier (Ctrl+S pour la sauvegarde)
* Onglet de preview pour simuler la mise en oeuvre d'une ressource en
  cours d'édition (onglet qui reste local à l'éditeur)


## PlayExo (exerciseur)

PlayExo est l'exerciseur proprementy dit, c'est la partie la plus testée du logiciel, et sans doute la plus origniale et aboutie. 
C'est le module qui permet d'éxécuter les exercices définis dans le langage PL (cf. doc)
Le langage de programmation est muni d'un compilateur qui fait de la vérification syntaxique (il est possible d'augmenter les contrôles pour un type d'exo spécifique).


## Sandbox (sécurisation d'exécution)

Une sandbox utilisant docker fonctionne avec quelque accoups. Lenteur, trop lourd, manque un jail.

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

- API 

## Connecteur LTI 

- Remonté de notes dans moodle 

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

