

# Atelier 

l'atelier est un environnement permettant la création des données et fichiers accessibles par un établi(workbench/workspace). L'etabli étant l'environnement qui permet la création de ressources.


Un atelier est un ensemble de répertoires et fichier qui sont éditables (CRUD) par le "directeur scientifique" du cercle lié. 
Cet ensemble de fichier apparait dans tout les établis du cercle et des cercle inclus, et sont donc utilisable par les membres du cercle et des cercles inclus.

exemple: un fond de carte, une liste de verbes irréguliers, un exercice type, un calcul de PkA, etc.

Quand un membre du groupe créer un établi il récupère l'ensemble des répertoire de l'atelier du cercle et des cercle englobant.

Le Cercle Ygddrasil contient tout les cercles.
Tout le monde est membre du cercle yggdrasil, le président est le BDFL du projet. 

## Atelier enchasés 

Chaque atelier est lié de façon univoque avec un cercle displinaire. 


Les fichiers et répertoires d'un atelier sont composés des fichiers et repertoire des cercles englobant et de ceuxn défini par le cercle.

par exemple :

Le cercle de Chimie a placé dans son atelier un repertoire data contenant un fichier mendeleiev.csv contenant des informations sur les différent atomes.

le cercle de chimie/chimie generale a  ajouter dans un repertoire model un fichier oxy.pl de type d'exercice sur la réacton d'oxydation.

le cercle de chimie/chimie generale/chimie organique ajouter un repertoire data un fichier aromatique.py qui fournie une fonction qui dit si oui ou non une molécule est une molécule aromatique.


Ainsi un membre du cercle "chimie organique" aura un établi qui contiendra l'arborescence suivante :  
  data/mendeleiev.csv  
      /aromatique.py  
  model/oxy.pl  
  
 
 ## edition de l'atelier 
 
 La modification de l'atelier est autorisé aux membre "editeur d'atelier/secretaire/directeur scientifique" du cercle.

 Deux types de fichier dans la zone d'édition de l'atelier, les fichiers en cours et les fichiers publiés.
 
 
 
 
 



