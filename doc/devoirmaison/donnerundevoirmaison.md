# Donner un devoir maison

Pour donner un devoir maison, un enseignant se rends dans son tableau de bord, il clique sur la discipline dans laquelle il veut donner un devoir maison, puis il clique sur "créer".
Un éditeur s'ouvre et l'enseignant doit créer son devoir maison.
Il peut choisir si le devoir se fait en groupe ou pas.
Si le devoir se fait en groupe, il doit choisir la date limite de création des groupes, le nombre d'étudiant par groupe et la manière dont les groupes sont formés.
Les groupes peuvent être formés :

* Aléatoirement, c'est à dire que l'application va mettre automatiquement les étudiants dans des groupes de n.

* Manuellement, c'est à dire que l'enseignant va créer lui même les groupes.

* Par les étudiants, c'est à dire que les étudiants seront chargés de créer les goupes eux même.

Lorsque la date limite de création des groupes est dépassé, un système d'"autofill" est appliqué. Les étudiants qui n'ont pas de groupe complète les groupes imcomplets. Si tous les groupes sont complet et qu'il reste des étudiants sans groupe, un ou plusieurs nouveaux groupes sont créés. Après ça, tant que les groupes ne sont pas au complet, on détruit le dernier groupe incomplet créé et on complète les autres groupes.

## Ex de devoir maison

title=Devoir maison n°1
introduction==

Devoir sur les chaînes de caractère

==
type=dm | type : string
subject==

@ path/string.pl

==
date.group=26/09/1996-00:05 # type : date() | Date limite de création des groupes  
date.deposit= 26/09/1996-00:05 # type : date() | Date à partir de laquelle on peut rendre le devoir  
date.limit=26/10/1996-00:05 # type : date() | Date limite pour rendre le devoir  
overtime=true # type : boolean | Autorisation de rendu avec retard  
deposit.type=unique # type : string | unique si un seul des membre du groupe doit rendre le devoir ou all si tous le membres doivent le rendre  
deposit.number=1 # type : int | Nombre maximum de fichier à rendre, 0 pour illimité  
deposit.size=20 # type : int | Taille max d'un fichier en Mo  
restriction.begin=26/11/1996-00:05 # type : date() | date de début du devoir maison  
restriction.end=26/12/1996-00:05 # type=date() | date de fin du devoir maison  

## Création de groupe

Les étudiants doivent créer ou rejoindre leurs groupes si l'enseignant a choisis de déléguer la création des groupes à ses étudiants.
Pour cela, ils se rendent dans leur tableau de bord, il clique ensuite dans un menu "groupe".
Dans ce menu, les étudiants voient toutes les disciplines où ils ont besoin de créer un groupe. Ils cliquent donc sur la discipline voulu. Une fois dans la discipline, les étudiants voient tous les groupes déjà créer et peuvent en créer ou rejoindre. Pour créer un groupe, un étudiant clique sur le bouton "créer un groupe" et doit saisir le nom et le mot de passe de son groupe. Pour rejoindre un groupe, il clique sur "rejoindre" à coté du groupe qu'il veut rejoindre, et saisit le mot de passe correspondant. Un étudiant qui rejoint un groupe ne peut plus le quitter. Cependant, l'enseignant responsable peut toujours supprimer ou ajouter un étudiant à un groupe.

## Faire un devoir

Pour faire un devoir, un étudiant se rend dans son tableau de bord, il clique sur la discipline souhaité, et clique sur le devoir. Il a donc accès aux exercices ou activités du devoir.

## Rendre un devoir

Pour rendre un devoir, un étudiant doit se rendre sur la discipline voulu, il clique sur le devoir maison correspondant à son besoin, et il a un bouton upload où il peut rendre son devoir sous forme d'archive.
Selon le rendu souhaité par l'enseignant, le rendu doit être fait soit par un seul membre du groupe, soit par tous les étudiants du groupe. Si un étudiant rend plusieurs version d'un devoir, les devoirs précédents sont conservés.

## Récuperer et noter les devoirs

Pour récuperer les devoirs, l'enseignant doit aller dans son tableau de bord, il clique sur la discipline souhaité, puis il va dans le devoir maison voulu. Il peut ensuite voir le statut du rendu des étudiants et il peut cliquer sur télécharger. Il téléchargera donc une archive contenant tous les dossiers des étudiants ayant rendu le devoir, ainsi qu'un fichier csv où l'enseignant doit rentrer une note et un feedback pour chaque étudiant/groupe qu'il corrige. Pour cela, l'application doit désarchiver toutes les archives rendus par les étudiants, et créer une archive contenant tous les dossiers des étudiants / groupes. Cela évite au enseignant de télécharger et désarchiver trop d'archive. Après avoir remplit le fichier .csv avec les notes et les feedbacks, l'enseignant peut réupload le fichier .csv pour stocker les notes dans la base de données.
