# Specification matérielle

* les VMs de la plate-forme PL tournent en environnement **virtualisé** sur des serveurs DELL (PowerEdge R640), faisant tourner un système **Proxmox**

* À ce jour, ces VMs sont configurées comme suit :

## Prod

Servers de production disponibles directement sur le web.

|          |PL (frontend)                            |SANDBOX                                                 |
|----------|-----------------------------------------|--------------------------------------------------------|
|CPU       |2                                        |4                                                       |
|MEM       |2 Go                                     |8 Go                                                    |
|DISK      |10 Go, 1 seule partition (utilisée à 64%)|10 Go (système, 43% utilisé) + 20 Go (data, 18% utilisé)|
|NET       |1 lien réseau 1 Gbps                     |1 lien réseau Gbps                                      |
|OS        |debian (version 10.1 "buster")           |debian (version 10.1 "buster")                          |
|SOFT      |Apache / Python / Django / PostgreSQL    |Apache / Python / Django / docker                       |


## Pre-Prod

Serveur permettant de tester la plateforme dans les mêmes conditions que sur **Prod**.
Accessible depuis le web.

|          |PL (frontend) + SANDBOX                                 |
|----------|--------------------------------------------------------|
|CPU       |2                                                       |
|MEM       |4 Go                                                    |
|DISK      |10 Go (système, 88% utilisé) + 20 Go (data, 57% utilisé)|
|NET       |1 lien réseau 1 Gbps                                    |
|OS        |debian (version 10.1 "buster")                          |
|SOFT      |Apache / Python / Django / PostgreSQL / docker          |

## Test

Serveurs permettant aux devs d'effectuer divers tests nécessitant un serveur live. Accessible seulement depuis *eduroam*.

|          |PL (frontend x4) + SANDBOX                             |
|----------|-------------------------------------------------------|
|CPU       |2                                                      |
|MEM       |4 Go                                                   |
|DISK      |10 Go (système, 76% utilisé) + 20 Go (data, 6% utilisé)|
|NET       |1 lien réseau 1 Gbps                                   |
|OS        |debian (version 10.1 "buster")                         |
|SOFT      |Apache / Python / Django / PostgreSQL / docker         |
