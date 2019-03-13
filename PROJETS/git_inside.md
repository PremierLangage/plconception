# Projet Git Inside

* Ce projet pourra être subdivisé en plusieurs lots.
* Cette page à vocation à présenter un cahier des charges fonctionnels et techniques 
  pour réaliser la partie technique du partage des ressources pédagogiques.
* Ce projet correspond au design technique de la résolution du ticket :
  https://github.com/PremierLangage/premierlangage/issues/204

## Objectifs globaux du projet

* Centraliser les contributions dans un endroit commun pour favoriser les mutualisations, 
  échanges et les collaborations de manière générale.
* Cacher les détails techniques de sauvegarde et de pérénisation des productions pédagogiques.
* Permmettre une grande flexibilité pour l'utilisateur (ici les enseignants éditeurs) dans les 
  choix de versions.
* Monter en qualité via la mise en place de version de référence pour chaque ressource 
  (à la Wikipédia).

## Decription des fonctionalités utilisateurs

### Versionnage des ressources pédagogiques

Chaque ressource pédagogiques (exercice PL, grader, bilbiothèque fonctionnelle...) aura une 
unique version finale (comme un article wikipedia). Le developpement de chaque ressource sera 
ainsi incrémental dans le sens que la manière normale de travailler est de prendre la dernière
version, de l'améliorer et de publier une nouvelle version.

* À la première création d'une ressource, la première publication est automatiquement la version 
  finale.
* Il est possible via la donwgrade, de pacer comme nouvelle version finale, une vieille version.
* L'accès aux vieilles versions est autorisées mais ce n'est pas le point d'entrée naturel.

Une version d'une ressources pédagogiques n'est pas une version aux sens techniques des utilitaires
informatiques de gestion de version (git, mercurial, subversion, ...). Ici, on enttends par version
un état d'une ressource pédagogique tel qu'à un certain instant, un enseignant éditeur a considéré 
cette ressource comme finale.

Les versions des ressources pédagogiques PL sont donc des versions au sens pédagogiques.

    V0 : premier jet d'un enseignant qui publie son exo car il a fini de travailler dessus
    V1 : correction et reformualtion d'une question de l'énoncé par un autre enseignant
    V2 : l'auteur original change le builder et rajoute de l'aléatoire
    V3 : Un troisième auteur rend l'exercice multi-langue
    V4 : Correction orthographique allemande d'un enseignant Allemand
    ...

On peut imaginer que le saut de V1 à la V2 n'a pas été fait en seule séance de travail car l'auteur
à du débuguer son nouveau builder durant une semaine. Les tentatives de travail de cet enseignant
sont sauvegardée à chaque fois mais n'entre pas dans le versionnage pédagogique. On verra plus tard
que toutes les mini-modifications de cet auteurs ont toutefois déclanchés des commit git en interne.


### Rechercher et ouvrir des ressources

On peut ouvrir une ressource en parcourrant l'arborescence du dépot logique

* QUEL EST L'UNITÉ POUR LA RESSOURCE ?
* PEUT-ON DIRE TOUT FICHIER DU DÉPÔT CONCEPTEXO EST UNE RESSOURCE ?
* UN GRADER EN DEUX FICHIERS CONSTITUE UNE OU DEUX RESSOURCES ?
* QUELQU'UN QUI OUVRE UN FICHIER DE CONCEPTEXO OUVRE QUOI ALORS ?

### Ouvrir une vieille version

Lors de l'ouverture d'une ressource, il est possible d'accèder aux anciennes version publiée. On peut
alors consulter les noms des auteurs successifs ainsi que les dates de sorties des versions. On peut
aussi cliquer sur une ancienne version pour la visualitser. Lors de la visualisation d'une vieille 
version, deux nouvelles options s'ouvre à l'utilisateur :

* Possibilité de faire une downgrade : c'est à dire un boutton qui propose de rendre la vieille version
  comme nouvelle version courrante
  
* Édition de la vieille version : sur le compte personnel de l'utilisateur courrant, cela ouvre la 
  vieille version en mode édition. L'utiliateur peut alors faire des modifications et les sauvegarder
  petit à petit. Il aura la possibilité de publier sa version locale. Cela aura pour effet de donwgrader
  vers la version d'où il est reparti et aussi d'empiler les modifications locales qu'il a opéré.

### Modification de la version courrante

Losqu'un utilisateur à ouvert une version finale (ASK - elastic search ou parcours dans l'arborescence) 
ou lorsqu'il a décidé manuellement d'ouvrir manuellement une ancienne version. Un utilisateur peut apporter
des modifications (que l'on appelera modifications locales tant qu'elles ne sont pas publiée). Ces 
modifications seront sauvegardé uniquement pour lui. Chaque utilisateur peut donc possiblement avoir 
une version courrante de travail de chaque ressource présente dans la base.

