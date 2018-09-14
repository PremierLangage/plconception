

TODO : relire et classer ce fichier

# Enseignement assisté par ordinateur - Scénario de gestion de travaux pratiques
Objectif

L’objectif de ce scénario est de proposer, pour un coût en encadrement raisonnable, la mise en place d’un suivi en continu des travaux des étudiants dans le cadre de travaux pratiques de programmation.
Description générale

Nous proposons une amélioration du fonctionnement habituel d’un groupe de travaux pratiques (TP) dans un module de programmation, par exemple dans le contexte d’un cours de découverte de la programmation au premier semestre de première année d’études supérieures.

Les caractéristiques marquantes de ce type d’enseignement sont les suivantes :

    élèves de niveaux très hétérogènes,
    effectif potentiellement important (100, 200…),
    équipement informatique personnel des élèves hétérogène.

Ces caractéristiques ont un certain nombre de conséquences sur les possibilités de suivi du travail des élèves. Tout d’abord, le travail autonome à la maison est compliqué par la maîtrise encore faible des outils de développement (installation des logiciels, hétérogénéité des équipements personnels). L’effectif potentiellement important et la cherté du personnel enseignant introduisent une difficulté d’évaluation continue (trop nombreux travaux à corriger pour une évaluation hebdomadaire rigoureuse des productions d’élèves, rythmes de progression inégaux).
Solution minimale

Le scénario que nous proposons requiert, a minima, la mise en place d’un système d’évaluation automatique de productions d’élèves prenant principalement la forme de programmes ou d’extraits de programmes (fonctions isolées par exemple), ainsi que d’un mécanisme permettant leur transmission et leur archivage. Le fonctionnement envisagé est un travail des élèves sur les exercices proposés par l’enseignant, leur validation automatique par le système et l’attribution d’une note indicative ou d’un pourcentage de complétion de chacun des sujets pour chacun des élèves.
Correction automatisée

Si l’on suppose l’existence de sujets de travaux pratiques (prenant traditionnellement la forme de recueils d’exercices de quelques pages sur un thème donné, ou « feuilles de TP »), le principal travail requis de l’équipe enseignante est de donner, pour chaque question de chaque exercice, un programme de référence dont les réponses sur une liste d’entrées donnée (également fournie) seront confrontées à celles de la solution proposée par l’élève.

Ceci offre le bénéfice supplémentaire d’enrichir le matériel pédagogique dont disposent l’ensemble des enseignants intervenant dans le module, en clarifiant les solutions attendues et en imposant leur tenue à jour.
Évaluation

On peut envisager une évaluation de chaque question sur une échelle à quatre degrés, éventuellement assortie d’un code couleur :

    programme bien formé fournissant la bonne réponse (« vert »),
    programme bien formé avec erreur (« orange »),
    réponse invalide, ne compilant pas ou ne fournissant pas de résultat (« rouge »),
    pas de réponse fournie (« noir »).

Suivi de la progression

Au fur et à mesure de l’avancée des étudiants dans la liste d’exercices, l’enseignant a accès à la liste de tous les exercices abordés par chacun des étudiants, et de la qualité de leurs réponses (échelle ci-dessus). En l’absence de tout autre dispositif, ceci laisse déjà envisager :

    de fournir aux étudiants un retour immédiat sur la validité de leurs productions,
    de permettre une avancée des étudiants à leur propre rythme,
    de fournir aux enseignants une base possible pour une note de contrôle continu, reflétant notamment l’assiduité, la rapidité et la compétence de chaque étudiant,
    de permettre la détection d’étudiants décrocheurs (majorité de « noir ») ou en difficulté (majorité de « rouge ») par rapport au reste du groupe,
    de permettre l’identification d’énoncés à améliorer ou de notions mal comprises par le groupe.

Il est évidemment envisageable de limiter l’accès au serveur d’évaluation à un créneau horaire bien défini, dans le cadre d’un examen sur machine par exemple.
Perfectionnements possibles
Détection d’erreurs typiques

Plutôt que de fournir uniquement un programme de référence pour chaque question (ce qui ne permet de fournir que des réponses du type « juste / faux »), il est envisageable que les enseignants préparent un ensemble de programmes présentant des erreurs typiques.

Exemple : dans un exercice demandant d’écrire une fonction calculant le n-ème terme de la suite de Fibonacci, le programme de référence (écrit dans le langage du cours) calcule correctement le n-ème terme de la suite, un programme erroné pourrait calculer le terme de rang n+1 ou n-1 au lieu du terme de rang n, etc.

La solution proposée par l’élève est ainsi confrontée successivement à chacun des programmes (ou listes d’entrées et sorties) fournis par l’enseignant. On peut ainsi envisager de raffiner l’échelon 2 proposé ci-dessus entre programmes avec erreurs typique et avec erreurs non identifiées.

La détection d’erreurs typiques requiert plus de travail préparatoire de la part des enseignants, qui doivent envisager les erreurs possibles des élèves et écrire les solutions erronées correspondantes. Elle permet en revanche de fournir à l’élève des messages informatifs sur la sémantique de leurs programmes, ce qui peut présenter un bénéfice non négligeable.
IDE en ligne

La mise en place d’un environnement de développement intégré en ligne (accessible à l’aide d’un navigateur web), interfacé avec l’environnement numérique de travail des étudiants, offrirait un bénéfice non négligeable :

    accès plus rapide à un environnement de travail fonctionnel,
    simplification des problèmes matériels et logiciels,
    travail en autonomie facilité depuis l’extérieur de l’université,
    interaction facilitée avec le serveur d’évaluation.

Des outils performants (historique des versions, coloration syntaxique, complétion automatique, documentation en ligne, exécution pas à pas, visualisation de l’état de la mémoire, etc.) existent d’ores et déjà sous licences libres pour un certain nombre de langages de programmation.
Statistiques et indicateurs

Côté enseignant, les données recueillies par le serveur d’évaluation laissent envisager la mise en place de nombreuses statistiques et de pages de synthèse :

    page de synthèse personnelle d’un étudiant, avec vue d’ensemble de sa progression, du travail restant à effectuer, comparaison avec l’avancée moyenne du groupe ou de la promotion,
    édition d’histogrammes de complétion des exercices pour l’enseignant,
    mise en place de concours (code le plus rapide, le plus court, etc.),
    détection de plagiat à l’échelle d’une promotion entière ou sur le Web (des outils performants existent à ce jour).

Parcours personnalisé

Le fonctionnement « linéaire » décrit ci-dessus, sur le modèle des sujets de TP traditionnels, peut être enrichi à l’aide du référentiel de notions élaboré dans le cadre du projet. Ainsi, l’environnement de travail pourra proposer à un élève ayant validé avec succès certains exercices-clé de passer directement à une notion suivante, tandis qu’il proposera à un élève ayant eu des difficultés une reformulation des énoncés d’exercices, des exercices complémentaires, etc.
