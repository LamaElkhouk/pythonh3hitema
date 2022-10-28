1)redis

redis est un outil qui permet de sauvegarder les informations sous forme de clef valeur , qui seront stoker dans la memoire et ainsi pouvoir les recuperer rapidement

est utiliser pour gerer des session utilisateur

lancer redis : redis-server

pour interagir avec redis en ligne de commandes :
redis-cli

recuperer une valeur  (string)
SET clef value
>> ok
GET clef
>>value

pour supprimer une valeur
DEL clef
>> 1

pour incrementer une valeur  (integer)
SET clef 0
>>ok
INCR clef
>>1
INCRE clef
>>2

TTL clef renvoit -1 si c'est une clef permanente sinon revoit la dureé en seconde de sa durabilité
EXPIRE clef pour definir une durée a une clefs

operation sur les listes

RPUSH liste "ele1"
(integer) 1
127.0.0.1:6379> LPUSH liste "ele2"
(integer) 2
127.0.0.1:6379> LPUSH liste "ele3"
(integer) 3
127.0.0.1:6379> LRANGE liste 0 -1     (on ne fait pas d'operation GET sur les listes)
1) "ele3"
2) "ele2"
3) "ele1"

LLEN liste pour recuperer la taille de la liste

LPOP supprime le premiere element de la liste RPOP supprime le derniere element

liste particuliere qui s'appel "sets", ne comprend que des clefs unique:

SADD users "user1"
SADD users "user2"
SADD users "user1"  => renvoit une erreur

SMEMBERS users => renvoit la liste
SREM users "user1" => supprime l'utilisateur

SISMEMBER users "user2"=> renvoit si oui ou non l'utilisateur est dans la liste

SUNION users users2 pour fusionner les deux listes

autres operation :ZADD ZRANGE ZREVRANGE ZREM ZRANGE pour ajouter un score par exemple aux utilisateurs

sauvegarder plusieurs informations en meme temps :

127.0.0.1:6379> HMSET user:1 username "MARIE" age 20 email maria@gmail.com
OK
127.0.0.1:6379> HGETALL user:1
1) "username"
2) "MARIE"
3) "age"
4) "20"
5) "email"
6) "maria@gmail.com"
127.0.0.1:6379> HGET user:1 age
"20"

la commande redis-cli nous connecte directement sur la base de données 0

KEYS *

SELECT 1  pour acceder a la base de données 1 

2)DOCKER COMPOSE = regroupe plusieurs containeur
un fichier sous forme " docker-compose.yml "

docker-compose build
docker-compose up -d (build et run )
docker-compose ps : pour avoir l'etat des services
docker compose start
docker-compose pull :met a jour les images


dans le fichier docker-compose.yml

version :'' #version du docker compose
services:   #ensemble de containeur
 myfirstservice:
  image: NomImage
  restart: always
  container_name:NomContaineur
  entrypoint: commande que l'on souhaite executer

microservices? application independantes qui communiquent