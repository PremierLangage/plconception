# Stratégie

La stratégie est l'élément qui gère la dynamique d'interaction d'un étudiant avec une feuille d'exercice.

Exemple : 
* Un mode **révision** qui sélectionne les exercices qu'un [étudiant](../acteurs/etudiant.md) n'a pas réussi
ou pas fait, pour lui proposer une suite d'exercices adapté.

* Un mode **apprendre** qui sélectionne les exercices de base

* Un mode **divertissant** qui permet de défier d'autres étudiants, avec un chrono
et le nombre d'exercice réalisé pendant ce temps imparti

La stratégie peut être crée par un [Enseignant](../acteurs/enseignant.md), il peut lui même définir une stratégie
en lui définissant un nom, et un enchaînement d'exercices, en fonction des données des étudiants.
L'intérêt n'est pas de créer une stratégie individuelle pour chaque élève d'une [classe](classe.md) mais de créer des
stratégies qui puissent s'adapter en fonction des données récoltés qui puisse être adapté automatiquement pour chaque
étudiants (succès, échecs, nombre d'essais etc)

Cependant un Enseignant doit pouvoir avoir la possiblité de créer une stratégie en lien avec des notions ([tags](tag.md))
, et de la **partager via une URL** 


<!--- 
Author : Elaad 
Validator : -
-->
