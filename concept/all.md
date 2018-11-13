
# Droits d'acces à une activité

Chaque activité d'un cours a un fiche access rights intialisé au vide== pas d'accès.

Sinon le fichier contient des lignes avec la syntaxe suivante:

Personnes:droits:datedebut:datefin
Personnes pouvant être :
  - * "etoile" pour tous le monde inscrit au cours
  - @groupename pour indiquer tout les inscrits au groupe défini dans le cours (ou la formation a voir).
  - name pour indiquer une personne en particulier (name étant la clef de la base user)

droits:
  n lire l'exercice avec une note
  x faire l'exercice sans note 
 
Les deux dates.time d'ouverture et de fermeture.



# Actions

Les actions sont une formalisation des activités des utilisateurs sur le site PL.

Une action est faite par un utilisateur et une ressource. 
Les actions de base sont:
- CreateReadUpdateDelete pour les ressources 
- validate/Annotate i.e. modification des métadata d'une ressource 

La réalisation (success) d'une action entraine des opération du système:
- Quand un exercice est validé, le propriétaire de l'exercice est notifié, et sa réputation est augmentée, le validateur gagne aussi en réputation. 



## Table des actions 
| Action | Description | URL/URI | Droits | Qui est notifié |
|--------|-------------|---------|--------|-----------------|
|Créer exercice |Créer un nouvel exercice|  /discipline/createexercice | Avoir le rôle de créateur  |[Responsable de formation](acteurs/reponsable)|
|Créer exercice en ajoutant des paramètres de notification|             |         |        |                 |
|        |             |         |        |                 |

# Activité

L'activité est l'unité de partage entre les LMS (moodle and co) et PL.

FIXME Une activité à une URL qui peut être utilisé dans le connecteur LTI. Le connecteur LTI définie un identifiant externe qui est utilisé pour identifier l'activité dans PL.

Une activité peut être utilisé dans plusieurs cours, mais il existe une instance distincte pour chaque cours. 

Une activité contient à minima une Stratégie standard et au moins un fichier pltp.

Une activité exporte des tableaux de bord : studentactivitydashboard, teacheracivitydashboard utilisables dans les tableaux de bords correspondants.

