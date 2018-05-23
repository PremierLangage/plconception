# Corriger une feuille

Objectif : Permettre à un enseignant de corriger une feuille d'exercice.

Résumé général : Un enseignant doit pouvoir corriger une feuille d'exercice, qu'il a donné.


# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un enseignant clique sur un de ses cours, il a alors la possibilité de voir les "tache" qu'il a donné aux étudiants d'une classe qui suit ce cours.


## Pré-conditions

### Données d'entrées :
	Le cours associé

Avoir un compte enseignant dans la base de donnée.

Avoir au moins un cours.

Avoir au moins une classe qui suit ce même cours.

## Post Conditions

En cas de succès : L'enseignant voit toute les "taches" qu'il a demander de faire.

En cas d'échec : L'enseignant ne voit rien.

# Navigation / IHM 

L'enseignant voit une liste des "taches" qu'il a demandé et la classe associé.



## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant vois la liste des taches qu'il a donné a chacune des classes qui suivent son cours.]

1	[L'enseignant peut ensuite cliquer sur l'une des taches et voit la liste des étudiants et la feuille d'exercice qu'ils ont rendu]

2	[il peut cliquer sur l'une des feuilles et la voir en detail]

3	[Une fois que l'enseignant a cliqué, il voit ce qu'a fais l'étudiant ainsi que l'énoncer et il peut associer a la feuille une note]

4	[Cette note seras [notifié](/centredenotification.md) à l'étudiant.]

5   Ce cas d'utilisation se fini lorsque l'enseignant change de page internet.


RELATED INFORMATION

Include Use Cases	[Centre de notification](/centredenotification.md)



<!--- 
Author : Jordan
Validator :  
-->
