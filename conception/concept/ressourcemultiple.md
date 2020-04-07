

# Ressource multiple 

Une ressource multiple contient des liens vers d'autres ressource, le lien indiquant le numéro de version de la ressource ciblée à intégrer dans la ressource mulitple. 

Le choix de {} pour indiquer le numéro de version n'est pas un choix définitif et doit être validé par qui s'occupe du parser.

Exemple:
```
# feuille de tp 
introduction= feuille d'exemple 
@ exo1.pl {1}
@ exo2.pl {111}
@ exo3.pl # pas de numéro de version implique dernière version valide rem: valide est une métadonnée associée a une version.
@ exo4.pl {0} # numéro 0 veux dire dernière édition quelque soit le status
```
