# Activities

An activity is the link between PL and the Learning Management System (LMS) such as Moodle.

The LMS defines an id for the activity that can be used with the name of the LMS to identify the activity in PL.

An activity can be used in multiple courses but there is a distinct instance of the activity per course.

An activity has at least a standard strategy and a PLTP file.

Activité= S + F* + (sd* td* I N B)
I  = Introduction + Documentation
S  = Strategie
F  = pltp + (decorators)
sd = student dashboard
td = teacher dashboard
N  = navigation
B  = Barem (comment est calculé la nte qui remonte à moodle)



Réflexion de Borie et Revuz  :


# Ressources

## Classes / Cours /  Activités   :


 On définit comme ressource des données informatiques éditables qui participe dans les unité d’enseignement de notre plateforme. 
Essentiellement il y a les  grandes catégories de ressources suivantes :
* les exercices: unité atomique dont l’objectif de construction et de conception est que cette unité soit facilement partageable 
* les documents : tout les documents classiques : texte, video, etc
* les activités: regroupement de ressource et d'éléments de programmables ayant un objectif pédagogique (AAV), une stratégie pour atteindre cet objectif, et une évaluation permettant de valider l’objectif.
* les cours/classes : les cours sont une organisation dans le temps d’individus (prof, élèves) regroupe des ressources et des éléments programmable, les cours affiche un ensemble d’objectifs pédagogiques, un cours doit proposer suffisamment d’activités pour atteindre et valider ces objectifs.


Présuppositions : 
=============

* L'unité atomique de ressources pédagogiques à partager est l'exercice (exo.pl).[ ne pas oublier les documents]
* l’activité doit être une ressource facile à partager et réutiliser 
* Les cours sont des assemblages d'autres ressources plus fine.
* Objectif : il faut séparer les activités de l'édition (a minima pour le développement).


* Stratégie : il paraît plus simple de commencer par les activités en
  prévoyant leur extensibilité avec l'édition pressentie.
* Les activités doivent être concues en même que leur workflow management.
* Les enseignants éditeurs proposent principalement des exercices et des activités
  (i.e. des ressources atomiques).
* Les cours sont plus proposées par des enseignants effectifs (i.e. devant une classe avec une
  stratégie pédagogique.)

l'idée est que le prof souhaite utiliser la plateforme pour sont cours :
- il doit définir des Objectifs Pédagogiques/ AAV (premier cas d'utilisation ou nous devons l'aider).
- il doit en suite trouver/choisir/ecrire des activitées pefrmettant d'atteindre les objectifs et les évaluer
- les activités en question ont besoin pour fonctionner des matériaux plus élé"mentaires : documents, exercices , données, il doit de nouveau trouver/choisir/ecrire ces ressources.
- enfin il doit faire le chef d'orquestre pour les activités: cad choisir le moment ou les etudiant ont accès au différentes ressources et activités.
- Pour cela il doit pouvoir faire le suivi des étudiants 
  

Workflow management : 
=====================

* Un peu comme la page de moodle fait un récapitulatif des matières ou
  l'utilisateur est inscrit, le workflow management devrait faire un
  récapitulatif des activités en cours de l'utilisateur de premier
  langage.
* Est-ce que Workflow management ne devrait pas s'appeler "Portail
  activités" avec un récap de l'avancement visuel rapide pour chaque
  activités ?
* Ce Workflow management est fortement conditionné par le rôle : les
  élèves voient des choses relative à leur travail, les enseignants
  voient des choses relatives à l'avancement de leur promotion.
* Le Workflow management a vocation à afficher rapidement :
  * L'avancement sur l'activité (8 / 12 TPs)
  * Les interactions pour chaque activités. (2 conseils non lus)
  * Les alertes pour chaque activités. (En retard de 4 exercices)
  * Les attendus. (1 travail à rendre dans xx jours et yy heures)
* Les activités listées sont cliquables pour aller vers un dashboard
  d'activité bien plus précis.

Activités : (à faire valider par D.R.)
===========

* Une activités est un assemblage complexe de ressources pédagogique
  plus légère. [ ceci est aussi valables pour un cours]
* Une activité a vocation à contenir une **scénarisation** et une
  stratégie pédagogique : par exemple 12 TP de difficulté croissante
  rassemblant des exercices de plus en plus durs portant sur des
  notions incrémentales (chaque TP introduisant une nouvelle notion,
  le dernier TP les utilisant toutes en même temps).
* L'activité a aussi pour fonction de calibrer ses contenus (temps
  limité, délais de rendus, objectifs didactiques, validation des
  acquis). Ces spécifications seront principalement assurés par des
  décorateurs.
