# Gestionnaire de Version

* Ce projet correspond au design technique de la résolution du ticket :
  https://github.com/PremierLangage/premierlangage/issues/204


## Objectifs globaux du projet

* Centraliser les contributions dans un endroit commun pour favoriser les mutualisations,
  échanges et collaborations de manière générale.
* Cacher les détails techniques de sauvegarde et de pérénisation des productions pédagogiques.
* Permettre une grande flexibilité pour l'utilisateur (ici les enseignants éditeurs) dans les
  choix de versions.
* Monter en qualité via la mise en place de version de référence pour chaque ressource
  (à la Wikipédia).



## Versionnage

Chaque ressource est une suite de version, commençant à la version `#0`.

```text
+------------+      +------------+      +------------+
| file.txt#0 +----->+ file.txt#1 +----->+ file.txt#2 |
+------------+      +------------+      +------------+
```

A tout moment, une ressource peut être *downgrade* en plaçant une ancienne version comme nouvelle
version:

```text
                           ........................................
                           .                                      |
+------------+      +------------+      +------------+      +-----v------+
| file.txt#0 +----->+ file.txt#1 +----->+ file.txt#2 +----->+ file.txt#3 |
+------------+      +------------+      +------------+      +------------+
```

Dans les fait, la version précédente de `#3` est la version `#2` et non la version `#1`.
Un utilisateur ne verrais que:

```text
+------------+ commit1 +------------+ commit2 +------------+ downgrade to #1 +------------+
| file.txt#0 +-------->| file.txt#1 +-------->| file.txt#2 +---------------->| file.txt#3 |
+------------+         +------------+         +------------+                 +------------+
```


On peut imaginer que le saut de `#1` à la `#2` n'a pas été fait en seule séance de travail car l'auteur
à du débuguer sa ressource durant une semaine. L'utilisateur doit donc être capable de sauvegarder
une version personnelle et temporaire, il n'est pas nécessaire de garder un versionnage de la partie
local d'un utilisateur, seul sa dernière sauvegarde est gardé.

A chaque version est associé un descriptif des changements par rapport à la version précédente (*commit*).



## Conflits

Supposons que deux utilisateur, Bob et Alice, édite en même temps la même ressource, mais que Alice
sauvegarde avant Bob:

```text
                                                     Alice   +------------+
                                                        +--->+ file.txt#3 |
                                                        |    +------------+
+------------+      +------------+      +------------+  |
| file.txt#0 +----->+ file.txt#1 +----->+ file.txt#2 +--+
+------------+      +------------+      +------------+  .
                                                        .    +------------+
                                                        ...->+ file.txt#3 |
                                                       Bob   +------------+

```

Il faut alors notifier Bob qu'une modification à eu lieu entre temps, et lui laisser proposer trois
choix:

1. Abandonner ses modifications :

```text
+------------+         +------------+         +------------+   Alice   +------------+
| file.txt#0 +-------->| file.txt#1 +-------->| file.txt#2 +---------->| file.txt#3 |
+------------+         +------------+         +------------+           +------------+
```

2. Repartir depuis la nouvelle version en le laissant gérer les possibles conflits (équivalent `git rebase`)

```text
+------------+         +------------+         +------------+   Alice   +------------+    Bob    +------------+
| file.txt#0 +-------->| file.txt#1 +-------->| file.txt#2 +---------->| file.txt#3 |---------->| file.txt#4 |
+------------+         +------------+         +------------+           +------------+           +------------+
```

3. Créer un nouveau fichier avec ses modifications (*fork*):

```text
                                                      Alice  +------------+
                                                        +--->+ file.txt#3 |
                                                        |    +------------+
+------------+      +------------+      +------------+  |
| file.txt#0 +----->+ file.txt#1 +----->+ file.txt#2 +--+
+------------+      +------------+      +------------+  |
                                                        |    +--------------------+
                                                        +--->+ another_file.txt#3 |
                                                       Bob   +--------------------+

```

Dans le cas *3.*, il y a donc maintenant deux fichiers avec chacun son historique:

```text
+------------+         +------------+         +------------+   Alice   +------------+
| file.txt#0 +-------->| file.txt#1 +-------->| file.txt#2 +---------->| file.txt#3 |
+------------+         +------------+         +------------+           +------------+

+------------+         +------------+         +------------+    Bob    +--------------------+
| file.txt#0 +-------->| file.txt#1 +-------->| file.txt#2 +---------->| another_file.txt#3 |
+------------+         +------------+         +------------+           +--------------------+
```

