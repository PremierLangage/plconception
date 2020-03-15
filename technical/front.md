# Front-End
L'interface web (Front-End) de PLaTon, peut être divisé en 2 parties :

- des pages dynamiques créés avec Angular (version 9+)
- des pages genérés côté serveur grâce au langage de templating de Django Jinja 2

# Angular

## Un framework complet
Contrairement à d'autres alternatives (React, Vue, Svelte...) Angular n'est pas une librairie mais un **framework complet** fournit avec un ensemble d'outils (unit-testing, animations, routing, formulaires...).

En ce sens, Angular est **très abstrait** et est beaucoup plus **difficile à apprendre** que les autres frameworks. En contre-partie, il permet de créer des applications plus **puissantes**, **sécurisés** et **maintenables**.

Angular est un donc framework fait pour des applications d'entreprise et non pour de simples applications web.


## Un framework supporté par Google (Long Term Support)
Un des plus gros avantages d'Angular est qu'il est soutenu par Google.

En choisissant Angular, le développeur évite un des plus gros problèmes lié à l'utilisation de JavaScript qui est la dépendances à des librairies tierces qui ne sont pas nécessairement retro-compatible avec les différentes versions des frameworks.

L'équipe Angular s'engage à publier une nouvelle version majeure tous les 6 mois avec toutes ses dépendances et chaque version est maintenue pendant 18 mois et reste compatible avec les fonctionnalités de la version précédente qui deviennent dépréciées. En résultat chaque mise à jour du framework ajoute des fonctionnalités et outils augmentant la performance des applications et la productivité des développeurs.

## Une architecture composant.
Contrairement à AngularJS (la première version du framework) qui est basé sur un modèle MVC, Angular est basé sur un modèle composant qui apporte les avantages suivants entre autres.

- **Réutilisation**:

le modèle composant permet de définir une application comme étant divisé en parties indépendantes et réutilisable avec leurs propres logiques (le principe des classes en POO).
 
- **Tests unitaires simplifiés**:

 étant indépendants les uns des autres, les composants facilitent les tests unitaires.

- **Facilité de maintanance**:

un composant est découplé du reste de l'application et est remplaçable avec une meilleure implémentation. En termes simples, il permet une maintenance et une mise à jour efficace du code.

## Angular Elements.
Angular permet de créer des web components (un standard HTML 5) qui permettent des créés des balises HTML (comme les h1, input, video...) réutilisables partout.
Ainsi, un développeur peut utiliser Angular pour créer des élements graphiques aussi complexe soit-il (diagrammes, editor de code, pages completes...) et les réutilisés dans un autre contexte (React, JQuery, Vue, Django-Jinja, HTML pure...).

## TypeScript
Angular profite de la rigueur et flexibilité du langage TypeScript.

TypeScript est une surcouche de JavaScript qui ajoute de la sécurité à ce langage en permettant de capturer et élimiter les erreurs durant la compilation et en augmentant la productivité des développeurs (autocomplétion, quick-fix, find-references, refactoring...) ce qui facilite grandement la maintenance.

# A propos d'AngularJS
AngularJS correspond à la version 1.x Il ne faut pas confondre AngularJS et Angular. Bien que le numéro de version 2.x semblerait indiquer une continuité avec la version 1.x de Angular, il s'agit d'une refonte intégrale du Framework.

La dernière version de AngularJS, AngularJS 1.7, la dernière version de AngularJS est sortie en Mai 2018 et rentre en Long-Term Support (LTS) à partir du 1er Juillet 2018 jusqu'au 30 juin 2021.

# Angular avec Django

Pour le projet PLaTon, l'utilisation d'Angular consiste à créer des custom elements (web components) avec Angular qui seront consumés dans les templates Django et non des applications complètes comme c'est fait habituellement.

Ces custom elements peuvent être complexes comme l'éditeur de code de la plateforme ou simple comme un simple diagramme et pourront commnuniquer avec le backend de la plateforme utilisant l'API rest fournit par ce dernier.

L'avantage de cette approche est que l'équipe de dev front peut être séparé en 2 parties (ceux qui maitrisent Angular et crée des éléments graphiques complexes et ceux qui font du HTLM/JS simple avec Jinja en utilisant les éléments graphiques.

C'est une architecture [micro-frontend](https://micro-frontends.org)

## References:

Site du langage TypeScript:

https://www.typescriptlang.org/

Quelques liens sur les web-components et les custom elements Angular:

https://developer.mozilla.org/en-US/docs/Web/Web_Components

https://blog.nrwl.io/5-reasons-to-use-angular-elements-390c9a629f89

- Quelques liens sur le framework Angular en général:

https://angular.io/

https://guide-angular.wishtack.io/

https://yalantis.com/blog/when-to-use-angular/

https://www.grazitti.com/blog/8-proven-reasons-you-need-angular-for-your-next-development-project/
