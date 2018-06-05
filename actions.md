# Actions

Les actions sont une formalisation des activités des utilisateurs sur le site PL.

Une action est faite par un utilisateur et une ressource. 
Les actions de base sont:
- CreateReadUpdateDelete pour les ressources 
- validate/Annotate i.e. modification des métadata d'une ressource 

La réalisation (success) d'une action entraine des opération du système:
- Quand un exercice est validé, le propriétaire de l'exercice est notifié, et sa réputation est augmentée, le validateur gagne aussi en réputation. 



## Table des actions 
| Action | Description | URL/URI | Droits | Qui est notifié |
|--------|-------------|---------|--------|-----------------|
|Créer exercice |Créer un nouvel exercice|  /discipline/createexercice | Avoir le rôle de créateur  |[Responsable de formation](acteurs/reponsable)|
|Créer exercice en ajoutant des paramètres de notification|             |         |        |                 |
|        |             |         |        |                 |
