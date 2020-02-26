
# LTI (Learning tools interoperability)  

Protocole utilisé pour accèder à la plateforme PLaTon. 
LTI permet la création d'utilisateur et de classes de manière transparente depuis un LMS, il permet aussi la remonté des notes de PLaTon vers le LMS.


## Création d'un utilisateur

Lorsqu'un utilisateur clique pour la première sur un lien LTI depuis un LMS, un utilisateur équivalent est créé à partir des informations du LMS.

## Création d'une classe

En ce qui concerne la classe, plusieurs cas de figure se présentent :

* Si la classe n'existe pas encore sur PLaTon :
  * Si l'utilisateur est un enseignant, celui-ci arrive sur un formulaire de création de classes pré-remplie avec les informations du LMS.
  * Si l'utilisateur n'est pas un enseignant, celui-ci reçoit une erreur 403.
 
* Si la classe existe déjà, l'utilisateur est ajouté à la classe avec le même rôle que celui qu'il avait sur le LMS.

## Remonté des notes

LTI permet la remonté d'une note par utilisateur pour chaque lien LTI créé. De plus, afin que la remonté soit possible pour un utilisateur, celui-ci doit avoir cliqué au moins une fois sur le lien correspondant.
