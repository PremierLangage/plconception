\tableofcontents
\section{Glossaire}
<!-- aav.md -->
## Acquis d'apprentissage Visés

Les AAV (Acquis d'apprentissage Visés) sont les objets frontière de notre logiciel, les objets qui permettent de réunir tout les acteurs autour d'un concept commun qui est utile pour tous.

Pour plus d'information sur les AAV se repporter au site : 
https://fa2l.be 

[regardez le fichier taxonomieofAAV.md](taxonomieofAAV.md)

### AAVN 
AAV Numériques, le problème de la définition actuelle des aav par fa2l bien que très adapté a la description d'une formation n'est pas adpatée a la construction d'une structure générale d'information et de savoir faires.



### Editeur d'aav

https://byrdseed.com/differentiator/index.php?l=fr


#### Canevas de construction d'un AAV

1) Spécifier le public
1) Spécifier le moment dans l’apprentissage lorsque les objectifs devront être atteints (à l’issue de …)
1) Décrire le comportement visé par un verbe d’action centré sur l’étudiant et spécifier/délimiter le contenu (l’étudiant est/sera capable de …)
1) Décrire les conditions, les situations, les circonstances, le contexte
1) Indiquer le niveau de performance attendu



Les AAV/LO (learning Outcomes) sont des objectifs de formations pemettant de décrire des ressources.


Un aav est une notion ou un objectif pédagogique. Les liens de prérequis qu'il peut avoir sont définis dans une ontologie.

A un aav est associé au moins une ressource (ou un demande de ressource dans le Q&A),
On appel la "ressource principale" d'un aav une ressource permettant de valider l'aquisition du aav.
On appel "Ontologie Par défaut" ou "Ontologie du domaine" est une ontologie spécifique aux aavs. 
Cf. [ontologie](ontology.md)


### Références 
Une autre approche des aavs est celle utilisée dans les cours : https://docs.moodle.org/3x/fr/Objectifs les objectifs pédagogiques.

#### Cas d'utilisation associé

[Editer un aav](../casutilisation/createur/editeraav.md)

[Editer une ontologie](../casutilisation/createur/crudontology.md)



#### Verbes de Bloom

Banque de verbes associés à la taxonomie de Bloom

1. Mémoriser

 Définir, décrire, identifier, lister, associer, nommer, dire, montrer, identifier, collecter, examiner, citer, copier, mémoriser, reconnaitre, répéter, se rappeler, reproduire, enregistrer, retenir.

2. Comprendre

 Interpréter, résumer, convertir, distinguer, estimer, généraliser, paraphraser, nuancer, prédire, associer, différencier, discuter, étendre, classer, exprimer, indiquer, situer, rapporter, rendre compte, sélectionner, traduire, appréhender, entendre, déchiffrer, lire.

3. Appliquer

 Appliquer, changer, compiler, démontrer, opérer, montrer, utiliser, résoudre, calculer, compléter, illustrer, examiner, modifier, raconter, changer, classer, expérimenter, mettre en scène, employer, illustrer, interpréter, opérer, pratiquer, planifier, faire un croquis, écrire, mettre en pratique, mettre en œuvre, pratiquer, vérifier.

4. Analyser

 Identifier les parties, distinguer, représenter dans un diagramme, tracer, relier, associer, déconstruire, subdiviser, analyser, séparer, ordonner, expliquer, classer, arranger, diviser, sélectionner, inférer, analyser, calculer, catégoriser, comparer, nuancer, différencier, discriminer, examiner, questionner, tester, décomposer, disséquer, étudier, examiner, voir, hiérarchiser.

5. Évaluer

 Critiquer, comparer, nuancer, supporter, conclure, discriminer, synthétiser, expliquer, inférer, déduire, témoigner, décider, tester, mesurer, recommander, convaincre, sélectionner, juger, expliquer, discriminer, supporter, argumenter, défendre, comparer, estimer, évaluer, juger, prédire, sélectionner, apprécier, calculer, soupeser, noter, coter, considérer, appuyer.

6. Créer

 Créer, inventer, interpréter, concevoir, imaginer, improviser, innover, trouver, composer, confectionner, élaborer, fabriquer, mettre au point, modifier, rédiger, produire.

<!-- actions.md -->
## Actions

Les actions sont une formalisation des activités des utilisateurs sur le site PL.

Une action est faite par un utilisateur et une ressource. 
Les actions de base sont:
- CreateReadUpdateDelete pour les ressources 
- validate/Annotate i.e. modification des métadata d'une ressource 

La réalisation (success) d'une action entraine des opération du système:
- Quand un exercice est validé, le propriétaire de l'exercice est notifié, et sa réputation est augmentée, le validateur gagne aussi en réputation. 



### Table des actions 
| Action | Description | URL/URI | Droits | Qui est notifié |
|--------|-------------|---------|--------|-----------------|
|Créer exercice |Créer un nouvel exercice|  /discipline/createexercice | Avoir le rôle de créateur  |[Responsable de formation](acteurs/reponsable)|
|Créer exercice en ajoutant des paramètres de notification|             |         |        |                 |
|        |             |         |        |                 |
<!-- activity.md -->

## Activité

Une activité est une Ressource.
Elle est transformée en asset à la ajout dans une classe.

Une activité peut être utilisé dans plusieurs cours, mais il existe une instance distincte pour chaque cours. 

Une activité contient à minima une Stratégie standard et au moins un fichier pltp.

Une activité exporte des tableaux de bord : studentactivitydashboard, teacheracivitydashboard utilisables dans les tableaux de bords correspondants.

une activité a une navigation 
Une activité a un barème (outil permettant le calcul d'une note).

Activité= P O S F*+ E  I N B  (spécial: sd* td*) 
i=introduction  
S= Strategie   
F= pltp  
N=navigation  
B=Barem (comment est calculé la nte qui remonte à moodle)
E=Evaluator (permet de calculer la validation de l'activité) 

En discution: Défini dans la ressource ou dans l'asset ? Fonction de du cours ? 
P= Prérequis 
O= Objectifs (AAV et ontologie)

CHANGEMENT les deux éléments suivant ne sont plus intégrés dans toutes les activités. 
sd=student dashboard  
td=teacher dashboard  


Références : modules WIMS

### LTI et activités

L'activité est l'unité de partage entre les LMS (moodle and co) et PL, mais l'avtivité doit être associé à un cours visible du MLS et de PL.

FIXME Une activité à une URL qui peut être utilisé dans le connecteur LTI.  Le connecteur LTI définie un identifiant externe qui est utilisé pour identifier l'activité dans PL.


<!-- activitydashboard.md -->

## studentactivitydashboard

Tableau de bord exporté par une activité retourne une div contenant un indicateur (voir les tableaux de bord)
qui peut être intégré dans le tableau de bord d'un etudiant.

## teacheractivity dashboard 

indicateur qui peut être intégré dans le tableau de bord d'un enseignant
<!-- area51.md -->
## Area51

Area51 est la zone qui contient tous les exercices qui ne sont associé à aucune discipline et/ou cours.
Elle contient tous les exercices qui ne sont pas créé à partir d'un cours.

Cette zone existera par défaut les exercices dedans en seront pas visibles sauf pour leur propriétaire.

Ceci peut être vue comme le repertoire personnel de chaqu'un.

En fonction du besoin effectif nous utiliserons l'une ou l'autre approche.

cf [Rerpertoire Personnel](home.md).



<!-- ask.md -->
## Ask 
[voire demande](demande.md) 
<!-- assets.md -->
  

## Assets 

Assets: class elements, specific, assigned to a class related to a resource. Assets are used in a class with students, an asset is linked to a resource (like an instance to its class in OOP). The code of the resource is used in the asset, but no modification of the resource is done in the class (except exceptional debug situations). Assets contain a finite set of information pertaining to the interaction of the asset with the student: (opening hours, access conditions, ..., teacher evaluations, etc). Those pieces of information are common to every asset, and, an HTML editor of these values is needed.

Les assets sont des instanciations des ressources. Une fois la ressource chargée la partie ressource ne peut pas être modifiée sur le serveur d'assets sans être préalablement changée sur le serveur de ressources.
Par contre l'asset contient un esnemble d'informations supplémentaires par rapport à la ressource.

## Les liens entre assets 
Il est possible d'ajouter des liens entre assets qui ont le même rôle (localement) que les liens entre ressources.





<!-- atelier.md -->
##  Atelier

Un atelier permet aux étudiants de se corriger entre eux. (Grâce à une grille d'évaluation)
C'est à dire que chaque étudiant doit corriger les exercices de plusieurs étudiants. La correction se fait de manière anonyme.

L'enseignant peut choisir si l'atelier se fait en groupe ou non. Si l'atelier se fait en groupe, chaque groupe corrige donc d'autres groupes.

Un utilisateur ou un groupe doit être corriger par plusieurs utilisateurs/groupe.
La note finale de l'utilisateur/groupe sera la moyenne des notes données par les différents utilisateurs/groupes.
La moyenne permet d'avoir une note "cohérente" (pas basé sur une seule correction).

Pour éviter que les utilisateurs/groupes donnent des notes aléatoires, il faut que la note que donne chaque élève soit comparé à la note donner par l'application (pl). Ce qui génèrera une note pour la qualité de la correction des étudiants/groupes.


La note maximale du correcteur est la note maximale qu'il peut donner en corrigeant.
Après qu'un étudiant ait corrigé et noté un autre étudiant, on réduit à la note maximale du correcteur la différence entre la note donnée par l'application et la note qu'il a lui même donné à l'étudiant.

Exemple :

Un étudiant Toto doit noter un étudiant Titi sur 20. La note maximale qu'il peut donner est donc 20/20. L'application (pl) donne une note de 18/20 à Titi et Toto donne la note de 10/20 à Titi. Après avoir noté Titi, Toto obtient une note pour la qualité de sa correction. La note maximale que Toto peut attribuer est de 20 et la différence est de 8, Toto obtient donc un 12/20 pour sa correction.


<!---
Author : Hugo
Validator : Jordan
-->
<!-- avisexercice.md -->
## AVIS Exercice

L'avis d'un exercice c'est ce que l'utilisateur a pensé de ce dernier (trop dur, trop facile, ...) après l'avoir terminé.

Les avis sont proposés à chaque exercice. Cependant si l'utilisateur n'a pas fait l'exercice son avis ne seras pas pris en compte.
Les avis doivent être cohérents avec ce qu'a l'utilisateur sinon ils ne seront pas pris en compte par l'application.

Par exemple si un utilisateur dit qu'un exercice est trop facile mais qu'il ne l'a pas réussi ou qu'il a abandonné l'avis en incohérent.

Ils sont représentés par des cases à cocher en plus d'une zone de texte "commentaire" qui permet aux étudiants d'écrire leur pensée sur l'exercice ou bien de justifier leur(s) choix.
L'étudiant peut cocher plusieurs options (choix) s'il le veut. Les cases à cocher sont des options qui peuvent être créer, modifier, supprimer par un administrateur (CRUD).

Un avis est facultatif, il n'est pas obligé de cocher des options et/ou remplir la zone de texte "commmentaire".


Chaque avis est anonyme.

En cas d'échec, il faut essayer de savoir pourquoi l'utilisateur n'a pas réussi à faire l'exercice.

Il faut faire attention car il y a 2 cas d'échec différents :

Soit il a échoué sans avoir essayer (ex. abandon au bout de 10s).

Soit il a échoué en ayant essayer.

Exemple d'options si l'étudiant a échoué :

Trop difficile : s'il pense que l'exo a un niveau trop élevé.

Trop long : s'il pense que l'exo est trop long.

Amusant : exercice fun

Enoncé trop compliquer à comprendre : s'il pense que l'énoncé n'est pas assez explicite.

Exemple en cas de réussite :

NEUTRE: Avis par défaut

Inutile : Si l'exercice est beaucoup trop facile et qu'il pense que ce dernier n'a aucune utilité.

Facile : Si l'exercice est facile

Trop difficile : s'il pense que l'exo a un niveau trop élevé.

Trop long : s'il pense que l'exo est trop long.

Amusant : exercice sympa et fun


<!---
Author : Hugo
Validator : Jordan
-->


<!-- badge.md -->
## Badge

 Un badge est une récompense attribuée à un acteur, attestée par un logo visuel, et ouvrant eventuellement des droits.

### Quelques exemples 

Les badges ont des déclancheurs variés. Par exemple :
1) passé plus de 10 heures sur la plateforme.
2) créer un exercice
3) Corriger un paquet de copies
4) Avoir fait correctement X exercices en 5 minutes.
5) avoir fini sa première feuille d'exercices
6) avoir taggé plus de 10 exercices
7) avoir valider plus de 100 exercices
8) avoir du Karma dans plus de 5 discplines
9) avoir réussit 35 exercice de suite 
10) avoir regarder 10 vidéos
11) avoir écrit une stratégie
12) avoir écrit sur un forum.
...


