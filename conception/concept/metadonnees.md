
# Métadonnées 

Les méta données sont des informations associées aux ressources. 

## Métadonnées et versions 

Par défaut si l'on édite pas les métadonnées elle sont les mémes que la version précédente de la ressource (récursivement, jusqu'a la valeur par défaut de la version zéro).

## Valeur par défaut des métadonnées

??? FIXME 

## Méta données automatiques
Les méta données automatiques sont essentiellement statistiques,
nombre d'utilisation, temps de réalisation, temps moyen, temps médian,
nombre de success, nombre d'abandons,
nombre d'intégration dans une activité,
etc. 

Si la ressource est une évaluation (utilisation au moins une fois comme évaluation).



## méta données ajoutées

Les méta données ajoutées doivent être sous une forme distribuée, càd que les éditions des un n'ont pas d'effet sur les éditions des autres.
Ainsi toutes les métas données de ce type sont de la forme:

    user X donne la propriété Y à la ressource.
    la propriété Y est soit un lien entre ressource,soit un json (ce qui permet d'ajouter de nouvelle propréitéé au fur et a mesure).

### Quelques type de méta données 

FIXME: Groupe de travail sur le sujet;

* utilisabilité: en production, utilisable, a valider, a patrouiller 
* cercle: labels-du-cercle
* tests: test fonctionnels, test-automatiques, etc 
* niveau scolaire: X,y,z
* Qualité: Excellent, bon , correct, a revoir
* Usage:  hors ligne, présentiel, groupes, examen, evaluation, formatif, mixte,etc


# Implémentation 

En première lecture pour les donnnées automatiques il faut une table contenant un json avec les données statistiques par ressource. Puis une fois que le système sera un peu plus stabilisé une table avec des entrées fixes pour des recherche plus rapides.

Pour les données ajoutés une deuxième table (ou pas) mais je trouve que l'on a trops de table json qui ne doivent pas être très efficasse ... FIXME.


# Besoin 

Il faut un éditeur de méta données ajoutées.

Il faut spécifier dans le module de stats les stats que l'on stocke dans l


