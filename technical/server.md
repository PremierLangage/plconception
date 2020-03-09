# Logiciels Server 

## NGINX

NGINX un serveur HTTP, c'est un système asynchrone par opposition aux serveurs synchrones où chaque requête est traitée par un processus dédié. Au lieu d'exploiter une architecture parallèle et un multiplexage temporel des tâches par le système d'exploitation, NGINX utilise les changements d'état pour gérer plusieurs connexions en même temps ; le traitement de chaque requête est découpé en de nombreuses mini-tâches et permet ainsi de réaliser un multiplexage efficace entre les connexions. Afin de tirer parti des ordinateurs multiprocesseurs, plusieurs processus peuvent être démarrés. Ce choix d'architecture se traduit par des performances très élevées, mais également par une charge et une consommation de mémoire particulièrement faibles comparativement aux serveurs HTTP classiques, tels qu'Apache. 

Utilisé NGINX nous permettra donc d'implémenter les WebSockets, nous permettant des mises-à-jour constantes des données affiché à l'utilisateur (ressources, activités en temps réel, notifications...).


## Daphne

Daphne est une surcouche de NGINX permettant d''utiliser les protocole HTTP, HTTP2, grâce à [ASGI](https://github.com/django/asgiref/blob/master/specs/asgi.rst) et [ASGI-HTTP](https://github.com/django/asgiref/blob/master/specs/www.rst).

Il supporte la négotiation automatique de protocole ; il n'y a pas besoin de préfixer les URL avec le bon protocole pour différencier les requête HTTP et WebSocket (`https://` / `ws://`).

## Django

Framework principal utilisé pour développer PLaTon. C'est un framework Python permettant de faire du web grâce à un système de gestions d'url par expressions régulières, une gestion de la base de données avec des modèles écrits en Python et un système de migrations.


## Django Channels

C'est un module Python permettant d'implémenter des échanges utilisant le protocole websocket (et d'autres protocoles) en ajoutant une couche asynchrone sous Django permettant d'écrire toujours du synchrone (vues http, fonctionement normal de Django) et qui permet également des échanges asynchrones.
Nous aurons besoins d'utiliser des websockets pour des mises-à-jour asynchrones de nos pages webs, par exemple pour notre système de notifications, ou pour une activité ayant des besoins en temps réels, sans devoir attendre une requete HTTP.
