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
    V1 : correction et formualtion d'une question par un autre enseignant
    V2 : l'auteur original change le builder et rajoute de l'aléatoire
    V3 : Un troisième auteur rend l'exercice multi-langue
    V4 : Correction orthographique allemande d'un enseignant Allemand
    ...

On peut imaginer que le saut de V1 à la V2 n'a pas été fait en seule séance de travail car l'auteur
à du débuguer son nouveau builder durant une semaine. Les tentatives de travail de cet enseignant
sont sauvegardée à chaque fois mais n'entre pas dans le versionnage pédagogique. On verra plus tard
que toutes les mini-modifications de cet auteurs ont toutefois déclanchés des commit git en interne.


### Rechercher et ouverture des ressources

Ourvrir une ressource 

### Ouvrir une vieille version

Lors de l'ouverture d'une ressource, il est possible de 


### Modification de la version courrante


### Publication d'une nouvelle version


### Conflits de fusion



## Techniquement à l'intérieur

### Le repository git à l'intérieur

Toute action de sauvegarde devra créer un commit dans un git sous-jacent unique.

Normalement, le git caché à l'intérieur devrait avoir pour commit : 

    %$262@356$%63456 : Work of nborie on computer_sciences/programmation/C/functions/
    #$@#5623412!!@24 : Work of dr on computer_sciences/programmation/C/python/dictionnaries
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl
    $@#$@#%^^3432342 : Work of Hugo on computer_sciences/programmation/C++/hanoi.pl
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl




