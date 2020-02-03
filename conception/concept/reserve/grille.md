

# Grille 

Grille d'évaluation ou Grille Critériée 

## Struture d'une grille 

In json :
{ "Text du critère" : [ ("Text niveau 1", pointsniveau1), ... ],
  ...
 }
 
 With évaluation :
 { "studentid":{ dic for student id },
   "evaluation":
    { "Text du critère": { niveau, "commentaire" },
       ...
   },
   "grid" :
   { "Text du critère" : [ ("Text niveau 1", pointsniveau1), ... ],
   ...
   },
}

