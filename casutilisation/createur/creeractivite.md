# Rechercher ou créer une activité

Objectif : Permet aux créateur de chercher une [activités](../../concept/activity.md) ou de la créer si elle n'existe pas.

Résumé général :

* Le créateur peut chercher une activé existante qui répond à ses besoins. La recherche est multicritère, elle peut se faire par nom, discipline, niveau, feuilles d'exercice, ressources, type ...
    Si une activité qui répond au besoin du créateur a été trouvé, le cas d'utilisation est terminé.
    
* S'il n'y a aucune activité qui lui convient, le créateur doit en créer une nouvelle qui répond à ses besoins.

* Lorsque qu'un créateur valide (clique sur le bouton "valider") son activité, ce dernier doit passer par un processus de validation (workflow) avant d'être complètement accepté. Cependant, si le créateur a un karma suffisament élevé dans la discipline, l'activité est accepté directement.

# Données :

Acteur Principal : Créateur

Acteur secondaire : Admin

Concurrence : non

Déclencheur : Se déclenche lorsque le créateur veut créer une nouvelle activité.

## Pré-conditions :

### Données d'entrées

* Avoir le rôle de créateur dans la base de données

### Données de sorties :

* Création d'un nouvelle activé

En cas de succès : L'activité est sauvegardé dans la base de données. Le succès est determiné par la validation de l'activité en question. La validation peut se faire si et seulement si le créateur a complété correctement tous les champs :

* Nom : obligatoire
* Type : obligatoire
* Discipline : facultatif, remplissage automatique si la création se fait directement dans un cours
* Niveau : facultatif, remplissage automatique si la création se fait directement dans un cours
* Stratégie : obligatoire, la stratégie par défaut est sélectionné si le créateur n'a rien sélectionner
* Feuille(s) : obligatoire, possibilité de choisir une ou plusieurs feuilles d'exercice
* Ressource : obligatoire

Lorsque qu'une activité est en cours de création, son fichier est sauvegardé toutes les 10s s'il y eu une modification, ou s'il y a un signal de l'éditeur.

Dans le cas où le fichier n'a pas de répertoire de stockage (il est uniquement dans la zone tampon) il faut demander dans quel répertoire le sauvegarder en proposant un navigateur de répertoires et en demandant le nom du fichier.

En cas d'échec : Grâce à la sauvegarde continue le créateur ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée.

# Scénario

## Main success scenario

Step : Action

* S : Le créateur crée l'activité et le valide. L'activité est ainsi sauvegardé dans la base de données et est en attente de validation. (si son karma est insuffisant)
* 1 : Le cas d'utilisation commence quand le créateur clique sur le bouton "créer une activité" ou lorsqu'il rentre l'URL d'édition d'activité dans le navigateur.
* 2 : Le cas d'utilisation se termine lorsque le créateur a validé son activité.

Step : Branching Condition

* 1 : Lorsque le créateur part avant d'avoir validé ses modifications. Etape 2
* 2 : Lorsque le créateur veut chercher un exercice. Etape 1

na.  Action causing branching :

* 1 : L'éditeur grâce à la [sauvegarde continue](/editeur.md), a gardé en mémoire l'activité que le créateur a commencé à écrire et les affiche.

* 2 : Le créateur trouve l'activité qu'il cherche

# Related information

<!---
Author : Raphael
Validator : Hugo
-->

