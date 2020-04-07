
# Droits d'acces à une asset-activité

Chaque activité d'un cours a un fiche access rights intialisé au vide i.e. pas d'accès.

Sinon le fichier contient des lignes avec la syntaxe suivante:

Personnes:droits:datedebut:datefin
Personnes pouvant être :
  - * "etoile" pour tous le monde inscrit au cours
  - @groupename pour indiquer tout les inscrits au groupe défini dans le cours (ou la formation a voir).
  - name pour indiquer une personne en particulier (name étant la clef de la base user)

 TODO DR:  ces droits sont insufissants 
 accès
 visibilité mais pas d'accès 
 accès pour évaluation 
 accès en retard
 visibilité après évaluation 
 visibilité de l'évaluation 
 visibilité de l'évaluation correpondante

droits:
  n lire l'exercice avec une note
  x faire l'exercice sans note 
 
Les deux dates. time d'ouverture et de fermeture.