une activité a une navigation 
Une activité a un barème (outil permettant le calcul d'une note).

Activité= S+ F*+ sd* td* I N B  
i=introduction  
S= Strategie   
F= pltp  
sd=student dashboard  
td=teacher dashboard  
N=navigation  
B=Barem (comment est calculé la nte qui remonte à moodle)


Références : modules WIMS

# studentactivitydashboard

Tableau de bord exporté par une activité retourne une div contenant un indicateur (voir les tableaux de bord)
qui peut être intégré dans le tableau de bord d'un etudiant.

# teacheractivity dashboard 

indicateur qui peut être intégré dans le tableau de bord d'un enseignant
# Area51

Area51 est la zone qui contient tous les exercices qui ne sont associé à aucune discipline et/ou cours.
Elle contient tous les exercices qui ne sont pas créé à partir d'un cours.
Un créateur peut cliquer sur un bouton [créer exerxice](../casutilisation/createur/createexercice.md).

<!---
Author : Hugo
Validator : 
-->
#  Atelier

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
# AVIS Exercice

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


# Badge

 Un badge est une récompense attribuée à un acteur, attestée par un logo visuel, et ouvrant eventuellement des droits.

## Quelques exemples 

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
# Balises

Champs d'un exercice une feuille ou un cours.

Les exercices pl sont des dictionnaires, chaque couple clef valeur est appelé une balise. 

Par exemple :
<pre>
  text==
  coucou c'est l'énoncé
  ==
</pre>

Est une balise texte contenant "coucou c'est l'énoncé\n"

<pre>
Berk="kiki"
</pre>
est une balise Berk contenant '"kiki"'

Une balise ne peut être None.  

Il existe de nombreux types de balises (title, from,extends etc..).

<!---
Author : DR
Validator : Jordan
-->
# Barre d'exercice

La barre d'exercice est un affichage HTML d'un exercice sur une seul ligne. 

C'est une barre contenant la discipline de l'exercice, son niveau, son nom, un metadata (validité, liste des cercle où il est).

La bare contient des boutons qui permettent différentes actions:  
-preview lance une nouvelle fenetre de preview de l'exercice   
-extends lance une fenetre d'edition d'un exercice ititialisé avec la ligne extends= référence de l'exercice de la bare d'exercice  
-fork lance une fenetre d'edition de l'exercice lui même avec la sauvegarde qui fabriquera un pull request.

Il est aussi possible de cliquer sur un bouton affichant la discussion sur l'exercice en question et un autre pour afficher un indicateur (à choisir). 

Les badges de l'exercice sont visibles: Labbel Rouge, académie de Versailles, LDAR++, comprehénsible, sans Fôtes.

# BARREFEUILLE

TODO
un affichage intelligent d'un lien de feuille de TP.
avec plein de goodies
# Centre de notification

Le centre de notification regroupe l'ensemble des notifications d'un utilisateur (Validation, Défi, Groupe etc..).

Il est accessible à n'importe quel moment dans le menu, il se trouve dans l'en-tête de premier language.

L'utilisateur peut désactiver les notifications qu'il veut dans le [profil](profil.md), ce qui annule toutes alertes.


<!---
Author : Hugo
Validator : Jordan
-->
# Les cercles

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
# Chat bot

Robot de discussion.
L'idée est  que les élèves connectés à une activité peuvent partager un tchat.
L'enseignant peut aussi y participer, ainsi il a accès à ce que font les étudiants.
En plus il peut envoyer des messages privés et envoyer des documents aux élèves.


<!---
Author :
Validator : Jordan
-->#  Classe

Une classe a un nom.

Une classe est un ensemble d'étudiant.

Un ou plusieurs [cours](cours.md) peuvent être affecté à une classe par l'acteur [AdminLMS](../acteurs/adminLMS.md).

Une classe a un niveau: CM2, 6ème, Terminal, L2, M1

## Cas d'utilisation associé

[Suivre une classe](../casutilisation/enseignant/suivreclasse.md)  
[adminsitration LMS](../casutilisation/adminLMS/administrationlms.md)


<!---
Author : Hugo
Validator : Jordan
-->

# Classe ouverte 

Une classe ouverte est une [classe](./classe.md) accessible à tous.


<!---
Author :
Validator : Jordan
--># Classification disciplinaire

### WIMS Taxonomie

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
# Cours

Un cours est un ensemble de notion à assimiler (que l'on représente aussi sous forme de graphe de notion) et qui doit permettre aux étudiants de réussir les exercices qui sont associés au cours. (Exemple:un cours de C, probabilité, python ...)

Il doit être créer par les enseignants et peuvent être éditer par ces derniers.

Chaque cours doit être gérer par un ou plusieurs enseignants.

Il faut au moins un enseignant responsable et editeur.
Le responable peux modifier le cours, ajouter des profs et des élèves.  
L'editeur peut ajouter des activités, modifier les activités.

Il doit contenir des [tags](tag.md) afin de pouvoir être associer à des [exercices](exercice.md).

Chaque cours est accessible à n'importe quel étudiant à condition qu'il soit inscrit dans cette discipline.

Chaque cours contient une ou plusieurs [activités](activity.md).

## Cas d'utilisation associé

[Créer un cours](../casutilisation/enseignant/creercours.md)

[Etudier un cours](../casutilisation/etudiant/etudier.md)

[Réviser un cours](../casutilisation/etudiant/reviser.md)



<!---
Author : Hugo
Validator : Jordan
-->
# Défis

La compétition permet à un étudiant de lancer un défi à un ou plusieurs autres étudiants de leur classe.
Le créateur du défi doit décider de la deadline du défi.

Il y a plusieurs défis :

* Les défis de rapidité (celui qui termine la feuille le plus rapidement possible).

* Les défis de réussite (celui qui réussit la feuille en utilisant le moins d'essai possible).

* Les défis de taille (programme le plus court pour résoudre un problème).

* Les défis de temps d'éxecution (le programme qui résoud le problème le plus rapidement possible)

Etc ...

Pour cela, il doit choisir une feuille d'exercice, puis il peut ajouter un où plusieurs étudiant de sa classe à une liste. Puis il doit valider le défi. Le défi est ensuite envoyé à chaque utilisateurs de la liste, qui est ainsi notifier avec une [notification](notification.md).

## Cas d'utilisation associé

[donner un défi](../casutilisation/etudiant/donnerexercice.md)

<!---
Author :
Validator : Jordan
-->
# Demande (ask)

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




#  Devoir maison

Un devoir maison est une feuille d'exercice que les étudiants doivent faire sur une durée déterminer qui est fixé par un enseignant.

Les exercices de cette feuille sont plus difficiles et plus longs à faire.

L'enseignant peut intervenir pendant la durée du devoir pour éditer le DM de tous les étudiants. (Ex. Pour donner un indice sur un exercice difficile).

<!---
Author : Hugo
Validator : Jordan
-->
# Discipline

Toutes les informations : cours, exercices, grains, ressources, sont organisé par disciplines. 

FIXME Une discipline spéciale : humanité, nous sommes tous karmique pour cette discipline et les autres discipline intègre les élements de cette discipline.

La discipline à un nom (clef unique), une description, et un utilisateur référent (dictateur bienveillant) avec un email et des membres (utilisateurs identifiés).

# Editeur de champs

Mode d'édition ou chaque [balise](balise.md) de pl peut être éditée.
Les balises de pl ont une valeur par défaut que l'on modifie grâce à l'éditeur.
 
<!---
Author : 
Validator : Jordan
-->
# Le processus editorial

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

#  Exercice

Un exercice permet à un utilisateur de s'entraîner de manière autonome.

Il est créé par un enseignant ayant un [karma](karma.md) suffisant ou peut être proposer par un étudiant (l'exercice doit donc être validé par un enseignant ayant aussi un karma suffisant dans la discipline de l'exercice).

Il est corrigé de manière automatique.

Il doit contenir un ou plusieurs [tag](tag.md) permettant de le relier à un [cours](cours.md).

Un exercice doit être placer dans une [feuille d'exercice](feuille.md) par un enseignant pour que les étudiants puissent s'entrainer.

Les exercices à valider doivent apparaitre dans le [centre de notification](centredenotification.md) des enseignants ayant l'autorisation de les valider.

## Cas d'utilisation associé

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
# Liste des Modèles d'exercices

## Questions à choix multipes
Il peut y avoir une unique ou plusieurs réponses, on pourrait laisser le choix au créateur de décider
de la notation, par exemple :
- Chaque bon choix rapporte un certain nombre de point mais un mauvais met 0 à la question
- Pour avoir le point sur la questions il faut avoir l'ensemble des bonnes réponses\
etc.

L'ordre des choix est aléatoire

Plusieurs questions successives sur un sujet précis.

## Selectionneur

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
 
## Boîte à saisie et menu déroulant

- L'utilisateur rentre la réponse attendue dans la boîte de saisie, la chaîne devra correspondre à celle
attendu par le créateur.

- L'utilisateur pourra cliquer sur le menu déroulant qui proposera une liste de réponses possible
un unique choix est possible

Exemple d'exercices :   
Texte à trous, calculs

## Classement

### Classement par catégorie
Consiste à ranger des boîtes dans des ensembles, en les déplaçant ou en cliquant sur une boîte et en
cliquant sur l'ensemble dans lequel il faut le ranger.
Exemple : classer les animaux par espèces

### Classement par relation d'ordre
Trier l'ordre des boîtes (par relation d'ordre logique ou non, par exemple des mots dans une phrases)
en les déplaçant à la position voulue.
Exemple : frise chronologique, classement par taille, <=, taquin etc

### Relier des boîtes
Permet d'associer par un lien une boîte à une autre, en indiquant graphiqument les liens, il faut
pouvoir selectionner la boîte1 et la boîte2 pour les relier. Possibilité d'avoir un sens dans les liens
Exemple : Relier des dates à des évènements historique

### Tableau à remplir
Permet de remplir les cases d'un tableau, en mettant des objets dedans : boîtes, checkbox, menu
déroulant ou encore boîte de saisie.
Exemple : remplir un tableau de valeur

## Ressources

Possibilité d'ajouter une ressource de type image, audio et vidéo à tous les modèles précédant.


#  Devoirs (c'est plustot une activité)

Rendus de projet / mémoires / devoir maison (DM).

L'elève doit fournir un (ou plusieurs) fichier(s) comme réponse à l'exercice. 

Eventuellement il est possible d'associer une évaluation automatique à un rendu. 
Eventuellement il est possible d'associer un test de validation du format de fichier à un rendu, le test est réalisé au moment du rendu et si il n'est pas conforme l'élève est prévenu.

Le logiciel permet de noter les rendus, Elève par Elève ou Groupe par Groupe si le devoir est un devoir de groupe.









# Export 

L'export est la possibilité de sauvegarder une ressource PL, bien entendu pour pouvoir l'importer plus tard.

Deux formats d'export/import :
- le format pl avec des = et == 
- le format json

Chaque éléments des modèles django doit avoir deux fonctions export(file,format) et import(file,format).

# Feedback

Bilan sur un exercice, feuille,...


#  Feuille / sheet / pltp

C'est une feuille qui regroupe plusieurs [exercices](exercice.md). Synonyme : pltp.

Chaque feuille est modifiable par les acteurs autorisés (enseignant ou groupe d'enseignant responsable du cours).

La feuille d'exercice n'a pas forcément un thème précis, elle peut être composé de un ou plusieurs [exercices](exercice.md) ayant un thème différent, elle dépend donc du choix de l'enseignant.

Exemple : Une feuille d'exercice de probabilité, une feuille de révision ou encore une feuille d'exercice sur les suites et les séries.

Une même feuille d'exercice peut servir pour plusieurs cours.

Exemple : Une même feuille d'exercice peut servir pour le langage C, python ...

Chaque feuille d'exercice modifiée doit être rechargée afin d'être mises à jour.

## Cas d'utilisation associé

[éditer une feuille](../casutilisation/createur/editerfeuille.md)

[corriger une feuille](../casutilisation/enseignant/corrigerfeuilles.md)

[accéder à une feuille d'exercice](../casutilisation/etudiant/accesfeuilleexercice.md)

<!---
Author : Hugo
Validator : Jordan
-->


#  Un fichier référence 

Un fichier référence est un fichier d'extension rf, qui apparait dans l'affichage comme un fichier d'un autre type.
C'est comme un lien symbolique vers le fichier référencé. Les opérations on lieux sur le fichier référencé. 


un fichier.rf contient:
une première ligne contenant le nom du fichier a afficher.
une deuxième ligne contenant la référence a un fichier publique. 


Les opérations faites sur le fichier référence sont faites sur le fichier public.


FIXME les opérations git sur un fichier référencé pose un chalange de code.

| Function   | id   |  Quality        | Mesure         | Description  |
| :----------|:-- | :-------------- | :------------- |:----|
| affiche le tableau de bord           | 1 | Vitesse | <1s | l'affichage du tableau de bord de l'utilisateur ne doit pas être trop longue |
# Le glossaire PL

Est un glossaire partagée (modifiable avec les droits adminstrateur).
Qui contient les mots utilisés dans le logiciel.

Le glossaire fait partie de la doc.


<!---
Author :
Validator : Jordan
--># Grader

Un grader est un logiciel python capable d'évaluer un exercice.

Le grader est exécuté sur la sandbox.

La balise correpondante dans un exercice pl est **grader**, cette balise contient un script python,
qui est exécuter sur la sandbox grace à la commande: python3 grader.py

<!---
Author : 
Validator : Jordan
-->
# Grain

Un grain est une notion ou un objectif pédagogique.

Une autre approche des grains est celle utilisée dans les cours : https://docs.moodle.org/3x/fr/Objectifs les objectifs pédagogiques.

## Cas d'utilisation associé

[Editer un grain](../casutilisation/createur/editergrain.md)

<!---
Author :
Validator : Jordan
-->#  Graphe

Les graphes sont une succéssion d'étape qui permet à l'étudiant d'assimiler les notion d'un [cours](cours.md).

Les noeuds du graphe sont des grains. Ces grains contiennent des pré-requis. Les prérequis sont des notions à assimiler pour pouvoir assimiler une notions.

Un même graphe peut être utiliser par plusieurs discipline.

Il peut être créer et éditer par un [cercle](cercle.md). Chaque utilisateur peut aussi y ajouter des grains. Cependant, l'ajout d'un grain nécéssite la validation du cercle ou d'un enseignant.

<!---
Author :
Validator : Jordan
-->

hint est une balise qui signale que l'on peut afficher les valeurs attendu dans les messages de test.


# Home 

Tout utilisateur identifié sur pl à un répertoire home dans lequel il peut écrire des ressources pl. 

Dans le filebrowser ce répertoire est le repertoire home (et pas la racine).

Il est possible dans ce repertoire de connecter un git externe.

Quand un exercice stocké dans le home est publié, il est copié dans la partie publique et effacé de la partie privé. 

à la place un fichier référence est stocké. 

# Indicateur

Un indicateur est élément graphique qui affiche des données d'un cours.

Et qui donne des informations visuelles à l'utilisateur.

Un étudiant aura des informations visuelles sur ce qu'il a fait sur la plate-forme (exercice etc..)

Un enseignant aura des informations permettant de suivre une classe, ou un étudiant.

Voir les différents indicateurs qui ont été écrits : [Indicateur](https://github.com/plgitlogin/plconception/tree/9d8b806f842d4f6f1bb9a1cb1767c9eeac992c75/indicateurs)

<!---
Author :
Validator : Jordan
-->

# Karma

Le karma est un entier qui représente le droit d'un enseignant dans une discipline (Exemple : Prog C, python, java ...).
Chaque enseignant a donc un karma pour chaque discipline. Pour le moment, il existe 3 niveau de karma (0, 1 ou 2).

Exemple : Pour la programmation un enseignant a un karma en informatique, mais pas en mathématiques.

Le karma est privé, il n'est pas visible.
Le karma est attribué par un Administrateur.
Le karma peut être déterminer par les diplômes de l'utilisateur.

Le niveau 0 ne confère aucun droit à l'utilisateur.

Les droits conférés par le karma au niveau 1 sont :
- la posibilité de valider un grain de la discipline.
- tagger un exercice.
- manipler (changer les noeux du graph) le graph savant.
- valider les ressources de la discipline 

Si un utilisateur atteint le niveau 2, en plus des droit du niveau 1, il peut:
* supprimer des exercices (validé ou non).
* supprimer des tags (validé ou non).

# Implementation 

une bonne idée (a valider) c'est d'uiliser un cercle pour implémenter le karma.


<!--
Author : Hugo 
Validator : Jordan
-->

<!--
AJETER :

Un inspecteur académique peut décider de donner du karma (entre 0 et 20 points) à un enseignant à n'importe quel moment. L'administrateur se chargera de modifier le karma.


Le karma s'attribut de plusieurs manière, libre à chaque académie de choisir sa méthode. Le karma est par défaut à 0.

Plusieurs enseignants peuvent décider du karma d'un enseignant. (Ensuite attribuer par l'admin)
Exemple: Un groupe d'enseignants décide de donner 15 de karma à un enseignant, l'administrateur se charge donc de mettre 15 points de karma à cet enseignant.

relation (comme linkedin), chacun peut donner du karma.

Un enseignant peut valider un tag ou un exercice proposé par un utilisateur s'il a au minimum 15 points dans la discipline de l'exercice.
Exemple : Un enseignant qui a 15 points de karma en C peut valider les exercices et les tags proposés par des utilisateurs en C.

Le karma n'est pas défintif, il est évolutif. C'est à dire qu'à tout moment son karma peut être modifier avec les méthodes du dessus.

Exemple :

Un inspecteur d'académie décide d'augmenter/diminuer le karma d'un enseignant car il le trouve meilleur/moins bon.

Un enseignant obtient une agrégation de mathématique, son karma va donc augmenter.

-->







# metadonnées 

Mot outil pour parler des attributs des exercices, feuilles, 

# Niveau d'un créateur 

cf. [L'acteur créateur](../acteurs/createur.md)

<!---
Author : 
Validator : Jordan
-->
# Node

Un noeud est une référence vers un grain. Ils constituent un graphe.

<!--
Author :
Validator : Jordan
-->

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


#Ontologie/Objectifs d’apprentissage visés/ Concepts/ Variables didactiques

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
# Panier

Quand on travaille à la fabrication d'une feuille automatiquement un panier (futur feuille) est créer dans lequel on place tous les exercices que l'on sélectionne.

Quand on souhaite valider la création le panier contient la liste des exercices pré-sélectionnés.

Il ne reste plus qu'à organiser les exercices (définir l'ordre) idéalement avec du drag en drop.
et fournir l'introduction de la feuille d'exercice (le pltp).


<!---
Author :
Validator : Jordan
-->#Paramétrage 

[Le parametrage sous WIMS](Paramétrage d'une feuille dans WIMS.odt)

Dans un premier temps voici les types de paramétrages disponibles dans WIMS

Nous souhaitons pouvoir utiliser toutes les potentialités des exercices auto-corrigés de WIMS. 

Qu’est-ce qu’un exercice dans WIMS ? 


Pour un étudiant, un exercice est ce qui correspond à une unité d’entrainement avec enregistrement d’une note et qui est visualisé par un carré qui change de couleur au fur et à mesure de la progression dans l’activité. 


Exemple de deux feuilles d’exercices, la première comporte 8 unités et la seconde 14. 


Un carré correspond en fait à une « série d’exercices » qui sont choisis parmi les « exercices élémentaires» par le prof. Une série peut correspondre à une unique répétition d’un exercice. 

Un « exercice élémentaire » peut être relativement simple, et ne demander que de remplir un unique champ. Il peut également être plus complexe et nécessiter de remplir de nombreux champs. Une validation binaire n’est donc pas envisageable dans le cas général. 

    • L’indice de sévérité (entre 1 et 9) va renvoyer une note qui va être plus au moins sévère (maximum de sévérité à 9)  qui dépend du nombre de champs dans lequel la réponse a été correcte (par exemple lorsqu’il y a 4 champs sur 5 de bons avec un indice de 1 la note est proche de 8/10. Dans le cas ou la sévérité est maximale, la note est beaucoup plus faible inférieure à 5/10). 
      
Dans WIMS l’indice de sévérité est fixé au niveau de la « série d’exercice ». Il est figé à partir de l’ouverture de la feuille

    • Le type de notation (max des réussite, prise en compte ou non de la note de qualité, limitation du nombre de tentatives…) est un paramètre fondamental qui oriente les stratégies de travail des étudiants. 

Dans WIMS, la notation est commune à une feuille, elle peut être modifiée même quand la feuille est active.

Autre type de paramétrages : 
    • Ouverture et fermeture d’une feuille/ d’un exercice
        ◦ Dépendance au niveau d’un amphi (a priori pour limiter  le travail du prof), d’un groupe, de l’individualisation. 
            ▪  discuter/décider des priorités pour les modifications de ces dates : le prof de TD a-t-il ou non la priorité sur le prof d’amphi ?  
            ▪ d’un individu (l’individualisation est-elle prioritaire sur le travail en groupe : i.e. une fois qu’une activité a été modifiée au niveau individuel, une modification au niveau groupe n’est prise en compte que sous des conditions à définir). 
# Le repertoire plbank

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
* les grains
* ...

<!---
Author :
Validator : Jordan
--># La syntaxe pl

[Doc pl](https://github.com/plgitlogin/premierlangage/tree/master/repo/plbank/doc)

<!---
Author : Jordan
Validator : Jordan
-->
# Previewer

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
#  Profil

Le profil permet à un utilisateur connecté de "paramétrer" son compte.
On peut choisir certaines options :
Le mode daltonien
Le mode nuit
Choisir la langue (français, anglais, ...)
Choix d'activation des notifications ou non

Page d'accueil : Par défaut un utilisateur est connecté à la dernière page sur laquelle il était (Session ? Cookie ? en Base ?) ou bien il est toujours placé sur son tableau de bord ou son profil. L'idée est d'avoir une page d'accueil modifiable comme les browsers.

## Cas d'utilisation associé

[Afficher le profil](../casutilisation/utilisateur/affichemodifprofil.md)

<!--- 
Author : Hugo 
Validator : Jordan
-->

# Referencement 

l'idee est de créer une balise markdown friendly pour inclure des liens dans un enoncé PL (du style de la balise latex $% texte latéxifié %$). En imaginant que "type" soit un concept dans une antologie, "balise type balise" produira un lien cliquable dans l'énoncé PL vers la description du concept dans l'ontologie.
# Réputation

La réputation est un nombre indiquant l'activité d'un enseignant ou d'un étudiant. (Activité == s'il propose des bons tags, des bons exercices, si il gagne des défis ...)

La réputation n'a pas de limite et peut monter à l'infini. Cela permet de valoriser les enseignants et les étudiants faisant un bon boulot. Il est distribué par l'application.

Il augmente lorsque l'enseignant ou l'étudiant propose des exercices et des tags qui ont été validé, lorsqu'il réalise des défis etc...

<!--- 
Author : Hugo 
Validator : Jordan
-->
#  Salon

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
#  Salon interactif

Un salon interactif est un salon créer par les enseignants pour une classe. Chaque étudiant de la classe peut ensuite rejoindre le groupe.

L'enseignant à l'origine du salon doit ajouter une ou plusieurs [feuilles](feuille.md).

Il sélectionne ensuite un exercice à traiter. Cet exercice doit être fait en temps réel. C'est à dire que chaque étudiant du salon interactif peut y participer, et la réponse de chaque étudiant apparaît à l'écran.

Les réponses données par les étudiants sont anonymes ou pas, c'est à l'enseignant de choisir.

<!--- 
Author : Hugo 
Validator : Jordan
-->
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
# La seed


La seed est produite par l'activité, si elle n'est pas définie dans l'activité alors elle prend pour valeur 1,2, etc.
La seed est n avec n étant le nombre de fois que l'élève à commencé l'exercice.
Première fois seed=1


La seed d'un exercice est la seed utilisé pour le build de l'exercice.

# Source d'exercice

La source d'un exercice c'est le code qui forme un exercice.
Il est composé de balise et suit la syntaxe [PL](plsyntaxe.md).
Le code est stocké dans un fichier .pl.
# Stratégie

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
# Dashboard

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

## Cas d'utilisation associé

[modifier son tableau de bord](../casutilisation/enseignant/modifiertableaudebord.md)

[tableau de bord de l'utilisateur](../casutilisation/utilisateur/tableaudebord.md)


https://elearningindustry.com/learner-dashboards-how-effectively-can-it-increase-lms-utility

<!--- 
Author : Hugo 
Validator : Jordan
-->
# tag

Un tag est une étiquette attribuée à chaque [exercice](exercice.md) pour définir à quels [grain](grain.md) l'exercice est lié.

Permets de relier une [feuile d'exercice](feuille.md) à un ou plusieurs [grain](grain.md).

Il est choisi par un enseignant (avec un [karma](karma.md) suffisant) et peut aussi être proposé par un utilisateur ayant un accès en édition à l'exercice mais doit être validé par un utilisateur confirmé.
Les [tags](tag.md) en attente de validation doivent apparaitre dans le [centre de notification](centredenotification.md) d'un enseignant pouvant valider ce dernier.

## Cas d'utilisation associé

[valider un tag](../casutilisation/enseignant/validation.md)

<!--- 
Author : Hugo 
Validator : Jordan
-->

# Un timer pour un exercice

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

# TOdo liste 

l'idée est d'avoir des exos qu'un enseignant à donner à l'élève.
#  Types

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
# Validation 


Le concept de validation est le fait qu'un élève maitrise ou non une notions.

Plusieurs possibilité de calcul de cette propriété :
- sommative (au moins N exercices sur la notions terminé avec succè).
- certains exercices sont des validateurs le sucess implique la maitrise 
- demander à l'élève son avis : maitrise t'il la notion ?? engagement et reflexion reflexive ....


<!--
remarques pour la recherche :
- comment rendre cohérent l'autoévaluation et l'evaluation par le système
quel feedback proposer en méta cognition à l'élève en cas d'incohérence.


-->

# La verification syntaxique

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


<!---
Author :
Validator : Jordan
--># La zone tampon

La zone tampon est le travail non terminé d'un utilisateur.
Par exemple si l'on a créée une stratégie mais qu'elle n'est pas encore sauvegardée.


<!---
Author :
Validator : Jordan
-->