
# Présentation 

Document de travail de présentation des différents projets en cours.

## Introduction & Objective

L’objectif de ce document est de définir la stratégique  générale d’organisation des différents projets en cours : WIMS-édition, WIMS-évolution, PL, NCU-OuiSI.

Pour chacun de ces projets de définir une feuille de route et ainsi que les éléments de calendrier que nous possédons a ce jour.

## La stratégie générale 

La stratégie générale se place dans notre volonté d’obtenir à terme une plateforme d’enseignement moderne avec un grande communauté d’usage permettant d’améliorer l’enseignement des mathématiques et de toutes les disciplines où l’on a besoin d’acquérir des connaissances, des savoirs faire, et des techniques calculatoires.

La plateforme doit pouvoir permettre aux enseignants de proposer des supports de cours dynamiques et individualisés d’une façon simple et évolutive. Permettre au étudiants d’apprendre d’une façon simple (accessible), efficace (rapide), solide (pérenne). Permettre aux chercheurs/ didactitiens de pouvoir profiter du flux de données produit. 

## Le projet WIMS-Evolution 

Le projet Wims Evolution  est un projet sur initiative dont les objectifs sont de deux formes, d’une part des audits pour nous donner des informations sur l’état du logiciel et de la communauté qui permettrons a celle-ci de prendre des décisions.

D’autre part la construction de deux modules autour de WIMS, LTI et le Search and compose.

### Audit technique de la plateforme WIMS

L’audit technique de la plateforme a pour objectifs 

Ecrire un document faisant une description de la platform WIMS en terme d’architecture informatique (voir plus bas).

Deuxième élément attendu une évaluation du cout de réécriture, du coût d’encapsulation dans une autre plateforme, des capacités d’évolution du logiciel. 

Troisième élément  recenser les équipes de développement capable de participer à) l’évolution du logiciel. 

#### Architecture logiciel :

-  Organisation en composant 
    -  Processus 
    -  Fichiers 

-  Outils externe utilisés
    -  Intégrés  
        - librairies mathématiques par exemple

    -  Externes 
        - Logiciel d’affichage d’image de molécules 

-  Langage de programmation 
    -  Y a t’il des langage internes 

-  Structuration en plugin 
    -  Quelles sont les capacités d’intégration de nouveaux composant ?

-  API exportées 

### Audit des usages 

Pour l’audit des usages nous allons faire un sondage sur l’ensemble de la communauté WIMS. Nous allons en particulier cibler des responsables de formations et des responsable d’enseignements.

Nous attendons des réponses à différentes questions avec l’audit des usages:

- WIMS est utile ! ( et oui ;)
- Les exercices efficaces sont de quel forme ? 
- Que les apprenant reproche à WIMS 
- Que les apprenant apprécie avec WIMS 

- etc 

Nous allons faire ce sondage en deux parties: construction du questionnaire avec des interlocuteurs privilégiés, puis une fois le questionnaire approfondi un sondage plus large sur l’ensemble des utilisateurs de WIMS.

### LTI

Learning Tools Interoperability, est un protocol permettant la communication entre logiciels d’enseignement. WIMS n’est pas LTI et donc nous allons développer un greffon permettant cette communication.

### Search & compose 

La création de feuille d’exercices sous WIMS est un exercice difficile et ingrat qui pénalise l’usage général du logiciel.  Le module Search & compose à pour objectif de simplifier cette activité. 

## Le projet WIMS-EDITION 

Le projet WIMS édition s’attaque au deux sens de termes « édition » d’une part l’édition scientifique avec les mécanismes de validation par les pairs de contrôle de qualité et de partage des productions.

Et d’autre part l’aspect plus prosaïque de l’édition informatique de ressources pédagogique  utilisable sur une platform comme WIMS.

## Le projet PL 

Le projet PL 

### Atouts 

Les atouts de la plateforme sont les caractéristiques suivantes:

- outils de développement modernes: BD, LTI, python3 (mais pas que), django , docker, etc
- Un mécanisme d’exercices aléatoires qui permettent d’éviter le plagiat 
- Des interface graphiques intuitives permettant d’écrire de nombreux types d’exercices de type classiques: QCM, sélection, vrai-faux, drag and drop, pointage, positionnement sur une carte, association, mots croisés, etc
- Un langage de programmation d’exercice complet permettant de proposer aux enseignant les plus exigeant de construire des types d’exercices totalement spécifiques à leur enseignement en profitant de composant élémentaires puissants. 
- sécurisation des transactions et sandboxing du code
