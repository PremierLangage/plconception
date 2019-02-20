
# Ontologie

Les ontologie de Premierlangage sont de deux formes, les "ontologie du domaine", qui sont définies sur les grains (du domaine).
Les "ontologies pratiques" qui sont des ontologies spécifiques à une activité, un cours ou une classe.

Elles sont basées toutes deux sur le même type de donné: Ontologie, la différence est de pouvoir associer dans le premier cas uniquement des grains, dans le deuxième cas n'importe quelle ressource peut être associée à un noeud de l'ontologie.


Pour pouvoir faire de l’apprentissage adaptatif, il est essentiel de rattacher les exercices à des concepts/ des cartes concepts / à des variables didactiques, à une/des ontologie(s), à des objectifs d’apprentissage visés… Toutes ces informations peuvent être déposées et/ou validées par des acteurs différents : 
    • les didacticiens  
    •  les enseignants  
    • les élèves   
    • à terme des logiciels ...  
Elle n’ont pas  a être forcément absolument cohérentes (il peut y avoir plusieurs écoles de didactique, plusieurs points de vues entre enseignants, entre profils d’étudiants).  

Elles permettent de 
    • faciliter le choix des exercices pour l’enseignant  
    • donner des informations « méta » aux étudiants (une activité pourrait-être de valider et ou proposer de nommer les concepts utilisés dans un exercice)  
    • de faire de l’adaptatif, de la validation des choix des profs (est-ce le meilleur ordre/ adpatation suivant les profils d’étudiants…)  

# Construction d'une ontologie 

Toutes les ontologies sont construite sur le même principe.
Des **objets externes** sont associés de façon univoques à des **noeuds** de l'ontologie. 
Les Noeuds de l'ontologie sont associés par des **relations** typées (le type par défault étant le prérequis).

L'affichage des ontologie ce fait avec un module utilisant graphviz (cf. [Vieux Projet pl](http://pl.univ-mlv.fr) )

# Types logiques 
## Ontologie du domaine
L'ontologie du domaine est un graphe de Noeuds (chaque Noeud est lié de façon univoque avec un grains défini dans la discipline).

Les relations entre les Noeuds sont pour le moment (20/02/2019) limités a une relation de prérequis. 
Un grain A est le prérequis du grain B si il faut avoir compris A pour apprendre B.

Elle est utilisée pour représenter les relations dans les connaissances de base d'un domaine/une discipline/un cours particulier.

## Ontologie Pratiques

Les ontologies pratiques de PL sont utilisées soit pour une representation des connaissance comme les ontologie de domaine. Soit dans une approche plus pratique (d'ou le nom), ou l'ontologie est un outil de gestion de la progresssion de l'élève.

L'ontologie est utilisée pour mesurer l'avancement (avec les Noeuds maitrisés), piloter la progresssion en proposant des exercices à la limites des connaissances de l'élève, exprimer le niveau atteint par l'élève (affichage de la liste des Noeuds limites).




cf. 
http://www.journaldunet.com/developpeur/tutoriel/theo/070403-ontologie.shtml
