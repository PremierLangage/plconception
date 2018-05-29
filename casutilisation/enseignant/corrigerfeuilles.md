# Corriger des feuilles

Objectif : Permettre à un enseignant de corriger toutes les feuilles d'exercice d'une classe.

Résumé général : Un enseignant après avoir sélectionner un cours et une activité qu'il a choisit d'evaluer (en plus de l'évaluation automatique de pl). Une nouvelle page d'interaction s'ouvre sur le **mode correction** de l'activité. Dans le mode correction l'enseignant peux choisir un élève et voir ses réponses à l'activité. Il peut modifier l'évaluation et ajouter un commentaire sur chaque réponse. Les commentaires et modifications sont pris en compte automatiquement. Le undo est disponible. En fin d'édition l'ensemble des modifications est sauvegardé automatiquement.

FIXME ne doit on pas voir ce cas d'utilisation comme un accès au mode correction d'une activité (stratégie ?).

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur un de ses cours, il a alors la possibilité de voir les "taches" qu'il a donné aux étudiants d'une classe qui suit ce cours.


## Pré-conditions

### Données d'entrées :
	Le cours associé

	La classe

	La tache a corriger

Avoir un compte enseignant dans la base de donnée.

Avoir au moins un cours.

Avoir au moins une classe qui suit ce même cours.

## Post Conditions

En cas de succès : L'enseignant voit toute les "taches" qu'il a demander de faire.

En cas d'échec : L'enseignant ne voit rien.

# Navigation / IHM 

L'enseignant voit une liste des "taches" qu'il a demandé et la classe associé, il peut alors entrer en mode correction et commencer a corriger les feuilles d'exercices.


## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant voit la liste des taches qu'il a donné pour son cours.]

1	[L'enseignant peut ensuite cliquer sur l'une des taches et voit la liste des étudiants et la feuille d'exercice qu'ils ont rendu, il clique sur le bouton "Mode correction", qui lui permet de corriger les feuilles de toute une liste d'étudiant.]

2	[Ce mode est spécial, il permet à l'enseignant de corriger les feuilles exercice par exercice, c'est à dire qu'il voit toutes les reponses à l'exercice 1 avant de passer à l'exercice 2, l'enseignant peut aussi épingler 3(à définir) réponses qui lui plaise, les réponses épinglées sont visible lors de la correction de chaque étudiant. Ce qui permet à l'enseignant de se rappeler des bonnes réponses et/ou des mauvaises.] 

3	[Une fois que l'enseignant a commenté et mis une note à l'exercice 1 de l'étudiant X, on  passe à l'exercice 1 de l'étudiant X+1, l'enseignant choisit par quel exercice il désir commencer la correction, en cliquant sur la liste des exercice disponible sur la gauche de la page.]

4	[Chaque [note et commentaire](.../concept/editeurdechamps.md) est sauvegardé, l'enseignant sait qu'il a déjà corriger tel exercice de tel étudiant, il peut modifier la note et le commentaire qu'il a déjà ecrit]

5	[Une fois que l'enseignant pense avoir fini la correction, il la valide ce qui [notifiera](~/concept/centredenotification.md) les étudiants.]

6   Ce cas d'utilisation se finit lorsque l'enseignant change de page internet, les corrections déjà effectué sont sauvegardé grâce à la [sauvegarde continu](~/concept/zonetampon.md) ou lorsque l'enseignant valide ou abandonne sa correction.


EXTENSION 

Step    Branching Condition

1	 Si il n'y a qu'une seule feuille à corriger. Etape 2

na.  Action causing branching:

1 : Dans ce cas l'enseignant voit les exercices les un apres les autres.

RELATED INFORMATION

Include Use Cases	[Centre de notification](~/concept/centredenotification.md) [Editeur](~/concept/editeurdechamps.md) [Sauvegarde continu](~/concept/zonetampon.md) 



<!--- 
Author : Jordan
Validator : Raphael
-->
