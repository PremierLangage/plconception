
# Base de données

# SQLite3 avantages :
- SQLite a l'avantage d'avoir des BDD très légères, elle est donc pratique pour tous les logiciels embarqués sur des appareils : ex smartphone pour une application.
- Performances très correctes en W/R, environ 35% plus efficace qu'avec un filesystem.
- Ne garde en mémoire que ce qui est demandé, pas de données inutiles en mémoire. (si SQLite n'a besoin que d'une 	- partie du fichier elle ne stocke que cette partie)
- Ecriture par partie, elle n'édite que ce qui a été changé.
- Pas de configurations, elle ne nécessite que la SQLite library
- Elle stocke l'entièreté de sa base sur un seul et unique fichier. (SQLite database files have a maximum size of about 140 TB.)
- Mise à jour en continue, donc très peu de perte voire aucune en cas de crash
- Portabilité 32bits et 64bits, compatible LE and BE architectures.
- Utilisable avec tous les langages de programmations (pas de problèmes de compatibilités)
- Pas de problèmes de rétro compatibilités.

SQLite désavantages : 
- Cependant en fonction du device, SQLite peut brider la taille de la BDD à seulement quelques GB.
- Http requests assez lentes

# Pourquoi PostGreSQL :

##Un peu d'histoire : 
Historiquement MySQL avait la réputation d'avoir une BDD extrêmement rapide pour une lecture incroyablement rapide mais au détriment d'un coût bien plus grand pour toutes les requêtes mixées avec des opérations d'écriture.

Postgres quant à lui était un peu plus modéré au niveau des performances, avec des lectures bien moins spectaculaires, cependant contrairement a MySQL il était capable d'écrire de très grands montants de données bien plus effiacement et de gérer la conccurence bien mieux.

## Aujourd'hui : 

Choisir MySQL ou PostgreSQL pour les performances n'a plus beaucoup de sens, les deux seront bons mais plutôt pour les features qui vont avec.

PostgreSQL est une BDD puremement relationnelle, et pour cela elle inclue l'héritable de table et la surchage. (Elle est également plus proche des standards SQL que MySQL)

## Point important : 
- Encore aujourd'hui Postgres gère mieux la conccurence que MySQL sans lock en lecture et peut créer des indexes en mode non bloquant en utilisant plusieurs cores CPU -> CREATE INDEX CONCURRENTLY.
- Les triggers et transactions sont très bien gérés en PostgreSQL, qui est connu pour garantir l'intégrité des données.
- En MySQL de sérieux bugs encore à ce jour sont connus en  ce qui concerne les triggers notamment.

### Prise en main et configuration : 
PostGreSQL est généralement bien plus effiace avec une installation par défaut que MySQL qui demande une configuration bien plus pointilleuse.

### Adaptabilité :
PostGreSQL peut supporter de nombreux type de données tel que (geometric/GIS, network address types, JSONB qui peuvent être indexés, ainsi que des UUID natives et des timestamps) qui ne sont pas disponibles en MySQL.

PostGreSQL est purement open-source et basée sur la communauté contrairement à MySQL qui comporte quelques problèmes de licences. (cependant il existe quelques fork open sources tel que MariaDB)

Cependant il est important de mentionner que même si PostGreSQL comporte de très nombreux avantages, il est vrai qu'il est moins populaire que MySQL et ce depuis des années, ce qui a eu, comme  conséquence de voir émerger beaucoup plus d'outils intermédiaires pour MySQL de gestion de BDD etc.

## Désavantage de PostGreSQL notable :
Pour chaque nouvelle connection de client, il alloue tout de même 10MB environ car il crée un nouveau processus.
# Django 
Django reste un paramètre essentiel dans le choix de la technologie.
En l'occurence il utilise SQLite par défaut, cependant MySQL et PostGreSQL sont tout à fait possible avec également.
## MongoDB 
Le couple python/mongoDB semble réputé pour les services Web mais à ce jour je ne me suis pas assez documenté sur cela.

Quelques features sur les stats serveurs sont baseline pour PostGreSQL ->

https://www.postgresql.org/docs/9.6/monitoring-stats.html

L'indexation du fulltext est possible en PostGreSQL -> 

https://www.postgresql.org/docs/9.5/textsearch.html

Egalement en MySQL, cependant cela utilise innodb, qui est une technologie récente pour supported la conccurence, triggers et transactions bien mieux qu'avant, mais en dépit de cela il perd de ses anciennes performances.

https://dev.mysql.com/doc/refman/5.6/en/innodb-fulltext-index.html
