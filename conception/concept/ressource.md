
# Ressources 

Concept gérant le fait qu'un élément de la plateforme doit avoir un certain nombre de proprtiétés pour être partageable.
Les ressources sont de deux forme la forme textuelle éditable, partageable, modifiable.

la forme compilé non modifiable (non mutable) mais remplaceable, utilisable par un étudiant (un professeur) dans le contexte d'un enseignement réalisé avec la plateforme. 


Les ressouces ont une méthode "publish(PLserveur)" qui permet de les charger dans un server PL. 


Les ressources éditables ont:
- un classement dans Yggdrasil
- des aav auquels la ressource participe
- une discution 
- une structure de stockage
- des dépendances
- des utilisateurs/propriétaire/observateurs/editeurs/

# Les ressources PL 

Les ressources PL sont stockés dans une arborescence versionnée. (Cloud à la Dropbox ?)
https://www.ubuntupit.com/best-cloud-storage-for-linux-15-reviewed-and-compared-for-linux-nerds/

Les ressources sont des objets de la base de donnée :

1. Une référence sur la dernière version de la ressource et la possibilité de remonter dans les versions … (diff, voir la version , voir le patch) … avoir la date et l’utilisateur … blâme/praise 
2. Meta Data
    1. Statut d’usage (ne pas utiliser, exam, jamais servi, une classe, classes multiples)
    2. Héritage, dépendances, bundle 
    3. Statistiques json complexe voir module de stats 
        1. Nombre de classe utilisant 
        2. Nombre d’utilisation 
        3. Exercices 
            1. Nombre d’essai moyen pour réussir
            2. Taux de réussite 
    4. Labels: (open ended)
        1. Label Rouge
        2. Label Upem
        3. Label Euler
 

Types de ressources PL
- exercices INFORMATIONS : Fichiers text / pdf / video/ podcast /autres formats non modifiable sur la plateforme 
- Liens vers des documents externes (i.e. pas stockés sur la plateforme (la question du cache ?))
- Tout les types Exercices 
- Tout les types Activités 
- Sections/chapitres/cours/listes_de_ressources 
- Protocoles de validations (i.e. activités couplés présentiel / plateforme)
