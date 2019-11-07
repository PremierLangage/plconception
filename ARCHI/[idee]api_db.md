En plus des deux serveurs décris dans 0.7.md , une idée est d'ajouter un serveur ne gérant
que la base de données qui propose une api permettant de la manipuler.

Cela permettrait d'isoler le code des activités et de rajouter des plugins qui seront obligés
de passer par l'api du serveur de la base de données au lieu d'y avoir un accès direct
(ce qui est le cas actuellement).


Ainsi on peut définir des groupes d'utilisateurs ayant des accès différents, en particulier,
pou résoudres des questions de RGPD.
