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

### Versionage des ressources pédagogiques

Chaque ressource pédagogiques (exercice PL, grader, bilbiothèque fonctionnelle...) aura une 
unique version finale (comme un article wikipedia). Le developpement de chaque ressource sera 
ainsi incrémental dans le sens que la manière normale de travailler est de prendre la dernière
version, de l'améliorer et de publier une nouvelle version.

* À la première création d'une ressource, la première publication est automatiquement la version 
  finale.
* Il est possible via la donwgrade, de pacer comme nouvelle version finale, une vieille version.
* L'accès aux vieilles versions est autorisées mais ce n'est pas le point d'entrée naturel.

### Rechercher et ouverture des ressources

Ourvrir une ressource


## Techniquement à l'intérieur

### Le repository git à l'intérieur

Toute action de sauvegarde devra créer un commit dans un git sous-jacent unique.

Normalement, le git caché à l'intérieur devrait avoir pour commit : 

    %$262@356$%63456 : Work of nborie on computer_sciences/programmation/C/functions/
    #$@#5623412!!@24 : Work of dr on computer_sciences/programmation/C/python/dictionnaries
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl
    $@#$@#%^^3432342 : Work of Hugo on computer_sciences/programmation/C++/hanoi.pl
    243523@#$%23^^%# : nthiery publish new version of computer_sciences/programmation/C++/hanoi.pl




