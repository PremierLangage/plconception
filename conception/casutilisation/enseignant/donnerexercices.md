# Donner exercices

Objectif : Permettre à un enseignant de donner une feuille d'exercice/défis à un étudiant ou à une classe qui suit son cours.

Résumé général : Lorsque l'enseignant clique sur une classe ou un élève, il y a un bouton "Donner feuilles", ce qui lui permet de donner une feuille d'exercice, il a ensuite le choix entre créer une nouvelle feuille ou d'en chercher une qui existe déjà, une fois la ou les feuilles trouvées, l'enseignant valide et cette feuille se retrouvera dans les notifications de chaque élève sélectionné.

# Données

Acteur Principal : Enseignant

Acteurs secondaires : Admin

Concurrence : Oui

Déclencheur : Se déclenche lorsqu'un enseignant clique sur une classe qui suit son cours, un étudiant ou encore un groupe, il peut cliquer sur "Donner une feuille d'exercice".


## Pré-conditions

### Données d'entrées :

	La feuille d'exercice à donner.

	Le nom de la classe/de l'élève/du groupe.

Avoir un compte enseignant dans la base de données.

## Post Conditions

En cas de succès : Les étudiants reçoivent la feuille d'exercice dans leurs centres de notificaton.

En cas d'échec : Les étudiants ne reçoivent rien.

# Navigation / IHM 

L'enseignant lance une recherche pour trouver l'étudiant/la classe/le groupe à qui il veut envoyer la feuille d'exercice.

Une fois trouvé il peut soit crée une nouvelle feuille d'exercice, soit en sélectionner une qui existe déja.



## Scénarios

MAIN SUCCESS SCENARIO

S	[L'enseignant donne une feuille d'exercice à un étudiant ou à l'une des classes qui suivent son cours.]

1	[L'enseignant recherche la classe qui suit son cours, ou recherche tout simplement l'étudiant, ou le groupe d'élève à qui il veut envoyer la feuille d'exercice]

2	[On affiche la liste des feuilles d'exercices qu'il peut donner et on lui propose d'en crée une.]

3	[L'enseignant choisit la feuille d'exercice qu'il veut donner et valide.]

4	[L'étudiant, la classe ou le groupe vont recevoir la feuille d'exercice dans leur [centre de notification](../../concept/centredenotification.md)]

5    Ce cas d'utilisation se finit lorsque l'enseignant change de page internet.


RELATED INFORMATION

Include Use Cases	[Accès feuille/exercice](../etudiant/accesfeuilleexercice.md) [Centre de notification](../../concept/centredenotification.md) [Salon](../../concept/salon.md)  [Classe](../../concept/classe.md).



<!--- 
Author : Jordan
Validator : Raphael
-->
