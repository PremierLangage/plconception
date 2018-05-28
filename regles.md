# Règles de bonnes pratiques

   ### I. Organisation du dossier conception

1. les dossiesr :

             - acteur : liste des acteurs et de leur descriptif
             - casutilisation : liste des cas d'utilisation
             - concept : liste des concepts du logiciel (glossaire)
             - patron : liste des templates disponible (pour écrire l'analyse du besoin)
             
2. les noms de fichiers devront être **explicite** par exemple visiteur.md

3. les fichiers à la racine concernent le **FQM** et la **Qualité**


### II. Conventions

1. Je n'utiliserai que des **minuscules pures** pour le nom des fichiers et dossiers, et les nom des fichiers devront suivre
le nommage utilisé dans les liens dans "Projects/Conception" associé à la tâche.

3. Les fichiers concernant la conception, doivent être écrit en **markdown**

4. les **liens** devront utiliser le format  : 
`[link name](relative_path/file.md)`


### III. Github
   
1. La gestions des tâches sera dans la partie "Projects/Conception"

2. Essayer de choisir une tâche à la fois dans **Projects/Conception** dans
la partie "To do" et la choisir avant de commencer à modifier le ou les fichiers
en question en la déplaçant dans la partie "In progress"

3. Les **modifications** devront être **poussées régulièrement**, pour éviter les
conflits d'ajout/supression entre les fichiers.

4. Si vous avez terminé votre travail sur une partie, veuillez mettre la tâche
de Projects/Conception dans la partie "Done"

5. Créer une issue associée à la tâche pour pouvoir discuter dans l'issue et ainsi garder un historique.
`Créer une issue avec un titre qui fait référence à la tâche et dans le corps, mettre un lien vers le fichier en question
et rajouter dans la tâche l'issue : [Issue numero](#numero)`

### IV. Modification des fichiers

1. Si éventuellement, vous rencontrez des problèmes de conceptions, veuillez
l'indiquer en utilisant l'indacteur **FIXME**.

2. Si vous êtes confronté à un problèmes que vous ne pouvez pas résoudre tout de
suite, ou que vous jugez qu'il méritte une plus grande réfléxion, veuillez
utiliser l'indicateur **TODO** sur une seule **ligne** de façons a pouvoir utiliser grep.

3. N'hésitez pas à **rajouter** des **sections** dans un template, lorsque celle ci vous
paraît **pertinante**

4. Ajouter l'auteur et celui qui a validé le fichier à la fin.
`<!---
Author : dr+Elaad
Validator : dr
value: ok.
-->`
