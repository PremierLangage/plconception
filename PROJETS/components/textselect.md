# Composant `TextSelect`

## Modifications

- Changer la sémantique de la propriété `text` : le texte doit indiquer par des accolades les unités sélectionnables.

~~~
<script>
var index = -1;
string=string.replace(/\{([^\{\}]*)\}/g, function(match,p) {
  index++;
  return `<span data-index="${index}">${p}</span>`;
});
</script>
~~~

- Supprimer la propriété `separator`.

- Ajouter une propriété `single` : booléen qui indique si on peut faire une ou plusieurs sélections (faux par défaut).