Seulement deux actions sont possibles à partir d'une version courrante modifiée d'une ressource :

* La publication : l'enseignant utilisateur a fini et considère son trvail comme final.

* L'abandon : l'enseignant ne veut pas publier... Les cas standards de cet utilisation correspondent à :
    - Une nouvelle version à été publiée depuis le travail de l'auteur et l'auteur ne veut pas écraser 
      la nouvelle version finale dont il n'a pas connaissance.
    - L'auteur renonce à finaliser son travail (manque de temps, pas envie de partager, etc...).


### Publication d'une nouvelle version

Une version courrante est un état d'une ressource pédagogique ouverte dans l'éditeur, ça peut être :
* La version finale (non publiable car déjà fait...)
* La version finale + modifications locales
* Une version ancienne
* Une version ancienne + modifications locales
Les trois derniers sont des versions courrantes publiables. Publier ces versions aura pour conséquence 
de ramplacer la version finale de la ressource consernée. Chacune de ces publications portent un nom 
particulier :
* La version finale + modifications locales --> Publication d'amélioration
* Une version ancienne --> Donwgrade de la ressource
* Une version ancienne + modifications locales --> Amélioration rebasée


### Conflits de fusion

Les conflits ne seront pas possible car il seront INTERDIT !

* Wikipedia et Github qui encapsule un gestionnaire de versions bas-niveau interdisent les fusions.
* Wikipedia : Impossibilité de sauvegarder les modifs s'il y a une modification faite entre temps.
* Github en session graphique : Défait le premier commit lors du second commit s'il se chevauchent

De manière générale, quand on encapsule totalement un système de gestion de version 
(git, mercurial, svn, etc...) et que l'on souhaite complètement caché sa présence à l'utilisateur,
on interdit les MERGES et autre FUSIONS. Chaque ressource est associé à un chapelet de patchs et
de versions mais PAS UN GRAPHE AVEC DES DIAMANTS ! 

Pour éviter d'entrer en contact avec le gestionnaire de version interne et technique, les diamants
sont linéarisé avec la fonction de downgrade.

    V0 : Bob premiere version
    V1 : Bob première version + ajout1
    V2 : Alice donwgrade V0 + ajout2
    V3 : Bob + ajout1

Bob et Alice travaillent ensemble sur une même ressource. Bob a l'idée d'y rajouter un *ajout1*, Alice 
souhaite aussi implementé *ajout2* sur le même exo en même temps.

En V0, Bob a fait son premier jet. Bob et Alice travaille maintenant en même temps chacun de leur coté
sur la même ressource. Ils font chacun des petit commit git sous-jacent sans le savoir. Ces petites 
modification locales n'entre pas dans le versionnage pédagogique. Bob finit en premier et sort la V1.
Alice finit en second, elle est averti par le message suivant : UNE NOUVELLE VERSION DE VOTRE RESOURCE
A ÉTÉ PUBLIÉE PAR BOB, SOUHAITEZ-VOUS QUAND MÊME PUBLIÉ VOTRE VERSION BASËE SUR UNE ANCIENNE VERSION 
MAINTENANT ? Alice à confirmé sa publication car elle ne voulait pas géré le conflit de son coté en
sauvegardant sur son disque dur personnel sa version, puis en prenant la nouvelle version de Bob et
en réintégrant depuis la nouvelle version de Bob les nouvelles modifications locales qu'elle avait
produite. De ce fait, Alice à downgradé la version finale. Elle envoie ensuite un mail à Bob qui a
plus l'habitude de PL et qui lui dit : Ne t'en fais pas, je fais prendre ta version et remettre ce que
j'avais rajouté. Je sais comment le récupérer rapidement et puis je l'ai déjà fait...


Ainsi les conflits n'existe pas dans le versionnage pédagogique : TOUTE NOUVELLE PUBLICATION REMPLACE
LES PRÉCÉDENTES ET DEVIENT VERSION FINALE. L'arbitrage est donc communautaire, ressource par ressource.
C'est ce qui est proposé par Wikpedia, github mode graphique, ... Techniquement, cela apparait comme
la manière la plus saine d'encapsuler les systèmes de gestions de version pour en cacher la complexité
aux utilisateurs tout en leur permettant de jouir de leur puissance.


## Techniquement à l'intérieur

### Le repository git à l'intérieur

Toute action de sauvegarde devra créer un commit dans un git sous-jacent unique.

Normalement, le git caché à l'intérieur devrait avoir pour commit : 

    %$262@356$%63456 : Work of nborie on computer_sciences/programmation/C/functions/
    #$@#5623412!!@24 : Work of dr on computer_sciences/programmation/C/python/dictionnaries
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl
    $@#$@#%^^3432342 : Work of Hugo on computer_sciences/programmation/C++/hanoi.pl
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl




