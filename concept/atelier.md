#  Atelier

TODO faciliter la compréhension de l'atelier.

FIXME problème pour la note du correcteur parce qu'il peut pas avoir exacteement la même note que l'application, à approfondir

Un atelier permet aux étudiants de se corriger entre eux. C'est à dire que chaque étudiant doit corriger plusieurs étudiants (choisis de manière aléatoire) sur un ou plusieurs exercices qu'ils ont fait. La correction se fait de manière anonyme.

L'enseignant peut choisir si l'atelier se fait en groupe ou non. Si l'atelier se fait en groupe, chaque groupe corrige donc d'autres groupes (aléatoire aussi).

Un utilisateur ou un groupe doit être corriger par plusieurs utilisateurs/groupe, le résultat sera la moyenne des notes donner par les différents utilisateurs/groupes.
La moyenne permet d'avoir une note "cohérente" (pas basé sur une seule correction).

Pour éviter que les étudiants/groupes donnent des notes aléatoires, il faut que la note que donne chaque élève soit comparé à la note donner par l'application (pl). Ce qui génèrera une note pour le correcteur.

Après qu'un étudiant ait corrigé et noté un autre étudiant, la note du correcteur sera déterminer par le delta entre la note donner par l'application et la note qu'il a lui même donné. En effet, on réduit au total de la note le delta. Le total de la note est la note maximale qu'un étudiant puisse donné à un autre étudiant lorsqu'il corrige un ou plusieurs exercices.

Exemple :

Un étudiant Toto doit noter un étudiant Titi sur 20. La note maximale qu'il peut donner est donc 20/20. L'application (pl) donne une note de 18/20 à Titi et Toto donne la note de 10/20 à Titi. Après avoir noté Titi, Toto obtient une note pour la qualité de sa correction. La note maximale que Toto peut attribuer est de 20 et le delta est de 8, Toto obtient donc un 12/20 pour sa correction.
