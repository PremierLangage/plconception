
# Qui ? Quoi ? Où ? Quand ? Comment ? Combien ? Pourquoi ?

## Qui ?

Une équipe locale au sein de l'université de Marne la vallée.  
Objectif de l'équipe fournir un exerciseur compatible LTI et différents outils d'enseignement en ligne.
Soutenue par la présidence, le CRI et le CN.

Une vision globale, de nombreux contacts et partenartiats avec des enseignants et des chercheurs et d'autres communautés (WIMS, IREM, Euler, ...)

### Une équipe en construction 
Aucunes des personnes indiquées n'est a 100 % sur le projet ayant toutes un emploi qui n'est pas directement lié au projet. 

- MOA 
  - Dominique Revuz : enseignant en informatique MOA 
  - Magdalena Kobylansky : enseignant en Mathématiques (UPEM)
  - Mourad Ben Hadj &  Xavier Lachapelle: responsables service informatique
- Développeurs Plateforme
  - A Coumes (apprenti) (UPEM)
  - C Calle  (apprenti)(UPEM)
  - M Cisse  (apprenti)(UPEM)
  - Nicolas Salegéro (ingenieur)(CRI UPEM)
- Développement des ressources : 
  - Nicolas Borie : enseignant en informatique (UPEM)
  - David Doyen : enseignant en Mathématiques (UPEM)
  - Nicolas M. Thiéry  : enseignant en informatique  (PSUD)
  - Etienne Sandier  : enseignant en Mathématiques (UPEC)
- Administration Système :
  - Nicolas Cuvelier (ingenieur)(CRI UPEM)

###  Les manques 
Les personnes suivantes sont présenties pour participer au projet 
- Coordinateur projet:
  - Francis Bock
- Coordinateur Migration pédagogique:
  - Sébastien Terssou
- Coordinateur Communication 
  - (une personne de la D.school)
- Administration du projet:
  - (un personne au CN)
- Développeur principal:
  - q coumes à ce rôle mais un élément sénior serait le bienvenu 
- Testeurs:
  - X

## Pourquoi ?
Pourquoi ce projet, trop d'élèves pas assez de professeurs, des élèves hétérogènes 

### Le contexte économique et politique. 

L'enseignement supérieur souffre d'un manque de moyen depuis plusieurs années. C'est particulièrement vrai pour notre université (dans le fin fond du classement en termes de moyens) malgré cela nous avons un taux de réussite en L1 dans le haut du classement. Ce manque de moyen a conduit a des situations de sous effectifs dont notre université soufre particulièrement. Ces problème de moyens se sont accrus avec l'augmentation des cohortes des années 2000 qui entre aujourd'hui dans les universités. 

La structure de l'enseignement supérieur avec l'université qui a la responsabilité de proposer une formation à tout les sortants du baccalauréat. 

L'ensemble de ces éléments créer une situation qui nous a poussé à trouver des solutions informatiques aux problèmes de nos enseignants. 

### Un besoin criant d'aide

- Des étudiants nombreux.
- Des niveaux hétérogènes.
- Des cultures variées.
- Des enseignants concernés mais débordés (risques psycosociaux, burnout, dépression, turnover, mécontentement, démission) .

### Des étudiants capables

L'expérience des presque 30 ans de l'université de Marne la Vallée, nous apporte confirmation que l'on peut obtenir des diplômés de qualité avec les jeunes de l'Est parisien. Seule règle a prendre en compte (mais inaplicables) les etudiants ont des retards qu'ils doivent rattraper pour cela il faut plus de temps et d'accompagnement mais ...  


Mais pour cela il faut pouvoir investir dans un suivi personnalisé des étudiants ce que nos ressources en personnel ne permettent plus. Les statistiques de réussite sont directement proportionelles au taux d'encadrement 


## Quoi ?

Le projet consiste a proposer une plateforme web interactive permettant aux enseignants de proposer des ressources padagogiques (exercices auto-corrigés et autres) à leurs etudiants et permettant à une communauté d'enseigants de construire de façon ouverte et partagée des ressources. 

La plate-forme permettra la mise en oeuvre de nouvelles modalités pédagogiques, notamment le tutorat, l'adpatation, asynchrone, travaux de groupes, dépistages précoces, remédiations (diagnostiques et parcours individualisés)...

Pourquoi une plateforme :  il en existe déjà de nombreuses moodle, canvas, talentLMS, Claroline, etc ...
D'un avis général de nos collègues les LMS sont fort utiles mais ils ne répondent pas entièrement a nos attentes c'est puorquoi nous proposons d'utiliser le protocol LTI Learning Tools Interoperability. [LTI Wikipedia](https://en.wikipedia.org/wiki/Learning_Tools_Interoperability), et créer ce qui est appeler un LTI Tool Provider, c'est à dire un fournisseur d'outil LTI qui nous apportera des réponses au besoins spécifiques que nous avons identifié et qui ne sont pas fournis par les LTI actuels.

[historique](historique.md) 

 

## Où  ?