* L'activité doit prévoir :
  * sa notation globale (Prévoir un default)
  * ses dashboards élèves et enseignants (Prévoir un default)
  * son rythme (notion de phase ??? ) (Prévoir un default)
    * phase 1 : un pdf de cours + un TP...
    * phase 2 : un nouveau TP
    * phase 3 : un autre pdf + encore un TP + un TP noté temps limité en séance prof
    * ...
  * son déploiement : bouton cliquable pour les enseignants : (activer phase x)
  * Les alertes élèves (Prévoir un default)
  * Les alertes enseignants (Prévoir un default)
* Une activité se joue possiblement sur un longue durée. Elle doit
  aussi resté modifiable durant son exécution (rajout d'un TP avant la
  fin et modification de la notation finale).
* De ce fait, une activité a un curseur temporel durant son exécution,
  les enseignants responsables peuvent déplacer ce curseur d'activité.


Décorateurs d'exercices :
=========================

* Limitation de temps (1 minutes par questions de QCM)
* nombre d'essais limités (tentatives de réponse limité : QCM avec 3 choix...)
* répétitions (jouer plusieurs fois le même exo (vaudrait mieux aléatoire...))
* Visibilité/disponibilité (programmé ou encore activé/désactivé)

Exemple :
@repeat(3)
@appempt(1)
@exo_aleatoire.pl
--> L'élèves doit réussir 3 fois l'exo du premier coup pour valider
    son exercice dans l'activité. L'enseignant considère qu'après 3
    résolutions d'un coup, c'est que l'élève a forcement compris.

Décorateurs de feuille d'exercices :
====================================

* Limitation de temps (2 heures)
* Visibilité/disponibilité (programmé ou encore activé/désactivé)
* Obligation de faire des exercices dans l'ordre (c'est un problème incrémental)
* Interdire de revenir en arrière (la solution de l'exo 2 est dans l'exo 3)

Exemple :
@start_on_click(duration=2.1)
@tp_note_2h_phase4.pltp
--> Le TP contenu dans l'activité ne sera disponible et visible que
    lorsque qu'un enseignant responsable de l'activité aura activer
    manuellement le TP vis un bouton dans son dashboard. Le TP sera
    disponible 2,1 heures (donc 2 heures et 6 minutes ici).
    Le clic par le prof sur le bouton ouvre les portes du tp pour les
    élèves. Avant le TP apparaissant mais un clic disait : "Ressources
    pas encore disponible"


Activités en autonomie :  OUAIS EXCELLENT
========================

* Révision / Remise à niveau / Curieux / Évaluation

* Révision : préparation avant une épreuve
* Remise à niveau : travail en autonomie pour rattraper un niveau, des notions
* Curieux : ben quoi ? ça me fait rire de faire des exos ! D'autre c'est Pokémon !
* Évaluation : Je fais quelques exercices et la plate-forme me juge automatiquement.

Toutes ses activités doivent s'appuyer sur un pool fini (mais
possiblement énorme) d'exercices


Points soulevés :
=================

* DANGER : Pour rendre les COURS partageables, il va falloir bien
  réfléchir sur leur personnalisation et leur pilotage...
  * Que peut-on partager ?
  * Quelles sont les parties à pérenniser ?
  * Quelles sont les parties à ignorer ?
  * Quelles sont les parties humain-dépendant ?

* A TERME : Un éditeur de Cours et d'activité de pltp et de pl !!!!

* DANGER : La gestion du temps sera un challenge ! Par analogie, si
  l'activité est une classe Python, sa réalisation concrète est une
  instance de classe (en gros durant la semaine 3 sur 12 semaine de la
  matière...). Partager une classe Python (son code), ça
  va... Partager une instance de classe est rarement raisonnable.
  L'activité, la classe Python : le scénario Sa réalisation,
  l'instance : vise une classe et ça a le curseur Une activité, ça
  s'écrit ou ça se donwload puis un prof l'instancie sur une classe,
  ce qui lance l'activité si elle est en une seule phase ou bien ça
  lance la phase 1 sinon.
  
    DR: Toutes les ressources ont deux états, un état programme et un état exécutable.
    Pour les constantes pas de problèmes. 
    Pour les éléments variables comme le nom du prof il faut une instance spécifique,
    il nous faut donc des patrons/template de classe.
    On instancie le tempplate en fournissant les élèments variables, dans le cas d'un reoudblement le prof doit pouvoir récupérer une partie importante des informations de l'an dernier.
    
    Si l'on veux que le prof puisse thésoriser sur ces cours précédent, si l'on veux pouvoir faire des analytics il faut aussi pouvoir garder le lien (tout en faisant attention à l'anonymoisation ).
    
  

* Analogie avec le théâtre :

    L'analogie avec le théâtre est que c'est tout pariel mais en général on n'a pas le texte de la piece...
    
    Cours  <--> texte authentique de la pièce de théâtre
    classe <--> la troupe 
    un prof  <--> un metteur en scène
    des élèves <--> des acteurs
    des activités <--> des scènes avec des décorts éventuellement différents (activités différentes)


