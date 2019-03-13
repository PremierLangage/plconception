#Paramétrage 

[Le parametrage sous WIMS](Paramétrage d'une feuille dans WIMS.odt)

Dans un premier temps voici les types de paramétrages disponibles dans WIMS

Nous souhaitons pouvoir utiliser toutes les potentialités des exercices auto-corrigés de WIMS. 

Qu’est-ce qu’un exercice dans WIMS ? 


Pour un étudiant, un exercice est ce qui correspond à une unité d’entrainement avec enregistrement d’une note et qui est visualisé par un carré qui change de couleur au fur et à mesure de la progression dans l’activité. 


Exemple de deux feuilles d’exercices, la première comporte 8 unités et la seconde 14. 


Un carré correspond en fait à une « série d’exercices » qui sont choisis parmi les « exercices élémentaires» par le prof. Une série peut correspondre à une unique répétition d’un exercice. 

Un « exercice élémentaire » peut être relativement simple, et ne demander que de remplir un unique champ. Il peut également être plus complexe et nécessiter de remplir de nombreux champs. Une validation binaire n’est donc pas envisageable dans le cas général. 

    . L’indice de sévérité (entre 1 et 9) va renvoyer une note qui va être plus au moins sévère (maximum de sévérité à 9)  qui dépend du nombre de champs dans lequel la réponse a été correcte (par exemple lorsqu’il y a 4 champs sur 5 de bons avec un indice de 1 la note est proche de 8/10. Dans le cas ou la sévérité est maximale, la note est beaucoup plus faible inférieure à 5/10). 
      
Dans WIMS l’indice de sévérité est fixé au niveau de la « série d’exercice ». Il est figé à partir de l’ouverture de la feuille

    . Le type de notation (max des réussite, prise en compte ou non de la note de qualité, limitation du nombre de tentatives…) est un paramètre fondamental qui oriente les stratégies de travail des étudiants. 

Dans WIMS, la notation est commune à une feuille, elle peut être modifiée même quand la feuille est active.

Autre type de paramétrages : 
    . Ouverture et fermeture d’une feuille/ d’un exercice
        . Dépendance au niveau d’un amphi (a priori pour limiter  le travail du prof), d’un groupe, de l’individualisation. 
            .  discuter/décider des priorités pour les modifications de ces dates : le prof de TD a-t-il ou non la priorité sur le prof d’amphi ?  
            . d’un individu (l’individualisation est-elle prioritaire sur le travail en groupe : i.e. une fois qu’une activité a été modifiée au niveau individuel, une modification au niveau groupe n’est prise en compte que sous des conditions à définir). 
