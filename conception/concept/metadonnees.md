
# Métadonnées 

Les méta données sont des informations associées aux ressources. 

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

# Implémentation 

En première lecture pour les donnnées automatiques il faut une table contenant un json avec les données statistiques par ressource. Puis une fois que le système sera un peu plus stabilisé une table avec des entrées fixes pour des recherche plus rapides.

Pour les données ajoutés une deuxième table (ou pas) mais je trouve que l'on a trops de table json qui ne doivent pas être très efficasse ... FIXME.


# Besoin 

Il faut un éditeur de méta données ajoutées.

Il faut spécifier dans le module de stats les stats que l'on stocke dans l


