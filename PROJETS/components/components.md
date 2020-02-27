# Tous les composants


* Ajouter une propriété `style` qui permet de définir une CSS inline pour un composant.

Exemple :
~~~
component.style = "color:blue; font-family:arial"
~~~

* Ajouter les classes suivantes dans `styles.scss`

~~~
.icon-check-after p::after {
    font-family: "Font Awesome 5 Free";
    color: #155724;
    margin-left: 1em;
    content: "\f00c";
    vertical-align: middle;
    font-weight: 900;
}

.icon-times-after p::after {
    font-family: "Font Awesome 5 Free";
    color: #721c24;
    margin-left: 1em;
    content: "\f00d";
    vertical-align: middle;
    font-weight: 900;
}
~~~
