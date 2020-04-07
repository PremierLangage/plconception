

# Partage 
Ce document cherche a definir le cahier des charges du partage des ressources sur la platforme.




## Types de modifications 

(a) les fautes d'orthographes, 
(b) le débuggage, l'amélioration, la traduction 
(c) l' ETIQUETAGE versionning/marking/tagging (donner une  étiquette à une version). 

Comment gère-t-on ces modifications nécessaires ? fait-on simplement confiance ? 
Vient aussi la question de

(d)  l'hérédité. 

Comment des corrections d'un ancêtre vont-elles être transférées à ses descendants ? Faut-il un traitement différent suivant que l'on est dans (a), (b) ou (c) ? 

Faut-il que le système indique que lorsqu'un exercice est hérité un nombre n de fois (n à préciser), on incite à changer l'exercice en question en élément d'une librairie ?  



## Etiquetage des Versions 

Concernant le ETIQUETAGE  il faut une norme éditoriale ? 
Un exemple de problèmatique de tagging : 
- un tag spécifique pour les exercices rédigés à l'infinitif, sur un ton neutre... 
- un autre tag pour les exercices rédigés a la deuxième personne du singulier, sur un ton plus proche. 
- un style csv par défaut très neutre. Avec un tag si on respecte ce style ou pas ? 

PROPOSITION : utiliser les cercles.
Les cercles sont des groupes d'editeur sur la plateforme partageant des objectifs.
Chaque cercle a une aut



## Comment fait-on dans WIMS ?

Les auteurs sont formés à la publication lors de leur premier dépôt. Après on leur fait confiance en général.

Il existe deux endroits d'où un exercice est stocké et d'où il peut être exécuté :

    la classe, et dans ce cas le prof peut faire des modifications dessus en directe, corriger des erreurs, debuggage. En règle général c'est très utile, car on a vite fait de prendre un paramètre trop général.
    le dépôt général. Là seul l'auteur peut faire des motifs et elles sont mises à jour toutes les nuits.

En pratique les exercices sont testés un certain temps dans des classes et débuggués en directe au cours des premières utilisations. Elles sont ensuite publiées si le prof est adoubé. Sinon elles ne sont jamais publiées.

## Défauts de la méthode Wims

Perte d'edition collaborative, il n'y a pas de conservations des modifications et proposition faites localement.

## Avantage 

Le prof peut modifier les exos appliqués a ces élèves "facilement". Sans rendre de comptes.
