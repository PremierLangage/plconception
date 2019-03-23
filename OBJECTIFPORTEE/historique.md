

Le projet a démarré sur la constatation d'un certain nombre de manques sur les plate-formes d'enseignement qui nous sont proposées.

Après un un travail d'analyse il nous semble que le premier besoin de tout outil de elearning/foad (enseignement à distance/sur ordinateur) c'est que le cours/les supports etc doivent être accessibles sur la plate-forme et donc que notre projet doit consister en une base de « cours » et « d'exercices », des ontologie matérialisant la connexion entre les cours et les exercices. Les cours devant être adaptable pour sa classe et améliorables par tous.
Mais en gardant l'idée que chaque enseignant va pouvoir définir sa propre structure de cours et de tp. Ainsi nous parlerons de deux mots clefs les Resources (ressources partagées) et les Assets (Instanciation privé à une classe cours d'une ressource).

Nous avons besoin d'un outil d'aide à l'enseignement de l'informatique (mais les autres disciplines ne sont pas oubliées), cet outil doit permettre de fournir plus de retour aux élèves avec moins d'intervention de la part de l'équipe enseignante [besoin 1 : exerciseur de programmation, besoin 2 : exerciseur automatique], d'autre part nos publics ont des objectifs hétérogènes que nous pouvons classifier en trois groupes, les passionnés [qui sont intéressés par la matière et prêts à travailler beaucoup], les diplômes [qui ont pour seul objectif de satisfaire aux exigences fondamentales de l'enseignement], les autres [mais pourquoi sont ils là ?]. Nous souhaitons pouvoir adapter nos exercices à ces différents publics [adaptation : besoin 3]. Les premiers cherchent des exercices avec du "challenge", de la compétition, l'absence de répétition, originaux. Les seconds cherche a savoir si ils sont "dans les clous" et donc si ils peuvent passer à autre chose. Les derniers sont parfois récupérables (sans plateforme c'est sans espoir) il faut appliquer deux stratégies en même temps d'une part s'occuper d'eux individuellement de façon à les rendre autonomes sur la plateforme et d'autre part leur donner accès à des enseignements (en général du secondaire) qui leur permettent de se remettre en selle. 

Pour apporter l'adaptation et l'automatisation nous faisons le pari d'utiliser un outil qui choisit automatiquement  l'exercice suivant d'un apprenant en fonction des objectifs définis par le professeur et des exercices déjà fait par l'apprenant et bien entendu: les résultats d'exercice, et toute l'information de son parcours sur la plateforme. Pour calculer les propositions de parcours nous utiliserons des référentiels de concepts (ontologies) [besoin 4] qui permettront de construire les objectifs d'un cours ou d'un TP et de suivre l'élève sur son parcours d’acquisition de ces objectifs.

Une des fonctionnalités attendues du référentiel est de permettre de voir l'avancement de l’acquisition de connaissances et ce aussi bien pour l'apprenant que pour le chargé de cours ou le chargé de TP. Ainsi nous attendons d'avoir une interface pour l'apprenant [besoin 5.1] qui lui permette d'avoir une idée de sa progression. D'une interface pour les enseignants [besoin 5.2] permettant d'avoir une idée de la progression d'un élève, d'un groupe ou d'une classe, de l'acquisition d'un concept .

Enfin le projet se veut expérimental et donc nous souhaitons pouvoir analyser la mise en œuvre de ces cours et TP par la plate-forme. Pour cela nous avons besoin de sauvegarder l'ensemble des interactions entre les apprenants et la plate-forme [besoin 6]. Un module de statistiques complémentaire doit permettre d'extraire toutes les informations pertinantes de ces parcours.

Pour l'éventuelle transformation en MOOC, il faut pouvoir ajouter des feedbacks à un exercice a posteriori, l'idée est de pouvoir répondre à un élève qui a mal répondu à un exercice et que cette réponse soit enregistré si l'on rencontre la même erreur. De la même façon ceci peut être un indice « hint » qui est fournis dans le cas d'un exercice ou les élèves bloquent [besoin 7].

Les exerciseurs de programmation peuvent être complétés par un ensemble de types d’exercices [qui existent déjà mais doivent être adaptés] [besoin 8] gift, AMC, SCORM, etc

Le partage des ressources [besoin 9] est une tache complexe il faut proposer une éditorialisation qui permette de faire rencontrer différents acteurs : des développeurs d'exercices aléatoires et constructifs (complexes à écrire), les enseignants (qui connaissent le besoin direct de leurs élèves: ne savent pas faire une règle de 3), les didacticiens (l'ordre d'apprentissage, le niveau de feedback, la forme des exercices, le travail sur la métacognition), les chercheurs (nouvelles formes de suivi, d'activités, indicateurs, etc). Cette éditorialisation permettre de faire apparaitre des versions validées et qualifiées des ressources par améliorations successives.


