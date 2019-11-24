# LMS

Learning Managment system

## Learning Tools Interoperability (LTI)

* [Specifications 1.0](https://www.imsglobal.org/specs/ltiv1p0/implementation-guide)
* [Specifications 1.1](https://www.imsglobal.org/specs/ltiv1p1/implementation-guide)
* [Specifications 1.2](https://www.imsglobal.org/specs/ltiv1p2/implementation-guide)  
* [Specifications 2.0](https://www.imsglobal.org/specs/ltiv2p0/implementation-guide)  
* [Specifications 2.1](https://www.imsglobal.org/specs/ltiv2p1/implementation-guide)  


### LMS -> PL

Informations récupérables depuis le LMS:

* Contexte :
  * Nom du LMS
  * URL du LMS
  * Langue
  * Nom de la classe
  * Label de la classe
  * ID de la classe dans sur le LMS
  * ID unique pour chaque lien LTI
  * URL sur laquelle renvoyé des notes potentielles

* Utilisateur
  * Nom
  * Prénom
  * Mail
  * Role
  * ID de l'utilisateur sur le LMS

***Note :*** Les informations ne sont unique que pour un LMS, il faut donc coupler le LMS à celle-ci si une instance de PL se sert de plusieurs LMS.

### PL -> LMS

Informations envoyable au LMS:

* Une note par lien LTI et par utilisateur (flottant entre 0 et 1).