On stocke dans la base de données toutes les données permettant de détecter l'obtention d'un badge  
comme par exemple le nombre d'exercice crée, le temps passé sur les exercices etc...

L'admin LMS crée les badges.


<!---
Author : Hugo
Validator : Jordan
-->
<!-- balise.md -->
## Balises

Champs d'un exercice une feuille ou un cours.

Un autre terme est la clef (key), ce qui est naturel comme les ressources sont des dictionnaires python. 


Les exercices pl sont des dictionnaires, chaque couple clef valeur est appelé une balise. 
Par exemple :
<pre>
  text==
  coucou c'est l'énoncé
  ==
</pre>

Est une balise texte contenant "coucou c'est l'énoncé\\n"

<pre>
Berk="kiki"
</pre>
est une balise Berk contenant '"kiki"'

Une balise ne peut être None.  

Il existe de nombreux types de balises (title, from,extends etc..).

<!-- barredexercice.md -->
## Barre d'exercice

La barre d'exercice est un affichage HTML d'un exercice sur une seul ligne. 

C'est une barre contenant la discipline de l'exercice, son niveau, son nom, un metadata (validité, liste des cercle où il est).

La bare contient des boutons qui permettent différentes actions:  
-preview lance une nouvelle fenetre de preview de l'exercice   
-extends lance une fenetre d'edition d'un exercice ititialisé avec la ligne extends= référence de l'exercice de la bare d'exercice  
-fork lance une fenetre d'edition de l'exercice lui même avec la sauvegarde qui fabriquera un pull request.

Il est aussi possible de cliquer sur un bouton affichant la discussion sur l'exercice en question et un autre pour afficher un indicateur (à choisir). 

Les badges de l'exercice sont visibles: Labbel Rouge, académie de Versailles, LDAR++, comprehénsible, sans Fôtes.
<!-- barrefeuille.md -->

## BARREFEUILLE

TODO
un affichage intelligent d'un lien de feuille de TP.
avec plein de goodies
<!-- centredenotification.md -->
## Centre de notification

Le centre de notification regroupe l'ensemble des notifications d'un utilisateur (Validation, Défi, Groupe etc..).

Il est accessible à n'importe quel moment dans le menu, il se trouve dans l'en-tête de premier language.

L'utilisateur peut désactiver les notifications qu'il veut dans le [profil](profil.md), ce qui annule toutes alertes.


<!---
Author : Hugo
Validator : Jordan
-->
<!-- cercle.md -->
## Les cercles

Les cercles sont des ensembles d'utilisateurs.
Les cercles ont un propriétaire et des administrateurs capables d'accepter et virer des utilisateurs.  
Les cercles ont des labels propres qui permettent d'étiqueter les exercices.  
Les cercles sont propriétaires de ressources (en lieu et place de personnes).

Le cercle savant d'une discipline est propriétaire du graphe savant de la discipline.

Le cercle par défaut de tous les créateurs est le cercle créateur. On y est inscrit par défaut.
(on peut se faire virer ....).


