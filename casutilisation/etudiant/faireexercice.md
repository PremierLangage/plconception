
# Faire exercice
Objectif : Permettre à l'étudiant de faire un exercice

Résumé général : Donner accès à des exercices pour qu'un étudiant puisse les faire


# Données

Acteur Principal : Etudiant

Concurrence : Non



## Pré-conditions

L'étudiant doit être connecté(login.md), TODO être inscrit à un cours, TODO une feuille doit avoir été ajouter et avoir accès à une feuille (accesfeuilleexercice.md).


## Post Conditions

TODO
L'étudiant a accès à un exercice avec un sujet, il peut y répondre sous différentes formes suivant la nature 
de l'exercice, sous la forme d'une boite de texte ou d'un QCM. 

TODO
En cas de succès : L'étudiant a eu la bonne réponse à l'exercice, un message s'affiche pour lui dire qu'il a 
réussi l'exercice et on passe à un autre exercice s'il y en a un. Soit un exercice de la même notion s'il en 
a réussi qu'un seul(ou plusieurs) sinon un exercice d'une autre notion, on délègue cela à la stratégie.

TODO
En cas d'échec : L'étudiant s'est trompé dans sa réponse, un message s'affiche pour lui dire qu'il s'est 
trompé et on passe à l'exercice suivant de la même notion s'il y en a un (on délègue cela à la stratégie).
Si l'étudiant quitte la page avant d'avoir validé, son travail est sauvegardé et il le retrouvera lorsqu'il 
reprendra son exercice.

Une fois l'exercice terminé, l'étudiant peut donner son avis sur l'exercice qu'il vient de faire(de façon 
anonyme) ou passer directement à l'exercice suivant.


# Navigation / IHM 

Lorsqu'un étudiant fait un exercice, il a un énoncé auquel il doit répondre, soit dans une zone de texte, 
soit sous forme de QCM. Une fois qu'il a répondu, l'étudiant doit cliquer sur le bouton valider. 
Ensuite pour passer à l'exercice suivant, l'étudiant peut soit donner son avis sur l'exercice qu'il vient de 
faire  en cliquant sur un bouton (trop facile, trop dure, etc. ou en écrivant une remarque dans une zone de 
texte) ou sur un bouton passer à l'exercice suivant s'il ne veut pas donner son avis.
Si l'étudiant quitte la page avant de valider, il retrouvera le travail qu'il avait effectué avant de 
quitter lorsqu'il reprendra son exercice.



## Scénarios

MAIN SUCCESS SCENARIO

S	[l'étudiant peut faire un exercice]

1	[L'étudiant se trouve sur la page d'un exercice]

2	[L'étudiant répond à l'énoncé et valide sa réponse]

3	[Sa réponse est correcte et il peut soit donner son avis sur l'exercice ou passer au suivant]

4	[L'exercice est terminé]



EXTENSION SCENARIOS

1	[La réponse de l'étudiant est fausse] Etape 3

2	[L'utilisateur quitte la page avant de valider]

[na. Condition causing branching:]

1 : Sa réponse est fausse et il peut soit donner son avis sur l'exercice ou passer au suivant

2 : Le travail que l'étudiant a effectué est sauvegardé



RELATED INFORMATION

Include Use Cases	[Login](login.md)
	                [Accès feuille/exercice](accesfeuilleexercice.md)



<!--- 
Author : Raphael
Validator :  
-->
