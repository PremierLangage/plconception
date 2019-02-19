
# Droits d'acces à une activité

Chaque activité d'un cours a un fiche access rights intialisé au vide== pas d'accès.

Sinon le fichier contient des lignes avec la syntaxe suivante:

Personnes:droits:datedebut:datefin
Personnes pouvant être :
  - * "etoile" pour tous le monde inscrit au cours
  - @groupename pour indiquer tout les inscrits au groupe défini dans le cours (ou la formation a voir).
  - name pour indiquer une personne en particulier (name étant la clef de la base user)

droits:
  n lire l'exercice avec une note
  x faire l'exercice sans note 
 
Les deux dates.time d'ouverture et de fermeture.