Les cercles ont un forum associé.
Les cercles ont un framavox (ou l'équivalent) associé: ce qui permet de prendre des décisions, de faire des sondages etc.


<!---
Author :
Validator : Jordan
-->
<!-- chatbot.md -->
## Chat bot

Robot de discussion.
L'idée est  que les élèves connectés à une activité peuvent partager un tchat.
L'enseignant peut aussi y participer, ainsi il a accès à ce que font les étudiants.
En plus il peut envoyer des messages privés et envoyer des documents aux élèves.


<!---
Author :
Validator : Jordan
-->
<!-- classe.md -->
##  Classe

Une classe a un nom.

Une classe est un ensemble d'étudiant.

Un ou plusieurs [cours](cours.md) peuvent être affecté à une classe par l'acteur [AdminLMS](../acteurs/adminLMS.md).

Une classe a un niveau: CM2, 6ème, Terminal, L2, M1

### Cas d'utilisation associé

[Suivre une classe](../casutilisation/enseignant/suivreclasse.md)  
[adminsitration LMS](../casutilisation/adminLMS/administrationlms.md)


<!---
Author : Hugo
Validator : Jordan
-->
<!-- classeouverte.md -->

## Classe ouverte 
Une classe ouverte est une [classe](./classe.md) accessible à tous.


<!-- classificationdisciplinaire.md -->
## Classification disciplinaire

#### WIMS Taxonomie

Arbre de notion disciplinaire.

La racine est une discipline, les noeuds sont des notions.

Une discipline comprend plusieurs cours et les cours plusieurs notions.

Par exemple :

Pour la discipline Informatique :

Informatique a pour fils :

                -Programmation
                -C2I
                -etc...

Programmation aura pour fils :

                -Python
                -C
                -Java
                -etc...

Ensuite Python a pour fils :

                -One liner
                -File
                -HTTP
                -Condition
                -etc..

Et ainsi de suite.

Ceci est représenté sous forme d'arbre ce qui est très utile pour la recherche de notion etc...

Lorsqu'on cherche un mot présent dans l'arbre on aura comme résultat tous ses fils.
Dans notre exemple si on cherche Python on aura comme resultat :

                -One liner
                -File
                -HTTP
                -Condition
                -etc..

Dans ce cas la on connait aussi le chemin qui mène de la racine jusqu'au mot recherché par l'utilisateur, ici Informatique -> Programmation -> Python .

<!---
Author : Jordan
Validator :
-->
<!-- classroom.md -->
## Classroom

Représente le concept contenant des élèves, sur le serveur d'asset.
<!-- complession.md -->

## Complession 

TODO

L'idée est de définir une modalité de complession pour une ressource.

La forme de complession la plus forte est la validation.

[Validation](validation.md)
<!-- completion.md -->

## complétion 


L'idée est de définir une modalité de complétion pour une ressource.

C'est une mesure de ce que l'apprenant à atteint comme niveau compétence par rapport à la ressource. 

La forme de complétion la plus forte est la validation.

[Validation](validation.md)

c'est à mettre en relation avec l'état d'un exercice.

[State](state.md)

<!-- cours.md -->
## Cours


Un cours est une ressource.

Un cours est un asset basé sur un cours-ressource. 

Un cours-ressource est:
- une liste d'AAV (aquis d'apprentissage visés) de niveau 1. 
- un lien vers des AATP (aquis d'apprentissage terminaux du programme) qui figurent dans le supplément au diplome.
- une liste de ressources de type section-chapitre.
Un cours-ressource est: une liste de ressources de type section-chapitre.
- associé à une discipline (ceci ne peux être vide et doit être rempli à la création).
- associé à un niveau (niveau des élèves: L1, CM2, BTS, etc voire nomenclature officielle/wims)
- associé à un thème (thème: classement dans la discipline)  


Un cours est un ensemble de notion à assimiler (que l'on représente aussi sous forme de graphe de notion) et qui doit permettre aux étudiants de réussir les exercices qui sont associés au cours. (Exemple:un cours de C, probabilité, python ...)

Il doit être créer par les enseignants et peuvent être éditer par ces derniers.

Chaque cours doit être gérer par un ou plusieurs enseignants.

Il faut au moins un enseignant responsable et editeur.
Le responable peux modifier le cours, ajouter des profs et des élèves.  
L'editeur peut ajouter des activités, modifier les activités.

Il doit contenir des [tags](tag.md) afin de pouvoir être associer à des [exercices](exercice.md).

Chaque cours est accessible à n'importe quel étudiant à condition qu'il soit inscrit dans cette discipline.

Chaque cours contient une ou plusieurs [activités](activity.md).

### Cas d'utilisation associé

[Créer un cours](../casutilisation/enseignant/creercours.md)

[Etudier un cours](../casutilisation/etudiant/etudier.md)

[Réviser un cours](../casutilisation/etudiant/reviser.md)



<!-- coursvide.md -->

## Objet coursvide

Le coursvide est un template d'instance d'asset de cours.

C'est un asset sur une base d'activité, avec un certain nombre d'activités standard (que l'on peut retirer si elles ne sont pas au gout de l'enseignant).
Ces activités sont considérées comme les bases d'un bon cours. 
Avec le cours vide un certain nombre de notifications sont affectées à l'enseignant responsable du cours (mainteneur).


TODO TBC
<!-- cycle_de_kolb.md -->

## Cycle de Kolb

Le "cycle" de l'apprentissage celon Kolb.

Une référene  parmis d'autres
http://cei.ust.hk/files/public/simplypsychology_kolb_learning_styles.pdf
<!-- defi.md -->
## Défis

La compétition permet à un étudiant de lancer un défi à un ou plusieurs autres étudiants de leur classe.
Le créateur du défi doit décider de la deadline du défi.

Il y a plusieurs défis :

* Les défis de rapidité (celui qui termine la feuille le plus rapidement possible).

* Les défis de réussite (celui qui réussit la feuille en utilisant le moins d'essai possible).

* Les défis de taille (programme le plus court pour résoudre un problème).

* Les défis de temps d'éxecution (le programme qui résoud le problème le plus rapidement possible)

Etc ...

Pour cela, il doit choisir une feuille d'exercice, puis il peut ajouter un où plusieurs étudiant de sa classe à une liste. Puis il doit valider le défi. Le défi est ensuite envoyé à chaque utilisateurs de la liste, qui est ainsi notifier avec une [notification](notification.md).

### Cas d'utilisation associé

[donner un défi](../casutilisation/etudiant/donnerexercice.md)

<!---
Author :
Validator : Jordan
-->
<!-- demande.md -->
## Demande (ask)

La demande (Ask) permet à un créateur de demander la création d'un exercice. Pour cela il doit donner une description précise de l'exercice qu'il souhaite avoir:
- discipline 
- niveau 
- sujet 
- cours 
- chapitre
(bien entendu si il souhaite ajouter un exo a son cours/ dans le contexte d'un cours qqcvd tous ces champs sont préremplis).

La création se fait sous la forme d'une requête (stakeoverflow like) dans le logiciel ASK. 

L'utitilisation de ASK structure les discutions sur l'exercice. 
sous question, ups/downs, liens, propositions, etc et KARMA !!




<!-- devoirmaison.md -->
##  Devoir maison

Un devoir maison est une feuille d'exercice que les étudiants doivent faire sur une durée déterminée fixée par un enseignant.

Les exercices de cette feuille sont plus difficiles et plus longs à faire.

L'enseignant peut intervenir pendant la durée du devoir pour éditer le DM de tous les étudiants. (Ex. Pour donner un indice sur un exercice difficile).


[créer/piloter/terminer un devoir maison](../acteurs/casutilisation/enseignant/dm.md)

<!-- discipline.md -->
## Discipline

Toutes les informations : cours, exercices, aav, ressources, sont organisé par disciplines. 

FIXME Une discipline spéciale : humanité, nous sommes tous karmique pour cette discipline et les autres discipline intègre les élements de cette discipline.

La discipline à un nom (clef unique), une description, et un utilisateur référent (dictateur bienveillant) avec un email et des membres (utilisateurs identifiés).

<!-- droits.md -->

Seul un administrateur Django a la possibilité de donner, modifier ou supprimer des droits(CRUD) de tous les utilisateurs autres que des administrateurs django. Par défaut l'administrateur Django a tous les droits.

La visibilité totale désigne le fait de voir toutes les informations de tous les utilisateurs avec leurs noms. En visibilité anonyme, le nom de l'utilisateur à qui les informations appartiennent n'est pas visible. Autrement dit, on ne sait pas à qui appartient les données qu'on regarde en visibilité anonyme.

Les droits des utilisateurs seront stockés dans une table de la base de données où le login sera la clé étrangère et les autres champs correspondent à tout les droits possibles. La valeur de ces champs sera à 1 quand le droit lui est attribué et à 0 quand ce n'est pas le cas.

FIXME comment sotn définis les droits sur les ressources, des bits, des entiers un fichier ??? une table ??? quelle solution de stockage des droits ???


## Utilisateur

Un utilisateur a besoin d'avoir accès à toutes les informations le concernant. Il doit avoir accès à ses feuilles, ses exercices, ses réponses, son profil.  
L'utilisateur a accès en lecture seul à :
- ses exercices
- ses feuilles
- ses réponses

Il a accès en lecture/écriture à :
- son profil

En visibilité totale, l'utilisateur a accès à toutes ses informations.  
En anonyme il n'a accès à rien.



## Groupe

Les groupes sont une manière générique de segmenter les utilisateurs afin de pouvoir leur attribuer des permissions ou de les désigner par un nom défini. Un utilisateur peut appartenir à autant de groupes que nécessaire. Un groupe peut lui-même contenir un groupe.  
Un utilisateur d’un groupe reçoit automatiquement les permissions attribuées à ce groupe.  
Un groupe a accès en lecture seul à :
- ses feuilles
- ses exercices
- ses cours

En visibilité totale, un groupe aura la possiblité de voir que son groupe.  
En anonyme, un groupe n'a aucun droits.



## Enseignant

Un enseignant a besoin d'avoir accès aux informations concernant les étudiants de ses groupes ainsi qu'à ses cours.  
Un enseignant a accès en lecture seul à :
Il a accès en lecture/écriture aux :
- feuilles, exercices et cours (s'ils sont créateurs)

Il a accès en lecture seule :
- résultats de ses étudiants
- feuilles, exercices et cours

En visibilité totale il aura accès à tout ses groupes ainsi qu'à ses cours.  
En anonyme il aura accès aux autres groupes.



## Didacticien

Le didacticien a besoin d'avoir accès à toutes les données concernant le taux de réussite d'un exercice, le temps passé, etc.  
Un didacticien a accès en lecture seule :
- à toutes les données de la classe auquel il est associé

Il a accès en lecture/écriture :
- aux indicateurs

En visibilité anonyme, le didacticien va donc avoir accès à toutes les données.  
En visibilité totale il n'aura accès à rien.



## Responsable

Un responsable a besoin d'avoir accès à tout les groupes et cours dont il est reponsable.  
Un responsable a accès en lecture seule :
- à tout les exercices, feuilles et cours dont il est responsable

Il a accès en lecture/écriture :
- aux groupes dont il est reponsable

En visibilité totale il aura accès à tout ses groupes et cours.  
En anonyme il n'aura accès à rien.


<!-- editeurdechamps.md -->
## Editeur de champs

Mode d'édition ou chaque [balise](balise.md) de pl peut être éditée.
Les balises de pl ont une valeur par défaut que l'on modifie grâce à l'éditeur.
 
<!---
Author : 
Validator : Jordan
-->
<!-- edition.md -->
## Le processus editorial

FIXME (Si le créateur a suffisament de karma pour le valider directement ?) Quand un élément est créer sur pl il est considéré comme public, comme une page wikipédia,
si il est nouveau il est visible mais a le statut **nouveau** (new).
si la discipline n'est pas indiquée il a le statut **perdu** (lost).
si il est non taggé il a le statut **besoin de tag**(needtagging).

si il est validé par un utilisateur de la discipline avec suffisament de [karma](karma.md) il devient **validé**.
Il est **INTERDIT** de valider un exercice non taggé.

une fois que l'exercice a une discipline, un ou plusieurs tag, et qu'il est validé il apparait dans les recherches,
par tag (mot clefs) et dans les classements disciplinaires.

Par exemple: Discipline = informatique/python, tag=functioncall, text= Ecrire une fonction f qui retourne .... 
Si l'on cherche dans les exercices de python il n'appraitra qu'une fois validé.

<!-- eiml.md -->

## EIML 

Livre blanc de EIML : https://pierrelevyblog.com/tag/ieml/


Un outil de manipulation de EIML : intkel.io 
<!-- evaluation.md -->

## Evaluation 

L'alignement pédagogique s'obtient avec trois éléments:
- AAV qui décrit l'objectif observable que doit atteindre l'apprenant 
- activité qui fournis une interaction qui permet à l'apprenant de construire la compétence, le savoir faire corespondant
- évaluation qui est une épreuve qui permet à l'apprenant de valider l'AAV 

Certain aav contiennent directement l'activité et l'évaluation.
AAV: Savoir écrire une bascule en python. Activité : écrire une bascule. Evaluation : vérification automatique de la validité de la bascule. Niveau: Débutant. Public: débutant en programmation python. 


D'autres AAV sont beaucoup plus haut niveau:

AAV: Construire une solution informatique complette.
Niveau: M2, I5
Public: Fin de master, fin d'école d'ingénieur en informatique.

L'aav vas demander d'acquérir de nombreux savoir faire: Elliciter, modéliser, concevoir, programmer, tester, organiser, plannifier, architecturer, controler, qualifier, présenter, négotier. Pour modélisser ces différents objectifs avec des sous aav. 

L'évaluation de l'AAV principal peux s'imaginer de deux façons différentes, soit une approche directe ou l'on place les étudiants dans une cituation leur permettant d'intégrer sur un exemple concret et réaliste l'ensemble de leur formation un jury et leur pairs leur validant leur travail et leur compétence.
Soit l'on a une approche sommative ou la réussite à l'ensemble des sous-aav permet de valider l'aav principal.

Le choix de l'approche varie d'une équipe enseignante à l'autre et des sujets et disciplines participantes de l'aav. 

<!-- exercice.md -->
##  Exercice

Un exercice permet à un utilisateur de s'entraîner de manière autonome.

Il est créé par un enseignant ayant un [karma](karma.md) suffisant ou peut être proposer par un étudiant (l'exercice doit donc être validé par un enseignant ayant aussi un karma suffisant dans la discipline de l'exercice).

Il est corrigé de manière automatique.

Il doit contenir un ou plusieurs [tag](tag.md) permettant de le relier à un [cours](cours.md).

Un exercice doit être placer dans une [feuille d'exercice](feuille.md) par un enseignant pour que les étudiants puissent s'entrainer.

Les exercices à valider doivent apparaitre dans le [centre de notification](centredenotification.md) des enseignants ayant l'autorisation de les valider.

### Cas d'utilisation associé

[créer une exercice](../casutilisation/createur/createexercice.md)

[éditer un exercice](../casutilisation/createur/editerexercice.md)

[donner un exercice à un ou plusieurs étudiants](../casutilisation/enseignant/donnerexercices.md)

[donner un défi](../casutilisation/etudiant/donnerexercice.md)

[Valider un exercice](../casutilisation/enseignant/validation.md)

[faire un exercice](../casutilisation/etudiant/faireexercice.md)

[étudier](../casutilisation/etudiant/etudier.md)

[réviser](../casutilisation/etudiant/reviser.md)

<!---
Author : Hugo
Validator : Jordan
-->
<!-- export.md -->

## Export 

L'export est la possibilité de sauvegarder une ressource PL, bien entendu pour pouvoir l'importer plus tard.

Deux formats d'export/import :
- le format pl avec des = et == 
- le format json

Chaque éléments des modèles django doit avoir deux fonctions export(file,format) et import(file,format).
<!-- feedback.md -->

## Feedback

Bilan sur un exercice, feuille,...


<!-- feuille.md -->
##  Feuille / sheet / pltp

C'est une feuille qui regroupe plusieurs [exercices](exercice.md). Synonyme : pltp.

Chaque feuille est modifiable par les acteurs autorisés (enseignant ou groupe d'enseignant responsable du cours).

La feuille d'exercice n'a pas forcément un thème précis, elle peut être composé de un ou plusieurs [exercices](exercice.md) ayant un thème différent, elle dépend donc du choix de l'enseignant.

Exemple : Une feuille d'exercice de probabilité, une feuille de révision ou encore une feuille d'exercice sur les suites et les séries.

Une même feuille d'exercice peut servir pour plusieurs cours.

Exemple : Une même feuille d'exercice peut servir pour le langage C, python ...

Chaque feuille d'exercice modifiée doit être rechargée afin d'être mises à jour.

### Cas d'utilisation associé

[éditer une feuille](../casutilisation/createur/editerfeuille.md)

[corriger une feuille](../casutilisation/enseignant/corrigerfeuilles.md)

[accéder à une feuille d'exercice](../casutilisation/etudiant/accesfeuilleexercice.md)

<!---
Author : Hugo
Validator : Jordan
-->
<!-- fichierreference.md -->


##  Un fichier référence 

Un fichier référence est un fichier d'extension rf, qui apparait dans l'affichage comme un fichier d'un autre type.
C'est comme un lien symbolique vers le fichier référencé. Les opérations on lieux sur le fichier référencé. 


un fichier.rf contient:
une première ligne contenant le nom du fichier a afficher.
une deuxième ligne contenant la référence a un fichier publique. 


Les opérations faites sur le fichier référence sont faites sur le fichier public.


FIXME les opérations git sur un fichier référencé pose un chalange de code.
<!-- fqm.md -->

| Function   | id   |  Quality        | Mesure         | Description  |
| :----------|:-- | :-------------- | :------------- |:----|
| affiche le tableau de bord           | 1 | Vitesse | <1s | l'affichage du tableau de bord de l'utilisateur ne doit pas être trop longue |
<!-- grader.md -->
## Grader

Un grader est un logiciel python capable d'évaluer un exercice.

Le grader est exécuté sur la sandbox.

La balise correpondante dans un exercice pl est **grader**, cette balise contient un script python,
qui est exécuter sur la sandbox grace à la commande: python3 grader.py

<!---
Author : 
Validator : Jordan
-->
<!-- graph.md -->
##  Graphe

Les graphes sont une succéssion d'étapes qui permet à l'étudiant d'assimiler les notion d'un [cours](cours.md).

Les noeuds du graphe sont des aavs.
Ces aavs contiennent des pré-requis. 
Les prérequis sont des notions à assimiler pour pouvoir assimiler une notions.

Un même graphe peut être utiliser par plusieurs discipline.

Il peut être créer et éditer par un [cercle](cercle.md). 
Chaque utilisateur peut aussi y ajouter des aavs. 
Cependant, l'ajout d'un aav nécéssite la validation du cercle ou d'un enseignant.


<!-- grille.md -->


## Grille 

Grille d'évaluation ou Grille Critériée 

### Struture d'une grille 

In json :
{ "Text du critère" : [ ("Text niveau 1", pointsniveau1), ... ],
  ...
 }
 
 With évaluation :
 { "studentid":{ dic for student id },
   "evaluation":
    { "Text du critère": { niveau, "commentaire" },
       ...
   },
   "grid" :
   { "Text du critère" : [ ("Text niveau 1", pointsniveau1), ... ],
   ...
   },
}

<!-- hint.md -->


hint est une balise qui signale que l'on peut afficher les valeurs attendu dans les messages de test.
<!-- home.md -->


## Home 

Tout utilisateur identifié sur pl à un répertoire home dans lequel il peut écrire des ressources pl. 

Dans le filebrowser ce répertoire est le repertoire home (et pas la racine).

Il est possible dans ce repertoire de connecter un git externe.

Quand un exercice stocké dans le home est publié, il est copié dans la partie publique et effacé de la partie privé. 

à la place un fichier référence est stocké. 

<!-- homologation.md -->

## homologation
 Les AAV ont une phrase d'officialisation/homologation/validation

L'homologation consiste en une vérification par les pairs de la validité d'un AAV et de son intégration dans les AAV "officiels" d'une discipline.

Un aav tout neuf ne devient homologué que quand deux évènement ont eu lieux.
1) des enseignants curateurs de la disciipline on validé l'AAV (il est validé)
2) une ressource et une évaluation correspondantes ont été utilisé avec succès dans un enseignement (il est homologué ).
<!-- indicateur.md -->
## Indicateur

Un indicateur est élément graphique qui affiche des données d'un cours.

Et qui donne des informations visuelles à l'utilisateur.

Un étudiant aura des informations visuelles sur ce qu'il a fait sur la plate-forme (exercice etc..)

Un enseignant aura des informations permettant de suivre une classe, ou un étudiant.

Voir les différents indicateurs qui ont été écrits : [Indicateur](https://github.com/plgitlogin/plconception/tree/9d8b806f842d4f6f1bb9a1cb1767c9eeac992c75/indicateurs)

<!---
Author :
Validator : Jordan
-->

<!-- individualisation.md -->

## Individualisation 


Chaque élève se vois proposer des exercices spécifiques.

<!-- karma.md -->
## Karma

Le karma est un entier qui représente le droit d'un enseignant dans une discipline (Exemple : Prog C, python, java ...).
Chaque enseignant a donc un karma pour chaque discipline. Pour le moment, il existe 3 niveau de karma (0, 1 ou 2).

Exemple : Pour la programmation un enseignant a un karma en informatique, mais pas en mathématiques ni en lettres modernes.

Le karma est privé, il n'est pas visible.
Le karma est gagné en étant actif sur la plateforme.
Un karma  de base peut être déterminé par les diplômes de l'utilisateur (à la discression de l'administrateur).

Le niveau 0 une discipline permet de:
- réponde a des aav de la disicpline
- créer des exercices dans la discipline.

Les droits conférés par le karma au niveau 1 sont :
- la posibilité de valider un aav de la discipline.
- labeliser un exercice de sa discipline.
- manipler (changer les noeux du graph) de ontologie savante.
- valider les ressources de la discipline 

Si un utilisateur atteint le niveau 2, il peut:
* supprimer des exercices (validé ou non).
* supprimer des tags (validé ou non).
* 

### Gain de  karma pour les créateurs 



Pour chaque type de création (exercice ou feuille ou ...), l'enseignant peut gagner un [badge](../concept/badge.md). Il peut obtenir un badge à partir d'un certain palier.
Par exemple, lorsqu'il a créé 10 exercices, il remporte un badge.
Il en gagne un 2ème lorsqu'il en aura créé 50, puis un 3ème lorsqu'il en aura créé 100.
Il en est de même pour les feuilles, les grains et les ressources ...

Chaque création rapporte de la réputation au créateur.
Il gagne :
* 2 Points par commentaire + un point par pouce
* 10 points pour la création d'un exercice + log a base2 de (un point par utilisation)
* 20 points pour la création d'une feuille + log a base2 de (un point par utilisation)
* 20 points pour la création d'un AAV + un point par pouce
* 1000 points pour la création d'une nouveau type d'exercice (donné par un utilisateur karma niveau 10).


### Niveau et Karma 

Un certain nombre de points de karam permet d'atteindre un "niveau". 

Le niveau permet de réalisé certaines actions. 


+ **karma=0** -> niveau 0 
 * possibilité de proposer une nouvelle ressource
 * possibilité de faire une demande d'aav (attention pas un aav mais une demande).

+ **karma>0**  -> niveau 1
 * possibilité de commenter un aav 

+ **karma> (1*ressource+10*comments+) **
<!-- liensressources.md -->

## Rlinks 

Les liens ressource (Rlinks) sont des liens qui pointe sur une ressource, 
il sont parfois affichés comme des  barexos (cf. [barexo](barexo.md)


<!-- link.md -->
## Lien Interne

### Idée Générale :
  L'idée c'est de fournir une syntaxe brève, afin de pouvoir écrire des liens internes vers des ressources de notre système,ainsi quand on parse du text contenant #TYPENUMERO c'est remplacé par un lien vers 
  l'objet de type TYPE et d'ID NUMERO en fonction du type de l'objet c'est le mode preview ou accès  standard comme dans le cas d'une demande.
  
  - Des activités (#A_ID_activity)
  - Des évaluations (#E_ID_eval)
  - Des exercices (#X_ID_exo)
  - Des AAV (#V_ID_AAV)     (tout AAV est une réponse dans un QA)
  - Des QA  (#Q_ID_QA)
  - Des utilisateurs (@User)
  - Des cercles (@0_Cercle)
  
 

Les liens internes seront surtout utilisés dans les AAV et QA.

### Obtention des liens internes :
  Il doit être possible de récupérer le lien interne d'une ressource.

### Syntaxe proposée :
  
Le mieux est de pouvoir référencer tout ce qui concerne des personnes avec `@` suivit du nom de la personne / groupe :

* `@qcoumes`
* `@admin`
* `@AP1_2019`
* `@editor`
* ...

et les objets avec `#` suivit de l'ID de l'objet (`#21`). Il n'est pas forcément nécessaire de différencier l'objet si ceux si possède chacun une clé unique.

<!-- metacognition.md -->

## Meta Cognition

La notion de méta-cognition est en lien avec les notions de réflexivité et d'auto-régulation. 

Exemples de métacognitions : 
- savoir que l'on sait ou que l'on ne sait pas 
- savoir décomposer/ séquencer une action
- savoir quelles sont les actions à entreprendre pour apprendre, pour passer d'un état A à un état B
- savoir le temps et les moyens nécessaires à leur mise en oeuvre. 



<!-- metadonnees.md -->

## Métadonnées 

Les méta données sont des informations associées aux ressources. 

### Méta données automatiques
Les méta données automatiques sont essentiellement statistiques,
nombre d'utilisation, temps de réalisation, temps moyen, temps médian,
nombre de success, nombre d'abandons,
nombre d'intégration dans une activité,
etc. 

Si la ressource est une évaluation (utilisation au moins une fois comme évaluation).



### méta données ajoutées

Les méta données ajoutées doivent être sous une forme distribuée, càd que les éditions des un n'ont pas d'effet sur les éditions des autres.
Ainsi toutes les métas données de ce type sont de la forme:

    user X donne la propriété Y à la ressource.
    la propriété Y est soit un lien entre ressource,soit un json (ce qui permet d'ajouter de nouvelle propréitéé au fur et a mesure).

## Implémentation 

En première lecture pour les donnnées automatiques il faut une table contenant un json avec les données statistiques par ressource. Puis une fois que le système sera un peu plus stabilisé une table avec des entrées fixes pour des recherche plus rapides.

Pour les données ajoutés une deuxième table (ou pas) mais je trouve que l'on a trops de table json qui ne doivent pas être très efficasse ... FIXME.


## Besoin 

Il faut un éditeur de méta données ajoutées.

Il faut spécifier dans le module de stats les stats que l'on stocke dans l


<!-- modelesdexercice.md -->
## Liste des Modèles d'exercices

### Questions à choix multipes
Il peut y avoir une unique ou plusieurs réponses, on pourrait laisser le choix au créateur de décider
de la notation, par exemple :
- Chaque bon choix rapporte un certain nombre de point mais un mauvais met 0 à la question
- Pour avoir le point sur la questions il faut avoir l'ensemble des bonnes réponses\
etc.

L'ordre des choix est aléatoire

Plusieurs questions successives sur un sujet précis.

### Selectionneur

- Possibilité de selectionner des mots dans un texte, un retour visuel indiquant qu'ils ont été
selectionnés devra être mis en place. Les mots selectionnable devront pouvoir être différienciés
par rapport aux mots avec lequels on ne peut pas intéragir.

Exemple :   
Selectionnez les verbes dans la phrases suivante :\
Le **Petit** Chaperon rouge `ramasse` des champignons **hallucinogènes** pour mère-grand qui **dort** 
à la maison

(les mots en gras sont les mots selectionnables et les mots dans une boîte sont ceux selectionnés)

- Possibilité de créer des boîtes interactive que l'ont peut afficher ou cacher avec un clique
 il faudra définir l'état dans lequel l'exercice veut qu'il soit au moment de l'envoi de la réponse
 (élèment visibles et cachés)
 
### Boîte à saisie et menu déroulant

- L'utilisateur rentre la réponse attendue dans la boîte de saisie, la chaîne devra correspondre à celle
attendu par le créateur.

- L'utilisateur pourra cliquer sur le menu déroulant qui proposera une liste de réponses possible
un unique choix est possible

Exemple d'exercices :   
Texte à trous, calculs

### Classement

#### Classement par catégorie
Consiste à ranger des boîtes dans des ensembles, en les déplaçant ou en cliquant sur une boîte et en
cliquant sur l'ensemble dans lequel il faut le ranger.
Exemple : classer les animaux par espèces

#### Classement par relation d'ordre
Trier l'ordre des boîtes (par relation d'ordre logique ou non, par exemple des mots dans une phrases)
en les déplaçant à la position voulue.
Exemple : frise chronologique, classement par taille, <=, taquin etc

#### Relier des boîtes
Permet d'associer par un lien une boîte à une autre, en indiquant graphiqument les liens, il faut
pouvoir selectionner la boîte1 et la boîte2 pour les relier. Possibilité d'avoir un sens dans les liens
Exemple : Relier des dates à des évènements historique

#### Tableau à remplir
Permet de remplir les cases d'un tableau, en mettant des objets dedans : boîtes, checkbox, menu
déroulant ou encore boîte de saisie.
Exemple : remplir un tableau de valeur

### Ressources

Possibilité d'ajouter une ressource de type image, audio et vidéo à tous les modèles précédant.


##  Devoirs (c'est plustot une activité)

Rendus de projet / mémoires / devoir maison (DM).

L'elève doit fournir un (ou plusieurs) fichier(s) comme réponse à l'exercice. 

Eventuellement il est possible d'associer une évaluation automatique à un rendu. 
Eventuellement il est possible d'associer un test de validation du format de fichier à un rendu, le test est réalisé au moment du rendu et si il n'est pas conforme l'élève est prévenu.

Le logiciel permet de noter les rendus, Elève par Elève ou Groupe par Groupe si le devoir est un devoir de groupe.








<!-- niveaucreateur.md -->

## Niveau d'un créateur 

cf. [L'acteur créateur](../acteurs/createur.md)

<!---
Author : 
Validator : Jordan
-->
<!-- notification.md -->
##  Notification

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

<!-- ontology.md -->

## Ontologie

Les ontologie de Premierlangage sont de deux formes, les "ontologie du domaine", qui sont définies sur les aavs (du domaine).
Les "ontologies pratiques" qui sont des ontologies spécifiques à une activité, un cours ou une classe.

Elles sont basées toutes deux sur le même type de donné: Ontologie, la différence est de pouvoir associer dans le premier cas uniquement des aavs, dans le deuxième cas n'importe quelle ressource peut être associée à un noeud de l'ontologie.


Pour pouvoir faire de l’apprentissage adaptatif, il est essentiel de rattacher les exercices à des concepts/ des cartes concepts / à des variables didactiques, à une/des ontologie(s), à des objectifs d’apprentissage visés… Toutes ces informations peuvent être déposées et/ou validées par des acteurs différents : 
    • les didacticiens  
    •  les enseignants  
    • les élèves   
    • à terme des logiciels ...  
Elle n’ont pas  a être forcément absolument cohérentes (il peut y avoir plusieurs écoles de didactique, plusieurs points de vues entre enseignants, entre profils d’étudiants).  

Elles permettent de 
    • faciliter le choix des exercices pour l’enseignant  
    • donner des informations « méta » aux étudiants (une activité pourrait-être de valider et ou proposer de nommer les concepts utilisés dans un exercice)  
    • de faire de l’adaptatif, de la validation des choix des profs (est-ce le meilleur ordre/ adpatation suivant les profils d’étudiants…)  

### Construction d'une ontologie 

Toutes les ontologies sont construite sur le même principe.
Des **objets externes** sont associés de façon univoques à des **noeuds** de l'ontologie. 
Les Noeuds de l'ontologie sont associés par des **relations** typées (le type par défault étant le prérequis).

L'affichage des ontologie ce fait avec un module utilisant graphviz (cf. [Vieux Projet pl](http://pl.univ-mlv.fr) )

### Types logiques 
#### Ontologie du domaine
L'ontologie du domaine est un graphe de Noeuds (chaque Noeud est lié de façon univoque avec un aavs défini dans la discipline).

Les relations entre les Noeuds sont pour le moment (20/02/2019) limités a une relation de prérequis. 
Un aav A est le prérequis du aav B si il faut avoir valider A pour apprendre B.

Elle est utilisée pour représenter les relations dans les connaissances de base d'un domaine/une discipline/un cours particulier.

#### Ontologie Pratiques

Les ontologies pratiques de PL sont utilisées soit pour une representation des connaissance comme les ontologie de domaine. Soit dans une approche plus pratique (d'ou le nom), ou l'ontologie est un outil de gestion de la progresssion de l'élève.

L'ontologie est utilisée pour mesurer l'avancement (avec les Noeuds maitrisés), piloter la progresssion en proposant des exercices à la limites des connaissances de l'élève, exprimer le niveau atteint par l'élève (affichage de la liste des Noeuds limites).

#### Folksonomies

Ontologie créée par les tags donnés par les utilisateurs.




cf. 
http://www.journaldunet.com/developpeur/tutoriel/theo/070403-ontologie.shtml
<!-- pagedediscution.md -->

## Une page de discution

Une page de discution est liée (automatiquement) à chaque ressource.

La page de discution, 
<!-- panier.md -->
## Panier

Quand on travaille à la fabrication d'une feuille automatiquement un panier (futur feuille) est créer dans lequel on place tous les exercices que l'on sélectionne.

Quand on souhaite valider la création le panier contient la liste des exercices pré-sélectionnés.

Il ne reste plus qu'à organiser les exercices (définir l'ordre) idéalement avec du drag en drop.
et fournir l'introduction de la feuille d'exercice (le pltp).


<!---
Author :
Validator : Jordan
-->
<!-- paradox.md -->


## Paradox 

paradox est un glossaire proposant une approche des "learning objects" objets d'apprentissage et fournis un vocabulaire pour en parler.

https://web.archive.org/web/20041019162710/http://rclt.usu.edu/whitepapers/paradox.html

<!-- parametrages.md -->
## Paramétrages

### Le paramétrage ce fait sur un Asset

Voir la définition d'un [ASSET](asset.md).

Le parametrage d'un asset dépendant de son type et des propriétées générales d'un Asset.

### Parametrage d'un exercice 

Les exercices sont paramêtrés (décorés, modifiés etc) par les activités [Activités](activity.md) donc par l'asset de l'activité.


### Quelques exemples de paramêtrages sous WIMS 


Dans un premier temps voici les types de paramétrages disponibles dans WIMS

Nous souhaitons pouvoir utiliser toutes les potentialités des exercices auto-corrigés de WIMS. 

Qu’est-ce qu’un exercice dans WIMS ? 

Pour un étudiant, un exercice est ce qui correspond à une unité d’entrainement avec enregistrement d’une note et qui est visualisé par un carré qui change de couleur au fur et à mesure de la progression dans l’activité. 


Un carré correspond en fait à une « série d’exercices » qui sont choisis parmi les « exercices élémentaires» par le prof. Une série peut correspondre à une unique répétition d’un exercice. 

Un « exercice élémentaire » peut être relativement simple, et ne demander que de remplir un unique champ. Il peut également être plus complexe et nécessiter de remplir de nombreux champs. Une validation binaire n’est donc pas envisageable dans le cas général. 

L’indice de sévérité (entre 1 et 9) va renvoyer une note qui va être plus au moins sévère (maximum de sévérité à 9)  qui dépend du nombre de champs dans lequel la réponse a été correcte (par exemple lorsqu’il y a 4 champs sur 5 de bons avec un indice de 1 la note est proche de 8/10. Dans le cas ou la sévérité est maximale, la note est beaucoup plus faible inférieure à 5/10). 
      
Dans WIMS l’indice de sévérité est fixé au niveau de la « série d’exercice ». Il est figé à partir de l’ouverture de la feuille

Le type de notation (max des réussite, prise en compte ou non de la note de qualité, limitation du nombre de tentatives…) est un paramètre fondamental qui oriente les stratégies de travail des étudiants. 

Dans WIMS, la notation est commune à une feuille, elle peut être modifiée même quand la feuille est active.

Autre type de paramétrages : 
Ouverture et fermeture d’une feuille/ d’un exercice
Dépendance au niveau d’un amphi (a priori pour limiter  le travail du prof), d’un groupe, de l’individualisation. 
discuter/décider des priorités pour les modifications de ces dates : le prof de TD a-t-il ou non la priorité sur le prof d’amphi ?  
d’un individu (l’individualisation est-elle prioritaire sur le travail en groupe : i.e. une fois qu’une activité a été modifiée au niveau individuel, une modification au niveau groupe n’est prise en compte que sous des conditions à définir). 
<!-- partage.md -->


## Partage 
Ce document cherche a definir le cahier des charges du partage des ressources sur la platforme.




### Types de modifications 

(a) les fautes d'orthographes, 
(b) le débuggage, l'amélioration, la traduction 
(c) l' ETIQUETAGE versionning/marking/tagging (donner une  étiquette à une version). 

Comment gère-t-on ces modifications nécessaires ? fait-on simplement confiance ? 
Vient aussi la question de

(d)  l'hérédité. 

Comment des corrections d'un ancêtre vont-elles être transférées à ses descendants ? Faut-il un traitement différent suivant que l'on est dans (a), (b) ou (c) ? 

Faut-il que le système indique que lorsqu'un exercice est hérité un nombre n de fois (n à préciser), on incite à changer l'exercice en question en élément d'une librairie ?  



### Etiquetage des Versions 

Concernant le ETIQUETAGE  il faut une norme éditoriale ? 
Un exemple de problèmatique de tagging : 
- un tag spécifique pour les exercices rédigés à l'infinitif, sur un ton neutre... 
- un autre tag pour les exercices rédigés a la deuxième personne du singulier, sur un ton plus proche. 
- un style csv par défaut très neutre. Avec un tag si on respecte ce style ou pas ? 

PROPOSITION : utiliser les cercles.
Les cercles sont des groupes d'editeur sur la plateforme partageant des objectifs.
Chaque cercle a une aut



### Comment fait-on dans WIMS ?

Les auteurs sont formés à la publication lors de leur premier dépôt. Après on leur fait confiance en général.

Il existe deux endroits d'où un exercice est stocké et d'où il peut être exécuté :

    la classe, et dans ce cas le prof peut faire des modifications dessus en directe, corriger des erreurs, debuggage. En règle général c'est très utile, car on a vite fait de prendre un paramètre trop général.
    le dépôt général. Là seul l'auteur peut faire des motifs et elles sont mises à jour toutes les nuits.

En pratique les exercices sont testés un certain temps dans des classes et débuggués en directe au cours des premières utilisations. Elles sont ensuite publiées si le prof est adoubé. Sinon elles ne sont jamais publiées.

### Défauts de la méthode Wims

Perte d'edition collaborative, il n'y a pas de conservations des modifications et proposition faites localement.

### Avantage 

Le prof peut modifier les exos appliqués a ces élèves "facilement". Sans rendre de comptes.
<!-- personalisation.md -->

## Personalisation 


La personnalisation passe par un diagnostique qui permet de structurer l'élèves de la classe sur plusieurs critères (numeration, factorsation, etc ) en 3 groupes dans chaque critère. 

A: Bon élèves.
B: Ayant besoin d'un support.
C: Nécessitant une adaptation importante
 
Les exercices sont écrit de tel facons qu'ils sont préalablement préparés pour les trois groupes. 

Quand l'élève réalise l'exercice la plateforme lui présente l'exercice avec pour chaque critère pertinant l'adaptation de son niveau/groupe.

 
<!-- planning.md -->
  
  
 # Planning 
 
 le planning d'un cours permet de spécifier les périodes d'ouverture et de fermeture des assets d'un cours.
 
 IL faut dans le planning ajouter le choix d'avoir des alertes associé a la fermeture d'une activité.
 
<!-- plbank.md -->
## Le repertoire plbank

 plbank est un répertoire partagé par toutes les instances de pl. Quelque soit la discipline le langage ou autres.
 
 C'est la bibliothèque standard de pl.
 
 Que trouve-t-on dans plbank :

* les templates de base :
* les "fichier_balises" de base
* les tests de création d'exercice
* les exercices
* les feuilles
* les cours
* les graphes
* les aavs
* ...

<!-- plsyntaxe.md -->
## La syntaxe pl

[Doc pl](https://github.com/plgitlogin/premierlangage/tree/master/repo/plbank/doc)

<!---
Author : Jordan
Validator : Jordan
-->
<!-- portfolio.md -->

## PortFolio

Le portfolio « Collection structurée des travaux d'un étudiant et des commentaires qui leur sont attachés, qui fait foi de ses compétences montrant des traces pertinentes de ses réalisations. Les travaux conservés, et parfois affichés, sont sélectionnés en fonction de critères établis par l'étudiant et par l'enseignant » ( Bibeau, 2007)

Donc un outil parrallèle aux diplomes et certificats qui peut donner une idée plus fine et plus précise des qualités d'un candidat à une embauche. 

Les portfolio dans le cadre PL sont des objets externe pour lesquels nous pouvons fournir des éléments.
FIXME: doit on garder des informations, y a t'il un moyen d'exporté des résultats un format etc.



### Portfolio de présentation

Ce type de portfolio, axé sur le produit final, présente généralement une collection des meilleures productions de l'élève ou celles ayant une valeur plus significative. On peut l'associer au portfolio des artistes.

    Pourquoi? Pour qui?

    Recueille et choisit des productions + commentaires

    Ajoute réflexion (texte d'introduction ou de présentation)

    Présentation (et rétroaction)

#### Méthode

    L'élève (et/ou le prof) détermine/comprend dans quel but (pourquoi) se fait la présentation et à qui elle s'adresse

    L'élève (avec le prof ou seul) choisit ses meilleures productions (ou plus significatives / pertinente) et y ajoute des commentaires et réflexions

    L'élève ajoute une réflexion ou un commentaire plus global (par exemple une introduction, un paragraphe de présentation, ...)

    L'élève présente sa collection à son prof, ses pairs, ses employeurs potentiels ou d'autres personnes intéressées à mieux le connaître et reçoit de la rétroaction 


#### Rôle du prof :

    Soutenir l'élève dans la sélection de ses productions

    Soutenir l'élève dans sa démarche de connaissance de soi


#### Exemple

    Présentation pour une entrevue pour un stage ou un emploi.

    Présenter le résultat d'un travail long (recherche, projet) et recevoir des commentaires formatifs et encouragements!


### Portfolio d'évaluation

Ce type de portfolio permet de porter un jugement sur une collection de productions. Il s'inscrit dans un processus d'évaluation sommative qui permet de vérifier l'atteinte des compétences acquises par l'élève.

    Qu'est-ce qui sera évalué? Critères?

    Même démarche que pour le portfolio de présentation

    Évaluation (jugement) par le ou les profs

#### Méthode

    Le prof explique ce qu'il va évaluer et présente les critères d'évaluation

    L'élève produit un portfolio de présentation (même démarche – avec plus ou moins d'accompagnement) et le présente à son prof

    Le prof porte un jugement à partir du portfolio (évaluation sommative) et le communique

#### Rôle du prof

Préalablement :

    Identifie clairement ce qu'il souhaite évaluer

    Identifie les productions nécessaires (contenu) du PFN et les autres moyens et outils d'évaluation complémentaires nécessaires au besoin (par exemple : entrevue, observation en stage...)

    Élabore une grille d'évaluation à partir de critères et d'indicateurs

    Explique aux élèves que son évaluation se fera sur le contenu et non sur le « contenant » (pour éviter que les élèves passent trop de temps sur le contenant au détriment du contenu)

    Prendre des mesures pour éviter le plagiat : demander des productions personnelles différentes d'un élève à l'autre, demander de voir les traces de la démarche et non seulement le produit fini, etc. 

S'assurer (fournir le soutien nécessaire) que l'élève dépose dans son portfolio des productions lui permettant de porter un jugement éclairé, de faire l'évaluation souhaitée
#### Attention

Être conscient qu'en utilisant le portfolio pour l'évaluation, les élèves seront moins enclins à y montrer leurs moins bons coups et leur réflexion sur leurs difficultés de peur d'influencer le jugement du prof.
#### Exemple

    Portfolio de stage (recueil de productions présentées à la fin du stage)

    Portfolio « bilan » dans le cours

    Épreuve synthèse

### Portfolio d'apprentissage

Ce type de portfolio est plus axé sur le processus d'élaboration du travail de l'élève plutôt que sur le produit final. Il présente généralement une collection de productions et de réflexions faisant foi des progrès de l'élève sur une période donnée. Ce portfolio favorise le processus de métacognition par l'évaluation formative.

    Recueille des productions (tout au long) + réflexions

    Analyse de l'ensemble → buts

    Présentation (prof) + évaluation formative

#### Méthode

    L'élève recueille des productions et les classe

    Il rattache à chacune des productions des commentaires / réflexions

    Il analyse sa collection, se situe dans sa démarche d'apprentissage (ce qu'il a appris et par quel processus), reconnaît ses forces et les améliorations souhaitées, etc.

    Il se fixe des buts pour poursuivre sa démarche d'apprentissage

    Il présente sa collection et son analyse à son prof ou autres personnes pouvant le soutenir dans sa démarche d'apprentissage (rétroaction et évaluation formative)

Ces étapes peuvent être réalisées plusieurs fois!
#### Rôle du prof

    Soutenir l'élève dans le choix ses productions (critères) et leur classement

    Faire de l'évaluation formative

    Aider l'élève à se situer dans sa démarche d'apprentissage, à s'auto-évaluer, à mieux comprendre son processus d'apprentissage, à identifier ses forces et ses difficultés, se fixer des buts, etc.

####  Exemple

    Plan de développement en lien avec la maîtrise de la langue ou d'habiletés TIC

    Portfolio de stage servant à faire un suivi et donner de la rétroaction formative

### Portfolio de développement professionnel

Ce type de portfolio présente une collection de productions et de réflexions documentant son cheminement professionnel dans le temps. Il comprend généralement un curriculum vitæ.

    Recueillir et classer

    Analyser et réfléchir

    Partager (au choix)

#### Méthode

    Recueillir et classer ses productions significatives en fonction par exemple des sections suggérées par Bibeau:

        des disciplines étudiées,

        de ses champs d'intérêt

        des projets réalisés ou en cours de réalisation

    Analyse et réfléchit sur ses productions

    Présente (partage) le contenu choisi de son portfolio

### Portfolio mixte

Il est possible de combiner plusieurs finalités des modèles précédents.
Exempledémarche de réalisation de bilans d'étape dans un programme

    Cueillette et classement des productions tout au long de la formation

    Sélection des productions pour constituer un « dossier » d'apprentissage en fonction des objectifs lors de cours donnés

    Objectivation (prendre conscience de ses apprentissages ainsi que son processus d'apprentissage) principalement avec le « dossier » d'apprentissage lors de cours donnés

    Buts et moyens à prendre pour s'améliorer (ses apprentissages, son processus d'apprentissage) lors de cours donnés

    Préparation et présentation (partage) d'un dossier de présentation à des personnes choisies (profs, pairs, employeurs, etc.).

    Ce dossier pourrait en être un d'évaluation lors de cours donnés. 

#### Remarque

Ces étapes peuvent être réalisées plusieurs fois! 
<!-- previewer.md -->
## Previewer

Le previewer est une zone d'affichage d'un exercice qui permet de tester à la fois l'interface mais aussi le comportement de l'exercice, d'une feuille, d'une strategie etc.

La page est partagée entre l'éditeur et le previewer, il faut pouvoir placer l'éditeur dans un onglet et le préviewer dans un autre, pour les petits écrans.

Dans le previewer il y a des éléments en plus par rapport à l'éxecuteur d'un exercice standard :

- on a une zone ou est affichée la seed et les paramètres par défaut d'une stratégie.

- il est possible de modifier ces valeurs, l'exercice sera alors automatiquement réaffiché avec ces nouveaux paramètres.

Remarques: Ces valeurs ne font pas partie de l'exercice.

<!---
Author : 
Validator : Jordan
-->
<!-- profil.md -->
##  Profil

Le profil permet à un utilisateur connecté de "paramétrer" son compte.
On peut choisir certaines options :
Le mode daltonien
Le mode nuit
Choisir la langue (français, anglais, ...)
Choix d'activation des notifications ou non

Page d'accueil : Par défaut un utilisateur est connecté à la dernière page sur laquelle il était (Session ? Cookie ? en Base ?) ou bien il est toujours placé sur son tableau de bord ou son profil. L'idée est d'avoir une page d'accueil modifiable comme les browsers.

### Cas d'utilisation associé

[Afficher le profil](../casutilisation/utilisateur/affichemodifprofil.md)

<!--- 
Author : Hugo 
Validator : Jordan
-->
<!-- publication.md -->

## Publication 

Deux type de publication des ressources.

1) ajout de la ressources dans une classe. (transformation en asset).

Cette publication a pour effet de déclancher  la deuxième 

2) Publication d'une ressource privé en ressource publique.

<!-- recommandation.md -->

## Recommandation 

apprendre des traces des apprenants création d'un profile de l'apprenant et recherche par similarité:
(agrégation, clustering, ) 
avec des profiles types qui premettent de faire des recommandations aka AMAZON.
<!-- referencement.md -->

## Referencement 

l'idee est de créer une balise markdown friendly pour inclure des liens dans un enoncé PL (du style de la balise latex $% texte latéxifié %$). En imaginant que "type" soit un concept dans une antologie, "balise type balise" produira un lien cliquable dans l'énoncé PL vers la description du concept dans l'ontologie.
<!-- reflexivite.md -->

## Reflexivite

la capacité d'un etudiant
<!-- reputation.md -->
## Réputation

La réputation est un nombre indiquant l'activité d'un enseignant ou d'un étudiant. (Activité == s'il propose des bons tags, des bons exercices, si il gagne des défis ...)

La réputation n'a pas de limite et peut monter à l'infini. Cela permet de valoriser les enseignants et les étudiants faisant un bon boulot. Il est distribué par l'application.

Il augmente lorsque l'enseignant ou l'étudiant propose des exercices et des tags qui ont été validé, lorsqu'il réalise des défis etc...

<!--- 
Author : Hugo 
Validator : Jordan
-->
<!-- ressource.md -->

## Ressources 

Concept gérant le fait qu'un élément de la plateforme doit avoir un certain nombre de propriétés pour être partageable.

Les ressources sont éditables, partagées, versionnées. 
Deux grand types :

- binaires non éditable mais modifiable dans un editeur externe, il faut téléverser le document pour le remplacer. 
- textuelle éditable directement sur le site il bien sur aussi possible de téléverser un document pour le remplacer.


Les ressources peuvent être transformées en [assets](assets.md)  par une publication. 

Les assets sont directement utilisable par les apprenants si il sont dans le contexte d'un cours.
Rem: il est possible de produire des assets de démonstration qui sont accessibleis sur le site principal [demo](demo.md)


### Propriétées des ressources 

Les ressources éditables ont:
- un historique de modification (utilisateur, timestamp, modification)
- un classement dans Yggdrasil (ensemble d'étiquetages obligatoires)
- des aav auquels la ressource participe
- une discution (eventuellement une page loomio)
- une structure de stockage (apriori un fichier de données + fichier de meta data)
- des dépendances: information sur les versions des ressources liées.
- des utilisateurs/propriétaire/observateurs/editeurs/

### Les ressources PL 

Les ressources PL sont stockés dans une arborescence versionnée. (Cloud à la Dropbox ?)
https://www.ubuntupit.com/best-cloud-storage-for-linux-15-reviewed-and-compared-for-linux-nerds/

Les ressources sont des objets de la base de donnée :

1. Une référence sur la dernière version de la ressource et la possibilité de remonter dans les versions … (diff, voir la version , voir le patch) … avoir la date et l’utilisateur … blâme/praise 
2. Meta Data
    1. Statut d’usage (ne pas utiliser, exam, jamais servi, une classe, classes multiples)
    2. Héritage, dépendances, bundle 
    3. Statistiques json complexe voir module de stats 
        1. Nombre de classe utilisant 
        2. Nombre d’utilisation 
        3. Exercices 
            1. Nombre d’essai moyen pour réussir
            2. Taux de réussite 
    4. Labels: (open ended)
        1. Label Rouge
        2. Label Upem
        3. Label Euler
 

### types des ressources PL 
- exercices INFORMATIONS : Fichiers text / pdf / video/ podcast /autres formats non modifiable sur la plateforme 
- Liens vers des documents externes (i.e. pas stockés sur la plateforme (la question du cache ? pour assurer l'existance ? ))
- Tout les types Exercices: avec les codes et données (func.py, valeurs.csv) 
- Tout les types Activités en particulier : Sections/chapitres/cours/listes_de_ressources 
- Protocoles de validations (i.e. activités couplés présentiel / plateforme)




<!-- rights.md -->

## Droits d'acces à une asset-activité

Chaque activité d'un cours a un fiche access rights intialisé au vide i.e. pas d'accès.

Sinon le fichier contient des lignes avec la syntaxe suivante:

Personnes:droits:datedebut:datefin
Personnes pouvant être :
  - * "etoile" pour tous le monde inscrit au cours
  - @groupename pour indiquer tout les inscrits au groupe défini dans le cours (ou la formation a voir).
  - name pour indiquer une personne en particulier (name étant la clef de la base user)

 TODO DR:  ces droits sont insufissants 
 accès
 visibilité mais pas d'accès 
 accès pour évaluation 
 accès en retard
 visibilité après évaluation 
 visibilité de l'évaluation 
 visibilité de l'évaluation correpondante

droits:
  n lire l'exercice avec une note
  x faire l'exercice sans note 
 
Les deux dates. time d'ouverture et de fermeture.



<!-- salon.md -->
##  Salon

Un salon permet aux étudiants d'une même classe de former des groupes de manière autonome.
Un enseignant doit juste décider du nombre d'étudiants par groupes et de la deadline pour créer son binome.
Chaque étudiant peut donc créer un "salon". Les autres étudiants sont par la suite libres de rejoindre un salon parmi tous ceux qui ont été créé. Cependant, le créateur du salon peut accepter ou refuser que l'étudiant en question puisse rejoindre le salon.

Une fois la deadline passé, l'application place les étudiants qui n'ont pas de binôme dans des salons aléatoires (où il reste de la place), ou doit créer des nouveaux salons pour placer les étudiants s'il n'y a plus de place disponible dans les salons existants.

Une fois la deadline passée, les étudiants ont donc tous un salon attribué, et les salons sont validés.

L'appli peut permettre à l'enseignant d'empêcher la constitution d'un même groupe (obliger les groupes à être différents à chaque projet ou encore pour tous les projets).

On peut associer une activité ou un atelier à un salon. 

<!--- 
Author : Hugo
Validator : Jordan
-->
<!-- saloninteractif.md -->
##  Salon interactif

Un salon interactif est un salon créer par les enseignants pour une classe. Chaque étudiant de la classe peut ensuite rejoindre le groupe.

L'enseignant à l'origine du salon doit ajouter une ou plusieurs [feuilles](feuille.md).

Il sélectionne ensuite un exercice à traiter. Cet exercice doit être fait en temps réel. C'est à dire que chaque étudiant du salon interactif peut y participer, et la réponse de chaque étudiant apparaît à l'écran.

Les réponses données par les étudiants sont anonymes ou pas, c'est à l'enseignant de choisir.

<!--- 
Author : Hugo 
Validator : Jordan
-->
<!-- sandbox.md -->
##  Sandbox

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
<!-- seed.md -->
## La seed


La seed est produite par l'activité, si elle n'est pas définie dans l'activité alors elle prend pour valeur 1,2, etc.
La seed est n avec n étant le nombre de fois que l'élève à commencé l'exercice.
Première fois seed=1


La seed d'un exercice est la seed utilisé pour le build de l'exercice.

<!-- shortcuts.md -->

## Les touches de raccourci 

FIXME quelles touches quelles 

<pre>
https://www.w3.org/2002/09/tests/keys.html
</pre>
<!-- sourceexercice.md -->
## Source d'exercice

La source d'un exercice c'est le code qui forme un exercice.
Il est composé de balise et suit la syntaxe [PL](plsyntaxe.md).
Le code est stocké dans un fichier .pl.
<!-- state.md -->


## State (état)


L'état reflette pour un exercice/activité/ressource l'avancement d'un apprenant dans la résolution de l'exercice.

Pour le moment c'est limité à :
- commencé == l'étudiant a vue l'énnoncé mais n'a pas fait de tentative  
- raté == commencé + une tentative infructueuse
- abandonné  == une possibilité de certaines activités équivalent a raté 
- réussi == validé une tentative à été faite est a abouti a un sucess
- jammais vu (null)

Ce principe peut être appliqué au activitées en générales avec un état similaire:
- commencé (équivalent à vu l'énoncé) 
- partiellement fait 
- raté  
- abandonné 
- réussi 
- jammais vu (null)

Validé avec les implémentations


<!-- strategie.md -->
## Stratégie

La stratégie est l'élément qui gère la dynamique d'interaction d'un étudiant avec une feuille d'exercice.

Exemple : 
* Un mode **révision** qui sélectionne les exercices qu'un [étudiant](../acteurs/etudiant.md) n'a pas réussi
ou pas fait, pour lui proposer une suite d'exercices adaptés.

* Un mode **apprendre** qui sélectionne les exercices de base

* Un mode **divertissant** qui permet de défier d'autres étudiants, avec un chrono
et le nombre d'exercices réalisés pendant ce temps imparti

La stratégie peut être créée par un [Enseignant](../acteurs/enseignant.md), il peut lui même définir une stratégie
en lui définissant un nom, et un enchaînement d'exercices, en fonction des données des étudiants.
L'intérêt n'est pas de créer une stratégie individuelle pour chaque élève d'une [classe](classe.md) mais de créer des
stratégies qui puissent s'adapter en fonction des données récoltées qui puissent être adaptées automatiquement pour chaque
étudiants (succès, échecs, nombre d'essais etc)

Cependant un enseignant doit pouvoir avoir la possiblité de créer une stratégie en lien avec des notions ([tags](tag.md))
, et de la **partager via une URL** 


<!--- 
Author : Elaad 
Validator : Jordan
-->
<!-- tableaudebord.md -->
## Dashboard

le tableau de bord d'un utilisateur est la page par défaut toujours accessible avec le lien dashboard (à définir).

Le dashbord d'un utilisateur doit afficher:

Nom (classe/cours courant)
Un résumé visuel de ses résultats en temps réel : proportion de réussite (vert/rouge/organge/etc)
Un placement dans la promo : soit la réussite, soit l'avancement,soit le temps total, soit le % de réussite.

Les badges : dernier badge acquis, nombre de badge, badge le plus important (choix insitutionel mais l'utilisateur peut décider de son badge préféré.

Indicateur de notifications: messages reçus/non lus

Liste de tâches : toutes les choses que doit faire l'utilisateur pour sa classe/cours (étudiant, enseignant), ses actions d'édition (tagger, createur, etc ).

Pour un enseignant, en plus des badges ... il peut voir un onglet avec ses étudiants. Son onglet "Etudiant" diffère selon son nombre d'étudiants.
Exemple : S'il a trop d'étudiant, on peut les trier ou filtrer par promo, td ..., alors qu'on peut tous les afficher s'il n'a pas beaucoup d'étudiant.
A partir de l'onglet étudiant de son dashboard, un enseignant peut cliquer sur n'importe lequel de ses élèves et voir ses statistiques, résultats ...

L'enseignant doit aussi voir dans son dashboard un onglet "validation" qui contient les validations qu'il doit faire, pour les exercices, les tags et les ressources. Il peut trier s'il le souhaite ses validations à faire. (Ex. S'il veut voir que les tags à valider, que les exercices ou que les ressources)

Tous les utilisateurs peuvent également réorganiser leur dashboard (épingler un badge, intervertir 2 catégories ...)

### Cas d'utilisation associé

[modifier son tableau de bord](../casutilisation/enseignant/modifiertableaudebord.md)

[tableau de bord de l'utilisateur](../casutilisation/utilisateur/tableaudebord.md)


https://elearningindustry.com/learner-dashboards-how-effectively-can-it-increase-lms-utility

<!--- 
Author : Hugo 
Validator : Jordan
-->
<!-- taches.md -->

Version 2.0

## Taches

Comme des issues Github, avec un demandeur, des personnes assignées des labels etc.


<!-- tag.md -->
## tag

Un tag est une étiquette attribuée à chaque [exercice](exercice.md) pour définir à quels [aav](aav.md) l'exercice est lié.

Permets de relier une [feuile d'exercice](feuille.md) à un ou plusieurs [aav](aav.md).

Il est choisi par un enseignant (avec un [karma](karma.md) suffisant) et peut aussi être proposé par un utilisateur ayant un accès en édition à l'exercice mais doit être validé par un utilisateur confirmé.
Les [tags](tag.md) en attente de validation doivent apparaitre dans le [centre de notification](centredenotification.md) d'un enseignant pouvant valider ce dernier.

### Cas d'utilisation associé

[valider un tag](../casutilisation/enseignant/validation.md)

<!-- taxonomieofAAV.md -->


## Wiley
### Taxonomie of Learning Oject TYpes

1. Fundamental—For example, a JPEG of a hand playing a chord on a piano keyboard
1. Combined-closed—For example, a video of a hand playing an arpeggiated chord on a piano keyboard with accompanying audio.
1. Combined-open—For example, a Web page dynamically combining the previ- ously mentioned JPEG and QuickTime file together with textual material “on the fly.”
1. Generative-presentation—For example, a JAVA applet capable of graphically generating a set of staff, clef, and notes, which then positions them appropri- ately to present a chord identification problem to a student.
1. Generative-instructional—For example, an EXECUTE instructional transac- tion shell (Merrill, 1999), which both instructs and provides practice for any type of procedure, for example, the process of chord root, quality, and inver- sion identification.

### Charactéristiques

1. Number of elements combined—Describes the number of individual elements (such as video clips, images, etc.) combined in order to make the learning object.
1. Type of elements contained—Describes the type of learning objects that may be combined to form a new learning object.
1. Reusable component objects—Describes whether or not a learning object’s con- stituent objects may be individually accessed and reused in new learning contexts.
1. Common function—Describes the manner in which the learning object type is generally used.
1. Extra-object dependence—Describes whether the learning object needs informa- tion (such as location on the network) about learning objects other than itself.
1. Type of logic contained in object—Describes the common function of algorithms and procedures within the learning object.
1. Potential for inter-contextual reuse—Describes the number of different learning contexts in which the learning object might be used (that is, the object’s poten- tial for reuse in different content areas or domains).
1. Potential for intra-contextual reuse—Describes the number of times the learning object might be reused within the same content area or domain.
<!-- timer.md -->

## Un timer pour un exercice

l'idée est que l'on a une balise timer qui donne en miliseconde le temps que l'on a pour faire l'exercice.






Voici le code d'un timer qui permet de limiter le temps de réalisation d'un exercice.



<pre>
<p id="bob" />
<form>
  <input id="chronotime" value="0:00:00:0" style="width:40px"/>
  </form>

<script>
var initialtime = 61000 // 60000*minutes + 1000 * secondes
var diff = initialtime
var timerID = 0
var timerlength = 100
window.onload = starteverything;


function starteverything(){
document.getElementById("bob").innerHTML = " C'est parti "
chrono()
}

function chrono(){

	if (diff <60000) {
    	 document.getElementById("bob").innerHTML = "Attention plus que 1 Minute"
         document.getElementById("bob").style= "background: #ff9900;"
	}
	if (diff <5000) {
    	 document.getElementById("bob").innerHTML = "Attention plus que 5 secondes"
         document.getElementById("bob").style= "background: #ff0000;"
	}
	if (diff <1) {
    	  document.getElementById("bob").innerHTML = "PERDU !!"
          document.getElementById("bob").style= "background: #000099;color: white;"
          // appeler l'ajax de fin d'exercice (abandon)
         return
	}
	diff = diff - timerlength
    diff=new Date(diff)
	var msec = diff.getMilliseconds()
	var sec = diff.getSeconds()
	var min = diff.getMinutes()

    
	if (min < 10){
		min = "0" + min
	}
	if (sec < 10){
		sec = "0" + sec
	}
	msec = msec/100
	document.getElementById("chronotime").value =  min + ":" + sec + ":" + msec
	timerID = setTimeout("chrono()", timerlength)
}


</script>

</pre>
<!-- todolist.md -->

## Todo liste  (Activité)

La Todo List (liste de courses ;) est une activité que l'on peut ajouter à un cours pour peremmtre à un professeur 
de proposer des exercice à un élève ou un groupe d'élève.

IL faut que le groupe d'élève puisse être fabriqué par une requette sur la réussite de certains exercices, ou d'autre critères comme le temps passé sur la plateforme ou autre.

Les exercices doivent être trouvé avec un mécanisme de recherche similaire (mais sur les exos), voir si le mécanisme de création de feuille ne peut pas être adapté à cet activité.




<!-- travaildegroupes.md -->


## Travail de groupe 


### Formation des groupes 

Taille du groupe: l'enseignant doit définir la taille des groupes ou l'interval de valeurs autorisé [5-7].

Sujet important qui nécesite un outil dans le cas de promotions de grande taille.

Plusieurs stratégies :

- auto-composition 
- tirage aléatoire 
- tirage mixtes :   
    - avec sélection par l'enseigant d'un certain nombre de "leaders" qui forment les tête de groupes 
        - puis auto-composition pour les autres membres 
        - ou sélection aléatoires des autres membres
- auto-selection des leaders (avec déclaration de position de leader)
        - puis auto-composition pour les autres membres 
        - ou sélection aléatoires des autres membres

Il faut que l'outil puisse permettre ces choix , d'autre part la période de création de groupe doit être finie et définitive.

Le mécanisme pour auto-composition est le système des salons et des invitations.

### Objectifs 

Les objectifs sont définis par des **exercices PL** tout les exercices sont possibles,
deux possiblités:
- soit les réponses sont individuelles,
- soit la réponse d'un membre du groupe est valable pour tout le groupe, dernière validation étant conservé comme réponse du groupe.

Bien entendu un exercice pl peut être un rendu de fichier qui peut être une archive donc il n'y a pas de limites a ce que l'on peut demander.
Mais comme un objectif peut avoir un grader on peut imposer des règles formelles sur la forme des documents.


### Outils de communication du groupe 

L'objectif est aussi de former les étudiants à l'utilisation des outils numériques actuels.

La construction d'un document partagé avec un historique des modifications (ainsi il y a une validation effective de la participation de chaqu'un au projet par le truchement de la plateforme), 

Les outils numérique du travail en équie documents partagés, version, chats, workflots, planning etc.



<!-- triggers.md -->
## Triggers



Les Triggers sont des déclencheurs, ils s'activent au cours de certains évènements, une fois activé ils produisent une notification.

Exemple : j'installe une trigger sur une ressource (un template) de façon a être prévenu quand celle ci est modifiée. je choisi de recevoir un mail en plus de ma notification interne. 


Deux familles d'évènements:
- suivi des ressources 
  création/modification/etc d'une ressource triggers au niveau de la base de ressources,
- suivi des élèves (assets): 
 - des notifications pour les profs,
 - des notifications pour les élèves




### Un exemple avec une ressource activité 
Les activités sont stockées en base de données de la manière qui suit :

##### Activity
+ name
+ open
+ type
+ activity_data
+ PL
+ teachers
+ students
+ parent

Si les champs **PL**, **open**, ou **users**  changent, on envoie une notification à tous les étudiants concernés (dans cet exemple)

### Implémentation

Pour la manière dont cela va être implémenté dans PL il y a deux possibilités :
+ Mettre des triggers de notifications un peu partout dans les apps
+ Tout centraliser dans l'app notifs et tout gérer depuis celle-ci

Dans tous les cas chaque user peut subscribe à une activité (par exemple). 

Pour chaque subscribe on ajoute dans une liste en python à quel évènement on a souscrit. Quand une création/modification est faite en base de données on envoie une notification à ceux concernés.

Pour faire ça on utilisera les signaux de Django (presave, postsave etc)
<!-- types.md -->
##  Types

Les types d'exercices :

- question à choix multiple 
- question ouverte (chaine ou integer)
- question de programmation 
- association
- question ouverte multiple (ou  séquence)
- question graphique :
        choix d'un point sur un plan,
        choix d'un ou plusieurs noeuds sur un graphe 
        choix graphique (choix multiple)
        association (drga drop , links)
- coloriage
- saisi de matrice /  fractions / etc 

<!---
Author :
Validator : Jordan
-->
<!-- validation.md -->

## Validation 


Le concept de validation est le fait qu'un élève maitrise ou non une notions.

Plusieurs possibilité de calcul de cette propriété :
- sommative (au moins N exercices sur la notion terminés avec succès).
- certains exercices sont des validateurs le sucess implique la maitrise 
- demander à l'élève son avis : maitrise t'il la notion ?? engagement et reflexion reflexive ....

### Validation d'une activité 

En partant du principe qu'une activité est un ensemble d'exercices, voir de ressources à consulter, est-ce possible de noter cette activité ?

La question est : comment constater qu'une activité est réussie ou échouée ?
Deux options sont souhaitées :

    toutes les ressources doivent être validées
    certaines ressources (réussies, consultées) permettent de valider l'activité : 
    + elles devront être sélectionnées à la création de l'activité
    + Elles pourraient être multiples : soit la ressource 1, soit la resource 1 bis ou les deux

La question se posent aussi pour un cours qui serait un ensemble d'activité


<!-- verificationsyntaxique.md -->
## La verification syntaxique

La vérification syntaxique est un problème qui doit être traité de façon la plus large possible, en effet il est important pour le programmeur d'exercice de comprendre où est l'erreur qui fait que son exercice ne marche pas.

Les erreurs possibles :

1) Syntaxe PL non respectée: pas de préview (ni de chargement de l'exercice)
	exemples: pas de == pour finir un bloc, du code qui traine entre deux balises etc. Avec l'éditeur de champs (qui permet d'éditer les variables/balises une à une ce type d'erreur ne peut pas avoir lieu).

2) Erreur de Syntaxe du python dans une des balises de code.
 -> les balises de code sont : build,before,evaluate

 -> pendant l'exécution d'un exercice:
	la balise  **before** est exécuté pour préparer le dictionnaire qui va servir à l'affichage et la correction, il faut si il y a une exception dans ce code, signaler à l'utilisateur que c'est dans cette balise que se trouve l'erreur. Et il faut calculer la ligne ou a lieu l'erreur et afficher la ligne et la précédente.
	la balise **evaluator** est exécutée pour évaluer la réponse de l'élève. Même problématique il faut signaler que l'erreur est dans évaluator et donner l'exception et la ligne (recalculer) et la précédente.

3) Erreur de Syntaxe et ou d'exécution de la Sandbox, le retour de la sandbox est invalide (genre problème json) il faut que l'affichage soit clair sur le fait que l'erreur a lieu dans la communication avec la sandbox.

4) Erreur de Syntaxe ou d'exécution dans le code de l'étudiant. C'est pour ses pieds mais il faut lui remonter l'information mais c'est au gradeur de le faire dans le champ feedback de la réponse de la sandbox.


$\frac{\sqrt{67}}{88}$

<!-- version.md -->

## Versions 


1- Les Ressources sont sauvegardées en continue dans un git (chaque modification est enregistrée comme dans wikipédia).  
2- Tout le monde partage le même système de gestion de versions  
3- Il est possible de voir les différences avec les versions précédentes  
4- IL est possible de MARKER une version  
<!-- zonetampon.md -->
DEPRECATED 

## La zone tampon

DEPRECATED 

La zone tampon est le travail non terminé d'un utilisateur.
Par exemple si l'on a créée une stratégie mais qu'elle n'est pas encore sauvegardée.