Nous gardons ainsi nos historiques linéaires.



## Implémentation

### Système de fichier

(D.R.) Attention les répertoires EXT4 et autres sont très lents dés que le nombre d'entrées devient trop grand.
Ce qui posse deux problèmes: un fichier avec beaucoup de versions ?
le repertoire Yggdrasil qui devient trop grand (celui ci est plus facile à gérer : il faut des sous répertoires), 
et il me semble bien qui y ai un classement des ressources par disciplines et par themes et par niveau, ..., donc la ligne suivante est modifiée.

Les ressources sont stockés dans sous dossier du dossier `Yggdrasil/`. 

Chaque nouvelle ressources corresponds à un dossier dans l'arborescence `Yggdrasil/` portant le nom
de la ressource, dans lequel se situe un fichier `[name]#[version]` ainsi
qu'un fichier`[name]#[version].meta`, par exemple:

```
Yggdrasil/
├── enantiomere
│   ├── enantiomere#0
│   ├── enantiomere#0.meta
│   └── enantiomere#1
│   └── enantiomere#1.meta
└── fraction
    ├── fraction#0
    ├── fraction#0.meta
    ├── fraction#1
    ├── fraction#1.meta
    ├── fraction#2
    └── fraction#2.meta
```

Le fichier `[name]#[version]` est la ressource en elle même (texte, pdf, image...), le ficher `[name]#[version].meta`
contient les méta-données ainsi que les données relative à la version (commit, auteur, précédent, dépendances). 


### Base de Données

Chaque version possède une entrée associée dans la base de données avec la table:

![resource](uml/resource.png).

En cas de fork, les entrées des anciennes version sont dupliqués. Pour reprendre
l'exemple ci-dessus:

```
                   +------------+         +------------+         +------------+   Alice   +------------+
                   |   file#0   +-------->+   file#1   +-------->+   file#2   +---------->+   file#3   |
                   +------+-----+         +-----+------+         +-----+------+           +------+-----+
                          |                     |                      |                         |
                          |                     |                      |                         |
Yggdrasil/                |                     |                      |                         |
├── file                  |                     |                      |                         |
│   ├── file#0<-----------+                     |                      |                         |
│   ├── file#1<-----------|---------------------+                      |                         |
│   ├── file#2<-----------|---------------------|----------------------+                         |
│   └── file#3<-----------|---------------------|----------------------|-------------------------+
└── another_file          |                     |                      |
    └── another_file#3<---|---------------------|----------------------|-----------------------------+
                          |                     |                      |                             |
                          |                     |                      |                             |
                   +------+-----+         +-----+------+         +-----+------+    Bob    +----------+---------+
                   |   file#0   +-------->+   file#1   +-------->+   file#2   +---------->+   another_file#3   |
                   +------------+         +------------+         +------------+           +--------------------+

```

Ainsi, seul les entrés en base de données sont dupliqué, mais non les fichiers et les metadata (celle-ci étant une clé étrangère).

Le système de fichier est en soit suffisant, le base de données pouvant être entièrement créer à partir de celui-ci.
Celle-ci permet surtout un interfaçage plus rapide avec le code que *parser* un système de fichier.



Remarques:
===============

* (N.B.) Sachant qu'une ressource finale (anciennement un fichier) est maintenant un repertoire contenant des fichiers qui sont
donc les versions de cette même ressource finale, je dirais que `[name]#[version]` est redondant pour la partie `[name]`. Ceci
est une remarque seulement...
  * (Q.C.) Cette redondance est voulue, elle permet d'identifier une ressource et sa version juste avec le nom du fichier. Cela
  permet, en cas de gros pépin ou de gros changement, de reconstruire la base de données avec le système de fichier.

