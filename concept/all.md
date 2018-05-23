#  Atelier

TODO faciliter la compréhension de l'atelier.

FIXME problème pour la note du correcteur parce qu'il peut pas avoir exactement la même note que l'application, à approfondir

Un atelier permet aux étudiants de se corriger entre eux. (Grâce à une grille d'évaluation)
C'est à dire que chaque étudiant doit corriger les exercices plusieurs étudiants (choisis aléatoirement). La correction se fait de manière anonyme.

L'enseignant peut choisir si l'atelier se fait en groupe ou non. Si l'atelier se fait en groupe, chaque groupe corrige donc d'autres groupes (aléatoire aussi).

Un utilisateur ou un groupe doit être corriger par plusieurs utilisateurs/groupe.
La note finale de l'utilisateur/groupe sera la moyenne des notes données par les différents utilisateurs/groupes.
La moyenne permet d'avoir une note "cohérente" (pas basé sur une seule correction).

Pour éviter que les utilisateurs/groupes donnent des notes aléatoires, il faut que la note que donne chaque élève soit comparé à la note donner par l'application (pl). Ce qui génèrera une note pour l'étudiants/groupes qui a corrigé.


La note maximale du correcteur est la note maximale qu'il peut donner en corrigeant.
Après qu'un étudiant ait corrigé et noté un autre étudiant, on réduit à la note maximale du correcteur la différence entre la note donnée par l'application et la note qu'il a lui même donné à l'étudiant.

Exemple :

Un étudiant Toto doit noter un étudiant Titi sur 20. La note maximale qu'il peut donner est donc 20/20. L'application (pl) donne une note de 18/20 à Titi et Toto donne la note de 10/20 à Titi. Après avoir noté Titi, Toto obtient une note pour la qualité de sa correction. La note maximale que Toto peut attribuer est de 20 et le delta est de 8, Toto obtient donc un 12/20 pour sa correction.

<!---
Author : Hugo
Validator : Jordan
-->
# AVIS Exercice

L'avis d'un exercice c'est ce que l'utilisateur a pensé de ce dernier (trop dur, trop facile, ...) après l'avoir terminé.

Les avis peuvent être proposer à la fin de chaque exercices (réussite ou échec) car ils ont peu d'intérêt si l'étudiant n'a pas fait l'exercice.
Ils peuvent aussi être proposer lorsque l'étudiant a terminé la feuille d'exercice (Ou une partie des exercices), il peut donc donner son avis que sur les exercices qu'il a tenté.

Ils sont représentés par des cases à cocher en plus d'une zone de texte "commentaire" qui permet aux étudiants d'écrire leur pensée sur l'exercice ou bien de justifier leur(s) choix.
L'étudiant peut cocher plusieurs options (choix) s'il le veut. Les cases à cocher sont des options qui peuvent être créer, modifier, supprimer par un administrateur (CRUD).

Un avis est facultatif, il n'est pas obligé de cocher des options et/ou remplir la zone de texte "commmentaire".

Chaque avis est anonyme.

En cas d'échec, il faut essayer de savoir pourquoi l'utilisateur n'a pas réussi à faire l'exercice.

Il faut faire attention car il y a 2 cas d'échec différents :

Soit il a échoué sans avoir essayer (ex. abandon au bout de 10s).

Soit il a échoué en ayant essayer.

S'il n'a pas essayé, il ne lui propose pas de donner son avis, il peut donc directement passer au prochain exercice.

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

Récompense attribuée à un acteur, attestée par un logo visuel, et ouvrant des droits étendus.

Exemple de récompense visuelle possible : https://threejs.org/examples/webgl_materials_reflectivity.html

<!---
Author : Hugo
Validator : Jordan
-->

# Balises

Champs d'un exercice une feuille ou un cours.

Les exercices pl sont des dictionnaires, chaque couple clef valeur est appellée une balise. Par exemple :
text==
coucou c'est l'énoncé
==
Est une balise text contenant "\ncoucou c'est l'énoncé\n"

Berk="kiki"
est une balise Berk contenant '"kiki"'

Une balise ne peut être None.  

Il existe de nombreux types de balises (title, from,extends etc..).


<!---
Author : 
Validator : Jordan
--># Centre de notification

Le centre de notification regroupe l'ensemble des notifications d'un utilisateur.

Il est accessible à n'importe quel moment dans le menu.

Il peut être désactiver par l'utilisateur dans le [profil](profil.md), ce qui annule toute alertes.

<!---
Author : Hugo
Validator : Jordan
-->

# Les cercles 

Les cercles sont des ensembles d'utilisateurs.
Les cercles ont un propriétaire et des administrateurs capables d'accepter et virer des utilisateurs.
Les cercles ont des labels propres qui permettent d'étiqueter les exercices.

Le cercle par défaut de tout les créateurs est le cercle créateurs. On y est inscrit par défault. 
(on peut se faire virer ....).

Les cercles ont un forum associé.

<!---
Author :
Validator : Jordan
-->#  Classe

TODO définir précisement l'acteur responsable

Une classe a un nom.

Une classe est un ensemble d'étudiant.

Un ou plusieurs [cours](/cours.md) peuvent être affecté à une classe par un acteur (TODO à définir).

Une classe a un niveau: CM2, 6ème, Terminal, L2, M1

<!---
Author : Hugo
Validator : Jordan
-->
# Compétition

TODO penser à ajouter des compétitions

La compétition permet à un étudiant de lancer un défi à un ou plusieurs autres étudiants de leur classe.
Le créateur du défi doit décider de la deadline du défi.

Il y a plusieurs défis :

* Les défis de rapidité (celui qui termine la feuille le plus rapidement possible).

* Les défis de réussite (celui qui réussi la feuille en utilisant le moins d'essai possible).

* Les défis de taille (programme le plus court pour résoudre un problème).

* Les défis de temps d'éxecution (le programme qui résoud le problème le plus rapidement possible)

TODO

Pour cela, il doit choisir une feuille d'exercice, puis il peut ajouter un où plusieurs étudiant de sa classe à une liste. Puis il doit valider le défi. Le défi est ensuite envoyé à chaque utilisateurs de la liste, qui est ainsi notifier avec une [notification](notification.md).

# Cours

Un cours est un ensemble de notion à assimiler (que l'on représente aussi sous forme de graphe de notion) et qui doit permettre aux étudiants de réussir les exercices qui sont associés au cours. (Exemple:un cours de C, probabilité, python ...)

Il doit être créer par les enseignants et peuvent être éditer par ces derniers.

Chaque cours doit être gérer par un ou plusieurs enseignants.

Il doit contenir des [tags](tag.md) afin de pouvoir être associer à des [exercices](exercice.md).

Chaque cours est accessible à n'importe quel étudiant à condition qu'il soit inscrit dans cette discipline.

Chaque cours contient une ou plusieurs [feuilles d'exercice](feuille.md).

<!---
Author : Hugo
Validator : Jordan
-->
#  Devoir maison

Un devoir maison est une feuille d'exercice que les étudiants doivent faire sur une durée déterminer qui est fixé par un enseignant.

Les exercices de cette feuille sont plus difficile et plus long à faire.

L'enseignant peut intervenir pendant la durée du devoir pour éditer le DM de tous les étudiants. (Ex. Pour donner un indice sur un exercice difficile).

<!---
Author : Hugo
Validator : Jordan
-->
# Editeur de champs

Mode d'édition ou chaque [balise](/balise.md) de pl est éditée.
 
<!---
Author : 
Validator : Jordan
-->#  Exercice

Un exercice permet à un utilisateur de s'entraîner de manière autonome.

Il est créé par un enseignant ayant un [karma](karma.md) suffisant ou peut être proposer par un étudiant (l'exercice doit donc être validé par un enseignant ayant aussi un karma suffisant dans la discipline de l'exercice).

Il est corrigé de manière automatique.

Il doit contenir un ou plusieurs [tag](tag.md) permettant de le relier à un [cours](cours.md).

Un exercice doit être placer dans une [feuille d'exercice](feuille.md) par un enseignant pour que les étudiants puissent s'entrainer.

Les exercices à valider doivent apparaitre dans le [centre de notification](centredenotification.md) des enseignants ayant l'autorisation de les valider.

<!---
Author : Hugo
Validator : Jordan
-->
#  Feuille

C'est une feuille qui regroupe plusieurs [exercices](exercice.md). Synonyme : pltp.

Chaque feuille est modifiable par les acteurs autorisés (enseignant ou groupe d'enseignant responsable du cours).

La feuille d'exercice n'a pas forcément un thème précis, elle peut être composé de un ou plusieurs [exercices](exercice.md) ayant un thème différent, elle dépend donc du choix de l'enseignant.

Exemple : Une feuille d'exercice de probabilité,une feuille de révision ou encore une feuille d'exercice sur les suites et les séries.

Une même feuille d'exercice peut servir pour plusieurs cours.
Exemple : Une même feuille d'exercice peut servir pour le langage C, python ...

Chaque feuille d'exercice modifiée doit être rechargée afin d'être mises à jour.

<!---
Author : Hugo
Validator : Jordan
-->
# Grader

Un grader est un logiciel python capable d'évaluer un exercice.

Le grader est exécuté sur la sandbox.

La balise correpondante dans un exercice pl est **grader**, cette balise contient un script python,
qui est exécuter sur la sandbox grace à la commande: python3 grader.py

<!---
Author : 
Validator : Jordan
-->
# Grain

TODO être plus précis

Un grain est une notions (Ex. Probabilités) qui est associer à une ressource (Ex. cours, exercices...) et qui peut être associer à d'autres grains.

Une autre approche des grains est celle utilisée dans les cours : https://docs.moodle.org/3x/fr/Objectifs les objectifs pédagogiques.
# Karma

TODO compléter attribution du karma de départ, compléter les exemples.

Le karma est un nombre de points sur 20 qui représente le niveau d'un enseignant dans une discipline (Exemple : Prog C, python, java ...).
Chaque enseignant a donc un karma pour chaque discipline. Le maximum de point possible est donc 20 et le minimum est 0.
Exemple : Pour la programmation un enseignant a un karma en C, python, compilation, caml ...

Le karma est privé, il n'est pas visible par les étudiants mais il est visible par les enseignants.

Le karma s'obtient de plusieurs manières, libre à chaque académie de choisir sa méthode.

Un inspecteur académique peut décider de donner du karma (entre 0 et 20 points) à un enseignant à n'importe quel moment.

Le karma peut être déterminer par les diplômes de l'utilisateur.

Plusieurs enseignants peuvent décider du karma d'un enseignant. (Ensuite attribuer par l'admin)
Exemple: Un groupe d'enseignants décide de donner 15 de karma à un enseignant, l'administrateur se charge donc de mettre 15 points de karma à cet enseignant.

relation (comme linkedin)

Un enseignant peut valider un tag ou un exercice proposé par un utilisateur s'il a au minimum 15 points dans la discipline de l'exercice.
Exemple : Un enseignant qui a 15 points de karma en C peut valider les exercices et les tags proposés par des utilisateurs en C.

Le karma n'est pas défintif, il est évolutif. C'est à dire qu'à tout moment son karma peut être modifier avec les méthodes du dessus.

Exemple :

Un inspecteur d'académie décide d'augmenter/diminuer le karma d'un enseignant car il le trouve meilleur/moins bon.

Un enseignant obtient une agrégation de mathématique, son karma va donc augmenter.

<!---
Author : Hugo 
Validator : Jordan
-->






# Niveau d'un créateur 

cf. [L'acteur créateur]( plconception/acteurs/createur.md)

<!---
Author : 
Validator : Jordan
-->
#  Notification

Une notification est un message qui alerte l'utilisateur.

Chaque notification apparait dans le [centre de notification](centredenotification.md),avec un message indiquant ce pourquoi on a été notifé.

On peut notifer une classe, plusieurs utilisateurs, ou un utilisateur en particulier.

Exemple :
Pour un étudiant : Ajout d'un nouveau cours, d'une nouvelle feuille d'exercice.
Pour un enseignant : exercices à valider, tags à valider, ajout d'un avis sur ses exercices/cours.

<!---
Author : Hugo
Validator : Jordan
-->


# Panier 

quand on travail à la fabrication d'une feuille autonatiquement un panier (futur feuille) est créer dans lequel on place tout les exercices que l'on sélectionne.

Quand on souhaite valider la création le panier contient la liste des exercices pré-sélectionnés.

Il ne reste plus qu'a organiser les exercices (définir l'ordre) idéalement avec du drag en drop.
et fournir l'introduction de la feuille d'exercice (le pltp).


# la syntaxe pl

[Doc pl](premierlangage/repo/plbank/doc/)

<!---
Author : Jordan
Validator : Jordan
-->
# Previewer

Le previewer est une zone d'affichage d'un exercice qui permet de tester à la fois l'interface mais aussi le comportement de l'exercice.

La page est partagé entre l'éditeur et le previewer, il faut pouvoir de placer l'editeur dans un onglet et le préviewer dans un autre, pour les petits écrans.

Dans le previewer il y a des élements en plus par rapport à l'executeur d'un exercice standard :

- on a une zone ou est affichée la seed et les paramêtres par défaut d'une stratégie.

- il est possible de modifier ces valeurs, l'exercice sera alors automatiquement réaffiché avec ces nouveaux paramêtres. 

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
page d'accueil : Par défaut un utilisateur est connecté à la dernière page sur laquelle il était (Session ? Cookie ? en Base ?) ou bien il est toujours placé sur son tableau de bord ou son profil. L'idée est d'avoir une page d'acceuil modifiable comme les browsers.

<!--- 
Author : Hugo 
Validator : Raphael 
-->
# Réputation

TODO rajouter des critères pour gagner de la réputation, fixer les règles (si tout le monde commence à la même réputation)

La réputation est un nombre indiquant l'activité d'un enseignant. (Activité == s'il propose des bons tags, des bons exercices, ...)

La réputation n'a pas de limite et peut monter à l'infini. Cele permet de valoriser les enseignants faisant un bon boulot. Il est distribué par l'application.

Il augmente lorsque l'enseignant propose des exercices et des tags qui ont été validé.

<!--- 
Author : Hugo 
Validator : Raphael 
-->
#  Salon

TODO approfondir l'idée

Un salon permet aux étudiants d'une même classe de former des groupes de manière autonome.
Un enseignant doit juste décider du nombre d'étudiant par groupe et de la deadline pour créer son binome.
Chaque étudiant peut donc créer un "salon". Les autres étudiants sont par la suite libre de rejoindre un salon parmis tous ceux qui ont été créé. Cependant, le créateur du salon peut accepter ou refuser que l'étudiant en question puisse rejoindre le salon.

Une fois la deadline passé, l'application place les étudiants qui n'ont pas de binome dans des salons aléatoires (où il reste de la place), ou doit créer des nouveaux salons pour placer les étudiants s'il n'y a plus de place disponible dans les salons existants.

Une fois la deadline passer, les étudiants ont donc tous un salon attribué, et les salons sont validés.

L'appli peut permettre à l'enseignant d'empêcher la constitution d'un même groupe (obliger les groupes à être différents à chaque projet ou encore pour tous les projets).

<!--- 
Author : Hugo
Validator : Raphael 
-->
#  Salon interactif

Un salon interactif est un salon créer par les enseignants pour une classe. Chaque étudiant de la classe peut ensuite rejoindre le groupe.

L'enseignant à l'origine du salon peut ensuite ajouter des exercices.

Les exercices associés sont des exercices de type QCM.

Chaque étudiant dans le groupe peut donc choisir la réponse qui lui semble être la bonne.

Cela permet donc à l'enseignant de voir le taux de réponse pour chaque réponse du QCM.

Les réponses données par les étudiants sont anonymes

<!--- 
Author : Hugo 
Validator : Raphael 
-->
# Stratégie

La stratégie est l'élément qui gère la dynamique d'interaction d'un étudiant avec une feuille d'exercice.

Exemple : 
* Un mode **révision** qui sélectionne les exercices qu'un [étudiant](../acteurs/etudiant.md) n'a pas réussi
ou pas fait, pour lui proposer une suite d'exercices adapté.

* Un mode **apprendre** qui sélectionne les exercices de base

* Un mode **divertissant** qui permet de défier d'autres étudiants, avec un chrono
et le nombre d'exercice réalisé pendant ce temps imparti

La stratégie peut être crée par un [Enseignant](../acteurs/enseignant.md), il peut lui même définir une stratégie
en lui définissant un nom, et un enchaînement d'exercices, en fonction des données des des étudiants.
L'intérêt n'est pas de créer une stratégie individuelle pour chaque élève d'une [classe](classe.md) mais de créer des
stratégies qui puissent s'adapter en fonction des données récoltés qui puisse être adapté automatiquement pour chaque
étudiants (succès, échecs, nombre d'essais etc)

Cependant un Enseignant doit pouvoir avoir la possiblité de créer une stratégie en lien avec des notions ([tags](tag.md))
, et de la **partager via une URL** 


<!--- 
Author : Elaad 
Validator : -
-->
# Dashboard

le tableau de bord d'un utilisateur est la page par défaut toujours accessible avec le lien dashboard (à définir).

Le dashbord d'un utilisateur doit afficher:

Nom (classe/cours courant)
Un résumé visuel de ses résultats en temps réel : proportion de réussite (vert/rouge/organge/etc)
Un placement dans la promo : soit la réussite, soit l'avancement,soit le temps total, soit le % de réussite.

Les badges : dernier badge acquis, nombre de badge, badge le plus important (choix insitutionel mais l'utilisateur peut décider de son badge préféré.

Indicateur de notifications: messages reçus/non lus

liste de taches : toutes les choses que doit faire l'utilisateur pour sa classe/cours (étudiant, enseignant), ses actions d'édition (tagger, createur, etc ).

Pour un enseignant, en plus des badges ... il peut voir un onglet avec ses étudiants. Son onglet "Etudiant" diffère selon son nombre d'étudiant.
Exemple : S'il a trop d'étudiant, on peut les trier par promo, td ..., alors qu'on peut tous les afficher s'il n'a pas beaucoup d'étudiant.
A partir de l'onglet étudiant de son dashboard, un enseignant peut cliquer sur n'importe lequel de ses élèves et voir ses statistiques, résultats ...

L'enseignant doit aussi voir dans son dashboard un onglet "validation" qui contient les validations qu'il doit faire, pour les exercices, les tags et les ressources. Il peut trier s'il le souhaite ses validations à faire. (Ex. S'il veut voir que les tags à valider, que les exercies ou que les ressources)

Tous les utilisateurs peuvent également réorgansier leur dashboard (épingler un badge, intervertir 2 catégories ...)

<!--- 
Author : Hugo 
Validator : Raphael 
-->
# tag

Un tag est une étiquette attribuée à chaque [exercice](exercice.md) pour lui définir à quels [grain](grain.md) l'exercice est lié.
Permet de relier un [exercice](exercice.md) à un ou plusieurs [grain](grain.md).
Il est choisi par un enseignant (avec un [karma](karma.md) suffisant) et peut aussi être proposé par un utilisateur ayant un accès en édition à l'exercice mais doit être valider par un utilisateur confirmé.
Les [tags](tag.md) en attente de validation doivent apparaitre dans le [centre de notification](centredenotification.md) d'un enseignant pouvant valider ce dernier.

<!--- 
Author : Hugo 
Validator : Raphael 
-->
# La verification syntaxique

La vérification syntaxique est un problème qui doit être traité de façon la plus large possible, en effet il est important pour le programmeur d'exercice de comprendre ou est l'erreur qui fait que son exercice ne marche pas.

Les erreurs possibles :

1) Syntaxe PL non respectée: pas de préview (ni de chargement de l'exercice)
	exemples: pas de == pour finir un bloc, du code qui traine entre deux balises etc. Avec l'editeur de champs (qui permet d'editer les variables/balises une à une ce type d'erreur ne peut pas avoir lieu).

2) Erreur de Syntaxe du python dans une des balise de code.
 -> les balises de code sont : build,before,evaluate,
	(TODO: il serait bien que la liste soit stockée quelque part).
 -> pendant l'exécution d'un exercice:
	la balise  **before** est exécuté pour préparer le dictionnaire qui va servir à l'affichage et la correction, il faut si il y a une exception dans ce code, signaler à l'utilisateur que c'est dans cette balise que se trouve l'erreur. Et il faut calculer la ligne ou a lieu l'erreur et afficher la ligne et la précédente.
	la balise **evaluator** est exécutée pour évaluer la réponse de l'élève. Même problèmatique il faut signaler que l'erreur est dans évaluator et donner l'exception et la ligne (recalculé) et la précédente.

3) Erreur de Syntaxe et ou d'execution de la Sandbox, le retour de la sandbox est invalide (genre problème json) il faut que l'affichage soit clair sur le fait que l'erreur à lieu dans la communication avec la sandbox. 

4) Erreur  de Syntaxe ou d'exécution dans le code de l'étudiant. C'est pour ses pieds mais il faut lui remonter l'information mais c'est au gradeur de le faire dans le champs feedback de la réponse de la sandbox.


 
# la zone tampon

La zone tampon est le travail non terminé d'un utilisateur.
Par exemple si l'on créer une stratégie mais qu'elle n'est pas encore sauvegardée.

DR: je ne sais pas ou la stocker dans un répertoire perso de l'utilisateur, dans la base de donnée.


