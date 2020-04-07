# Composant `MatchList`

## Modifications .html/.ts/.scss

* Conserver le mécanisme de drag and drop pour relier deux noeuds entre eux. Agrandir la zone de drag autour du noeud source et la zone de drop autour du noeud cible.

* Ajouter le comportement suivant quand on clique sur un noeud source ou sur le texte associé :
  - si le noeud est déjà relié à un noeud cible, on supprime le lien ;
  - si le noeud est libre et si on clique ensuite sur un noeud source, on met un lien entre les deux.