Les indicateurs [besoin 10] forment une classe de besoin à part entière, il nous faut des indicateurs très variés et très différents en fonction des utilisateurs.

Les ressources doivent êttre permanenttes, disponibles, acessibles, dévouvrables (recencement) et ouvertes à la réutilisatinn et l'extension. [besoin 11].


Les exigences suivantes sont plus ponctuelles et à intégrer aux endroits appropriés.

* [activity] Un outil de validation de forme pour les projets de programmation.

* L'interface de « programmation » des cours et des exercices doit être simple.

* Il faut différentes formes d'exercices (la plateforme ne doit pas être barbante)

* [exoprog] Fussy output (ce que les débutants ont du mal a voir: les blancs les passages à la ligne les textes inutiles (la valeur est : val)). Si l’appréciation est fussy elle détecte ces écarts à la norme et les signales.

* outil de détection de plagiat pour les projets et les exercices (réponses trop rapides...).

* [tag] l'étiquetage des exercice sur l'ontologie permet à un apprenant de revenir sur une notion/concept d'une part en demandant un exercice supplémentaire ou en accédant à un module de cours correspondant.

* Il faut que les sujets de TP prennent en compte notre souhait d'avoir des variations de comportement en fonction des élèves.



### besoins/solutions

besoin 1 : exerciseur de programmation, beson initial du projet, nécessite une sécurisation de l'évaluation du travail des étudiant.  
Solution: Une sandbox externalisée utilisant une technique de  Jail et le gestionnaire de containeur DOCKER pour sécuriser les évaluations.

besoin 2 : exerciseur automatique. 
Solution : un langage de programmation des exercices permettant de modifier l'exercice a partir d'un aléa, de faire varier la difficulté grâce à un paramètre, de faire varier les feedback "retours", cela sans rendre la création d'exercices plus difficile, permettre de créer de nouveaux types d'exercices facilement.  

besoin 3:adaptation  
Solution: Chaque apprenant est traité de façon distincte sur la plateforme, c'est le mélange des activité et de la connaissance de l'apprenant qui permet une adpatation constante du parcourt.
L'apprenant choisissant le mode d'accès qu'il souhaite aux exercices avec un mode : chalenge, apprentissage, révision, entrainement. La plateforme proposant alors un exercice conforme à la demande. Bien entendu ce n'est pas le seul mode, l'enseignant pouvant définir un parcourt strict. 

besoin 4: outil de mesure de la connaissance d'un apprenant (d'un groupe). 
Solution : Utiliser des ontologies, bien documenté dans la littérature scientifique ce model convient bien.

besoin 5: Des interfaces éfficasses car graphiques. 
Solution : Permettre que les utilisateurs fassent le choix des indicateurs qu'ils souhaitent voir sur leur progression (resp. la progression du groupe pour les enseignants). Parmi ces indicateurs, la vue de l'ontologie est un indicateur important.

besoin 6: Conservation des parcourts avec [Anonymisation](https://fr.wikipedia.org/wiki/Anonymisation)
Solution: Utilisation de deux modes de sauvegarde, un version interne et une version anonymisée utilisant l'interface xAPI de sauvegarde de parcours.

beson 7:  ajouter des feedbacks a un exercice a posteriori. 
Solution: Les décorateurs la posibilité d'ajouter des décorateurs sur les exercices qui vont changer de façon générique leur comportement, cette solution élégante dans son principe n'est pas encore validé par un POC.

besoin 8: Compatibilité avec différents format d'exercices en particulier WIMS, exo7 gift, AMC, SCORM, etc. 
Solution: de nouveau la solution passe par un langage de programmation des exerices, 

besoin 9: Partage multi-auteur de l'edition des ressources.  
Solution: Pas de solution imédiate il nous faut trouver un compromis en la simpicité et le partage, 
nous avons lancer un projet parrallèle pour nous donner une solution c'est le projet [WIMS-Edition](wimdsed.besoin.md). 


besoin 10 : Les indicateurs  forment une classe de besoin à part entière, il nous faut des indicateurs très variés et très différents en fonction des utilisateurs.  
Solution: Un système de plugins, de widgets et de procedures qui permettent de construire directement sur la plateforme l'indicateur que l'on souhaite, la librairie graphique qui le permet n'est pas encore choisie.

 besoin 11: ressources permanenttes, disponibles, acessibles, dévouvrables.  
 Solution: un serveur unique de ressources. Des serveur d'assets par entités de formation.



**historique** D Revuz 