* (N.B.) Qu'est ce que créer un repertoire vide dans ce monde ? C'est versionné ou pas ? Les autres verrons ou pas le nouveau
repertoire ? S'il doivent actualiser leur browser, peut-il y avoir des conflits ou des problèmes ?
  * (Q.C.) Il n'y a pas de répertoire vide, le système de fichier est géré par le serveur, les utilisateurs n'y accède pas mais
  passe par une interface. 
  * (D.R.) Je suis pas sur de comprendre il y a deux systèmes de fichiers ? Le physique et un logique dans l'interface ? 
  * (D.R.) je trouve que: Les dossiers vides n'existe pas comme dans git. Si l'on créer un fichier avec un nom de répertoire
  innexisgtnt il est créer. Me semble raisonnable. 

* (N.B.) Peut-on éviter les copies profondes d'historiques ? Si on inverse le sens des flèches, chaque version qui n'est pas une
création de nouveaux fichier from scratch à une et une seule version père.
  * (Q.C.) La copie profonde d'historique ne se fait que sur la base de données, aucune copie n'est faites sur le système de
  fichier. Cette copie profonde est surtout pour le coté programmation: elle assure que `ressouse->prev->next` pointe bien sur
  `ressource`. Le système de fichier serait:
    ```
    Yggdrasil/
    ├── file
    │   ├── file#0
    │   ├── file#1
    │   ├── file#2
    │   └── file#3
    └── another_file
        └── another_file#3
    ```

* (N.B.) Question : À terme, on veut stocker quoi ? Demandez à D.R. s'il a déjà des idées (statistiques, méta-données, infor
auto-générées, q[my_list[x:x+5] for x in range(0, len(my_list),5)]ualification des ressources, review, tests, vaidations, etc)...
  * (D.R.) : Nicolas Toute ta liste est effectivement au programme, mais il faut distinguer deux type d'informations, les
  informations "manuelles/créatives" qui sont produites par une édition d'un utilisateur, exemple : exercice, activité, structure
  de cours, AAV, ontologie, video, sound etc.
  Les informations méta dont l'édition ne modifie pas les propriétés fonctionnelles et pédagogique de la ressource, mais les
  propriétées didactiques et les données de qualité/historiques/statistique etc. 
  
* (N.B.) Question : Peut-on monter en charge... 3 (ou 4 ou 5) personnes éditent en même temps la même ressource et cliquent 
successivement sur save... Vérifiez par des petits dessin ou autre que tout marche (j'en suis presque convaincu mais IL FAUT 
VÉRIFIER avant de se commit sévère sur une stratégie). Par exemple, au moment de la savegarde, il faut établir un script (ou une 
fonction) qui ouvre une boite de dialogue du style : "Vos modiffication sont basé sur une version en retard de 3 publications, 
que voulez-voir faire : 1 visualiser la dernière version dans un nouvel onglet, 2 rebase depuis la dernière version, 3 jettez vos 
modification, 4 vous différencier en créant un exercice différent de la dernière verion..."
  * (D.R.) il faut ajouter une information de partage quand on prend un fichier pour l'éditer, la couleur du fichier (ou autre
  chose de visuel) m'indique qu'il est déjà ouvert en modification par quelqu'un d'autre. Sinon il faut faire effectivement
  attention à avoir un verrou partagé qui doit nous assurer que deux processus ne vont pas créer la même version. Je pense que la
  base de donnée doit avoir ce type d'outil logiciel.

