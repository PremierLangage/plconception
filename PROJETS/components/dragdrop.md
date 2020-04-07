# Composant `DragDrop`

## Modifications .html/.ts/.scss

* `groupId`
* `type` : `label` ou `dropzone`
* `cloneable` pour les dragdrops de type `label`
* `origin`

* Remplacer le comportement de drag and drop actuel par le suivant :
  * si la cible n'est pas une dropzone avec le même groupId que la source, on ne fait rien ;
  * sinon,
   * si la source est un label cloneable, on copie le content de la source dans le content de la cible ;
   * si la source est un label non cloneable, on renvoie le content actuel à son origine (s'il y a une origine), on copie le content de la source et l'origine, on vide le content de l'origine ;
   * si la source est une dropzone, on échange le content et l'origine entre les deux dropzones.

Demos : https://pl.u-pem.fr/filebrowser/demo/11901/ https://pl.u-pem.fr/filebrowser/demo/11902/

  
 * Implémenter un comportement analogue au drag and drop à base de clics (clic sur la source puis clic sur la cible).
