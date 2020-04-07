# Rechercher ou créer une activité

Objectif : Permet aux créateur de chercher une [activités](../../concept/activity.md) ou de la créer si elle n'existe pas.

Résumé général :

* Le créateur peut chercher sur PL une activé existante qui répond à ses besoins. La recherche est multicritère, elle peut se faire par nom, discipline, niveau, feuilles d'exercice, ressources, type ...
    Si une activité qui répond au besoin du créateur a été trouvé, le cas d'utilisation est terminé.
    
* S'il n'y a aucune activité qui lui convient, le créateur doit en créer une nouvelle qui répond à ses besoins. La création de l'activité se fait depuis Moodle. Le créateur crée une activité sur Moodle, puis il est redirigé vers PL avec l'ID de l'activité qu'il vient de créer. Il peut ainsi créer son activité après avoir remplit les champs nécéssaire.

* Lorsque qu'un créateur valide (clique sur le bouton "valider") son activité, elle est intégré à son cours.

# Données :

Acteur Principal : Créateur

Acteur secondaire : Admin

Concurrence : non

Déclencheur : Se déclenche lorsque le créateur veut créer une nouvelle activité.

## Pré-conditions :

Avoir l'ID Moodle de l'activité qu'il doit créer

### Données d'entrées

* Avoir le rôle de créateur dans la base de données, et qu'il soit responsable du cours.

### Données de sorties :

* Création d'une nouvelle activé

En cas de succès : L'activité est sauvegardé dans la base de données. Le succès est determiné par la validation de l'activité en question. La validation peut se faire si et seulement si le créateur a complété correctement tous les champs :

* Nom : obligatoire
* ID Moodle : obligatoire, remplissage automatique
* Type : obligatoire
* Discipline : facultatif, remplissage automatique si la création se fait directement dans un cours
* Niveau : facultatif, remplissage automatique si la création se fait directement dans un cours
* Stratégie : obligatoire, la stratégie par défaut est sélectionné si le créateur n'a rien sélectionner
* Feuille(s) : obligatoire, possibilité de choisir une ou plusieurs feuilles d'exercice
* Ressource : obligatoire

Dans le cas où le fichier n'a pas de répertoire de stockage (il est uniquement dans la zone tampon) il faut demander dans quel répertoire le sauvegarder en proposant un navigateur de répertoires et en demandant le nom du fichier.

En cas d'échec : Grâce à la sauvegarde continue le créateur ne perd pas les modifications qu'il a effectué en "local". La base de données reste inchangée.

# Scénario

## Main success scenario

Step : Action

* S : Le créateur crée l'activité en complétant tous les champs nécéssaire et le valide. L'activité est ainsi sauvegardé dans la base de données.
* 1 : Le cas d'utilisation commence quand le créateur crée une activité sur Moodle et qu'il est redirigé vers PL.
* 2 : Il remplit le formulaire
* 3 : Le cas d'utilisation se termine lorsque le créateur a validé son activité.

Step : Branching Condition

* 1 : Lorsque le créateur part avant d'avoir validé ses modifications. Etape 3
* 2 : Lorsque le créateur veut chercher un exercice. Etape 1
* 3 : Lorsque le créateur valide sans avoir remplit tous les champs. Etape 3

na.  Action causing branching :

* 1 : L'éditeur grâce à la [sauvegarde continue](../../concept/zonetampon.md), a gardé en mémoire l'activité que le créateur a commencé à écrire.
* 2 : Le créateur trouve l'activité qu'il cherche.
* 3 : Le créateur retourne donc à l'étape 2.

# Related information

<!---
Author : Hugo
Validator : 
-->