* (N.B.) Question : Niveau overkill, je n'ai pas fait de calcul ou estimation pour évaluer approximativement la quantité de chose 
à sauvegarder mais est ce que ça vaut le coup de stocker les contenus complets de chaque version ? Pourquoi ? Est ce que ça peut 
être dangeureux ou pas ? Faut-il limiter de nombre de save par seconde ?
  * (Q.C.) On y pensé, les fichiers les plus lourds (image, vidéo, pdf...) ne sont que rarement modifiés. Seuls les fichiers
  textes sont beaucoup modifiés, sachant que `graderC` (qui est relativement gros) pèse environ 19Ko, il faudrait 52 631 version 
  le modifiant entièrement (c'est à dire les 19Ko à chaque fois) avant d'atteindre 1Go. Je trouve personellement que cela reste 
  correct.
  * (D.R.) Ouaip. 

* (N.B.) Question : Une inode Unix contient de nombreuse date... Est-ce suffisant ou faut-il dater dans des fichiers de méta données les versions ? Fichier unix = ? = fichier de version
  * (Q.C.) La date de création de l'inode me semble suffisante. (D.R.) Ouaip moi aussi.
  

* (N.B.) Peut-on supprimer des version ? Est ce que c'est bien ? Est ce que c'est pas dérangeant...
  * (Q.C.) Supprimer des versions pourrait causer des problèmes, mais je ne vois pas de cas pour lesquelles se serait nécessaire.
  * (D.R.) Obsolecence programmée peut-on détruire une ressource ??  Apriori Oui, c'est la qu'un git externe serait utile.

* (N.B.) Comme on versionne tout save, si on clique sur save avant une version finale et fonctionnelle, on écrase, durant un 
moment et sans vraiment le vouloir la dernière version des ressources. Durant le lap de temps ou la personne a fait un save 
préliminaire et avant qu'il termine sa refonte, le serveur de ressources publie donc une version pourrie (car probablement 
cassée) de la ressource. Est ce grave ? Pourquoi ? Comparaison à wikipedia ?
  * (Q.C.) Cela pourrait effectivement poser des problèmes. Une solutions pourrait être un système de validation : chaque version  
  doit être approuvée par certain membres certifiés, un warning étant affiché sur la ressource tant que celle-ci n'est pas 
  approuvée.
  * (D.R.) non cela est trop lourd. Les versions partielles sont en mémoire si l'on fait une sauvegarde cela créer une version 
  physique. La certification/validation etc est faite par les méta datas qui indique quelle version est certifié/validée. Je suis 
  pas encore conveincu ici ...
   

* (N.B.) TODO : imaginer une ressource qui importe buider et grader (un exo .pl qui importe et inclu 2 script .py eux aussi 
versionnés...). Imaginer maintenant Alice, Bob et Charlie qui édite un peu chaotiquement ces trois ressources interdépendantes et 
tentez d'imaginer les risques... Est ce qu'on est bon ? Faut-il des checker ? Autorise-t-on la publication quand on casse. Est ce 
qu'un importe de builder importe toujours la dernière version de ce builder ? Faut-il introduire un nouvel import : @ /C/template
/mon_builder.py#23 (import de la version 23 de la ressource mon_builder.py) ?
  * (Q.C.) C'est le principale problème, il y a un problème dans tout les cas: Si une ressource se sert toujours de la dernière 
  version d'une dépendance, celle-ci peut casser la ressource lors d'une mise à jour. A l'inverse, si elle ne se sert pas 
  automatiquement de la dernière version, il sera nécesssaire de mettre à jour chaque ressource manuellement.
 * (D.R.) IL faut parler d'**ASSETS**, un asset est défini sur une ressource versionnée, quand on fait un **reload** il faut que 
 l'on prenne des décisions sur ce que l'on veux charger, soit à la main, soit en choisisant un algorithme, du type "toutes les 
 versions validées", "les dernirère versions", "les versions postérieur à ma version avec le tag='label jaune'". 
 Ainsi l'asset garde l'information de version, c'est le rafraichissement qui réalise le réalignement.
 
* (N.B.) Le serveur ressource central crashe (Copernic est immondé...), comment on récupère le travail ? Comment on fait les basckup ? Rsync suffit ? Rsync + cron et on est peinard ? On git Yggdrazil dans un cron toute les heures ?
  * (Q.C.) Rsync me parait être la meilleur solution.
  * (D.R.) deux technique vale mieux qu'une non ? Que dit N.C. 

* (N.B.) Comme commentaire final, je dirais que l'approche me parait très sympa à priori. J'aime bien le coté simple et jetter 
git si possible... Par contre, certaines remarques au dessus sont pourries ou rapidement balayée mais quelques unes me semblent 
un peu profondes. Je serais convaincu si d'autres cerveaux malades se pensent sur cette modélisation avant de passer à l'action. 
On est dans un cas de design ou il faut passer beaucoup de temps à refléchir avant de coder (sinon le code va finir direct à la 
poublelle.). Je continue de penser que le problème est compliqué et je serai heureux que la solution soit simple. Il faut se 
méfier toutefois des solutions simples : elles existent mais il faut les éprouver... En espèrant que le patron prenne le temps de 
lire la proposition et les commentaires bien concentré...

  * (D.R.) si le problèmes des répertoires peut être réglé (c'est nécessaire uniquement sur le serveur de ressources).
  * (D.R.) je veux bien une description de la technologie de verrous pour l'accès à l'integer de version. je suis preneur d'une simulation de quelques exemple tordus.

 
