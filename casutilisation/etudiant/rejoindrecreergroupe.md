# Créer ou rejoindre un groupe


Objectif : Permet à un étudiant de créer ou rejoindre un groupe.

Résumé général : S'effectue lorsqu'un étudiant veut creer ou rejoindre un groupe dans le cas où un enseignant demande de constituer des groupes.


# Données :

Acteur Principal : Etudiant

Acteur secondaire : Admin

Concurrence : Non

Déclencheur : Se déclenche lorsqu'un étudiant veut creer ou rejoindre un groupe.



## Pré-conditions :

### Données d'entrées :

	Avoir un compte étudiant dans la base de données

	L'étudiant doit avoir au moins une matière où un enseignant leurs demande de faire un groupe


## Post Conditions :

### Données sortie :

	groupe crée ou rejoint

Un étudiant peut créer ou rejoindre un groupe dans le cas où un enseignant demande de créer des groupes dans une matière (pour un projet par exemple). Il peut soit créer un nouveau groupe soit rejoindre un groupe déjà existant en parcourant la liste des groupes existants. TODO Si l'étudiant veut rejoindre un groupe il doit faire une demande que le créateur du groupe peut accepté ou refusé.

En cas de succès : L'étudiant a créer/rejoint un groupe

En cas d'échec : L'étudiant n'a pas pu créer/rejoindre un groupe, par exemple si l'étudiant n'a aucune matière où il doit faire partit d'un groupe il n'aura pas la possibilité d'en créer/rejoindre un.


# Navigation / IHM  :

Principe de navigation du scénario principal, organisation de l'IHM.

En cliquant sur le bouton groupe sur son tableau de bord, l'étudiant peut voir la liste des matières où il doit créer ou rejoindre un groupe. Après avoir choisi la matière, il peut faire une recherche des groupes existants et faire une demande pour en rejoindre un(en cliquant sur le bouton à côté du nom du groupe) ou créer un nouveau groupe. 
Si l'étudiant a déjà créer un groupe il le voit en haut de page et il peut inviter des étudiants à rejoindre son groupe en faisant une recherche sur les étudiants qui suivent le même cours(seul le créateur du groupe peut inviter).


##Scénarios :

# MAIN SUCCESS SCENARIO

Step    Action

S    L'étudiant veut créer ou rejoindre un groupe.

1    Ce cas d'utilisation commence quand l'étudiant veut créer un groupe.

2    L'étudiant a la possibilité de créer un groupe dans une matière où un enseignant lui a demandé d'en faire un.

3    L'étudiant crée un groupe et peut inviter d'autres étudiants à le rejoindre.


EXTENSION SCENARIOS

Step    Branching Condition

1	 Lorsque l'étudiant veut rejoindre un groupe. Etape 1

na.  Action causing branching:

1 : L'étudiant peut rejoindre un groupe déjà existant, il peut faire une recherche du groupe qu'il veut rejoindre et faire une demande que le créateur du groupe peut accepté ou refusé.

 

<!--- 
Author : Raphael
Validator :
-->

