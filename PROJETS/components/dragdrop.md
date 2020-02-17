# Composant `DragDrop`

## Modifications .html/.ts/.scss

* Supprimer la propriété `droppedId`. Ajouter une propriété `cloneable` (booléen).

* Remplacer le comportement de drag and drop actuel par le suivant :
  * si la cible n'est pas droppable, on ne fait rien ;
  * si la source est cloneable et la cible est droppable, on copie le content de la source dans le content de la cible ;
  * si la source n'est pas cloneable et la cible est droppable, on échange le content de la source et le content de la cible.

Demos : https://pl.u-pem.fr/filebrowser/demo/11901/ https://pl.u-pem.fr/filebrowser/demo/11902/

  
 * Implémenter un comportant analogue au drag and drop à base de clics (clic sur la source puis clic sur la cible).