Nous proposons à l'UPEM un service national de gestion de ressources utilisables pour l'édition de ressources. Chaque institution est responsable de la mise en place de serveurs locaux pour la gestion des actifs . Rappelons que nous entendons par ressource tout élément réutilisable,  et par actif : la ressource dans le contexte de la classe (avec des élèves et des données).


Ainsi chaque unviersité ou académie sera maître du déploiement des environement d'utilisation. Et la monté en charge se fera graduellement et de façon horizontale.

## Quand   ?

Le projet est commencé depuis 1 ans. Nous pensons fournir chaque semestre une nouvelle version du logiciel apportant des fonctionnalités supplémentaires et fournir des corrections de Bug. Les deux version annuelles sont prévues en Juin et Janvier. 


## Comment   ?

Un serveur django sur des serveurs de l'université. Des serveurs django dans les autres établissements. 


      C	Comment ?	De quelle façon, dans quelles conditions, par quel procédé…	Procédure, technique, action, moyens matériel…
      C	Combien ?	Dans quelle mesure, valeurs en cause, à quelle dose…	Quantités, budget…
      P	Pourquoi ?	Cause, facteur déclenchant	Justification par les causes qui ont amené à… (la « raison » d'être, la croyance)
      P	Pour (faire) quoi ?	Motif, finalité, objectif	Justification par le souhait, l'ambition, la prévision…







# 	Pourquoi ?
##  Le suivi personnalisé

Les étudiants qui arrivent en L1 (première année) sont perdus, en général ils quittent le girond familial, sont confrontés à des groupes de grandes tailles où ils ne connaissent personne. Du fait de la grande proportion d'échec en premier année les enseignants ne peuvent légitimement pas investire dans tous les élèves. 
Cela pénalise les plus précaires et tous ceux (et celles) qui ont besoin d'une aide ponctuelle pour mettre le pied à l'étrier.

Réaliser ce suivi de façon partiellement automatique. Une plateforme d'exercice en ligne.


# Les conditions de la réussite

Pour que la platforme d'enseignement en ligne soit une réussité il faut réunir les ingrédiants suivants.

- Disponibilité continue sur internet (il faut que l'université propose des postes d'accès libre à internet en quantité suffisante).
- Disponibilité sur mobile (les étudiants ont plus souvant un téléphone moderne qu'un ordinateur).
- Ensemble cohérents de ressources sommatives et formatives (alignement pédogagique)
- Disponibilité sur le long terme pérénité des ressources.
- Visibilité (faciliter la découverte de la ressource par un apprenant)
- L'efficacité pédagogique et le traitement cognitif et pédagogique
- La qualité (complétude et autonomie)
- Son Evolutivité (Autoévaluation, amélioration continue).
- Validation


# Valeurs

Valeurs de la plate-forme 
- Premier pilier : pl (la plateforme) est une plateforme d’aide à l’enseignement qui incorpore des ressources et des logiciels pour utiliser ces ressources.
- Second pilier : l’objectif est de réunir  dans une structure unique pour chaque enseignement les meilleures ressources.
- Troisième pilier : PL  est publiée sous licence libre et autorise chacun à utiliser, éditer et distribuer ses contenus : puisque tous les éditeurs publient leur travail sous une licence Creative Commons, personne n’a le contrôle d’un article en particulier ; ainsi, tout texte apporté à Wikipédia peut être modifié et redistribué sans avertissement par n’importe qui. Le droit d’auteur doit être respecté, et il est interdit de plagier. 
- Quatrième pilier : Du fait de la nature programmable des exercice et des. Activités un processus de partage et de validation 
Est mise en place ainsi que  des règles de savoir-vivre : vous êtes tenus de respecter les autres développeurs en utilisant les procédure de demande de mise à jours (PULL request), 
- Cinquième pilier : PL suit des règles de savoir-vivre même lorsqu’il y a désaccord. Ne vous livrez pas à des agressions contre des personnes, ni à des généralisations insultantes. Gardez votre sang-froid lorsque l’atmosphère chauffe. Évitez les guerres d’édition. [...] Agissez de bonne foi et partez du principe que vos interlocuteurs font de même, sauf preuve flagrante du contraire. Efforcez-vous d'être ouvert, accueillant et amical. 
- Sixième pilier : PL a des règles et des lignes directrices, elles ont pour objectifs de rapprocher les enseignants d’une même matière sans entraver leur liberté d’enseigner à leur convenance, de structurer le partage pour converger vers des ressources idéales mais elles ne sont pas gravées dans le marbre ; leur contenu et leur interprétation peuvent être amenés à évoluer. Leurs principes et leur esprit importent davantage que leur application à la lettre, et il arrive que l'amélioration de PL nécessite quelques exceptions. Soyez audacieux sans être imprudents lorsque vous mettez à jour des ressources, et n'ayez pas peur de commettre des erreurs. Toutes les versions précédentes des ressources sont conservées et accessibles par le biais de l’historique, il est donc impossible d’endommager ou perdre irrémédiablement de l’information sur PL, part  contre tout les éléments logiciels sont fragiles et à ce titre doivent être traités avec des procédures adaptées (voir les règles logicielles).

