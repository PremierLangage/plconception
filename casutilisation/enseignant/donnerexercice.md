# Donner exercice

Objectif : Permettre à un enseignant de donner un exercice/défis à un étudiant ou a une classe qui suit son cours.

Résumé général : Un enseignant doit donner des exercices à une ou plusieurs classes qui suivent son cours et/ou à un ou plusieurs étudiants (groupes).

Un enseignant peut donner une feuilles d'exercice à une classe que si cette classe suit l'un des cours de l'enseignant.


# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Oui

Déclencheur : Se déclenche lorsqu'un enseignant clique sur une classe qui suit sont cours, un étudiant ou encore un groupe, il peut cliquer sur "Donner une feuille d'exercice".


## Pré-conditions

### Données d'entrées :

	La feuille d'exercice a donner.

	Le nom de la classe/de l'élève/du groupe.

Avoir un compte enseignant dans la base de donnée.

## Post Conditions

En cas de succès : Les étudiants reçoivent la feuille d'exercice dans leurs centre de notificaton.

En cas d'échec : Les étudiants ne reçoivent rien.

# Navigation / IHM 

L'enseignant lance une recherche pour trouver l'étudiant/la classe/le groupe à qui il veut envoyer la feuille d'exercice.

Une fois trouvé il peut soit crée une nouvelle feuille d'exercice, soit en sélectionner une qui existe déja.



## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant donne une feuille d'exercice à un étudiant ou a l'une des classes qui suivent son cours.]

1	[L'enseignant recherche la classe qui suit sont cours, ou recherche tout simplement l'étudiant, ou le groupe d'élève à qui il veut envoyer la feuille d'exercice]

2	[On affiche la liste des feuilles d'exercices qu'il peut donner et on lui propose d'en crée une.]

3	[L'enseignant choisit la feuille d'exercice qu'il veut donner et valide.]

4	[L'étudiant, la classe ou le groupe vont recevoir la feuille d'exercice dans leur [centre de notification](/centredenotification.md)]

5    Ce cas d'utilisation se fini lorsque l'enseignant change de page internet.


RELATED INFORMATION

Include Use Cases	[Accès feuille/exercice](accesfeuilleexercice.md) [Centre de notification](/centredenotification.md) [Groupe](/groupe.md) [classe](/classe/md).



<!--- 
Author : Jordan
Validator :  
-->
