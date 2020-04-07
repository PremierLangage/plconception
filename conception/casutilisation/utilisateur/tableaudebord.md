# Tableau de bord


Objectif :  Permet à l'utilisateur de voir sa progression, ses difficultés, ses cours, ses exercices, son classement par rapport à toute sa promotion, il s'agit d'un tableau de suivie.

Résumé général: Lorsque l'utilisateur se connecte il a directement accès à son tableau de bord, dans lequel il voit tous les cours et les notifications auxquels il peux accéder. La tableau de bord est le hub de navigation pour chaque utilisateur.

# Données

Acteur Principal : Utilisateur

Acteurs secondaires : Admin

Fréquence   : fréquence de la connexion

Concurrence : Oui

Déclencheur : se déclenche lorsque l'utilisateur se connecte, quand il clique sur le bouton "Tableau de bord", ou encore lors de l'actualisation de la page.


## Pré-conditions

### Données d'entrées
	login

	classe

Avoir un compte dans la base de données, pour cela il doit [s'inscrire](../visiteur/inscription.md).
L'inscription doit être effectué préalablement.

## Post Conditions

### Donnée sortie
	feuille d'exo

	suivie

	classement étudiant

	validation de tag et d'exercice pour les profs avec un bon karma dans la discipline

En cas de succès : L'utilisateur voit tous son suivie, les exercices qu'il a réussi, qu'il a raté, qu'il n'a pas fait, il voit son "classement" dans la classe et les cours.

En cas d'échec: ré-actualiser la page internet.

# Navigation / IHM 

Principe de navigation du scénario principal, organisation de l'IHM.

Une fois que l'utilisateur s'est connecté, il voit directement son tableau de bord ou il voit son suivi, son classement, ses difficultés dans les matières qu'il est tenu de suivre, il a alors la possibilité de faire de [reviser](../etudiant/reviser.md), d'[étudier](../etudiant/etudier.md), en faisant des exercices, en regardant les cours, il aura aussi la possibilité d'effectuer des [exercices](../etudiant/faireexercice.md) qui lui sont assigné.

## Scénarios

# MAIN SUCCESS SCENARIO

Step    Action

S    [L'utilisateur est sur la page d'acceuil après s'être connecté, il a accès au tableau de bord]

1    [Ce cas d'utilisation commence quand l'utilisateur clique sur le bouton "Tableau de bord", quand il se connecte ou encore quand on entre l'url dans un navigateur.]

2    [il voit ses difficulté en rouge].

3    [il voit ses cours].

4    [il voit ses exercices].

5    [il voit les exercices pas fait en blanc].

6    [il voit les exercices pas fini en orange].

7    [il voit son suivi].

8    [Ce cas d'utilisation se finit lorsque l'utilisateur change de page internet].

# RELATED INFORMATION

Concurrency    [Le tableau de bord s'actualise en temps réel.]

Include Use Cases    [Exercice](../etudiant/faireexercice.md), [Etudier](../etudiant/etudier.md),[Reviser](../etudiant/reviser.md)


<!--- 
Author : Jordan
Validator : Raphael 
-->
 
