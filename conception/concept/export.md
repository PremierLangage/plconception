
# Export 

L'export est la possibilité de sauvegarder une ressource PL, bien entendu pour pouvoir l'importer plus tard.

Deux formats d'export/import :
- le format pl avec des = et == 
- le format json

Chaque éléments des modèles django doit avoir deux fonctions export(file,format) et import(file,format).
