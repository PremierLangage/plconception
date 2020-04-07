# Sandbox

La sandbox est l'environment dans lequel les exercices sont exécutés. Celle-ci doit permettre d'exécuter du code non vérifiée de manière sécurisé.

Les deux choix principaux *jail* et *docker*.

Jail permet d'exécuter du code directement sur un système, tout en limitant des accès système spécifiques (network, I/O, ...). Le problème est que si le code arrive, par quelque moyen que ce soit, à crasher le serveur, l'ensemble des utilisateurs sont impactés.

Docker permet quand à lui de lancer un système virtuel indépendant dans lequel le code sera exécuté. Tout en offrant la de limiter certains accès, de plus, tout problème sur le container docker lancé se limitera à ce container et n'affectera pas les autres utilisateurs.

Nous avons donc opté pour Docker : un pool de container est lancé, et lorsqu'une requête arrive, un container disponible est choisi pour exécuter le code.
