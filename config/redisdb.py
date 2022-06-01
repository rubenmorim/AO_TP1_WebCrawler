import redis


redificio = redis.StrictRedis(
   host='127.0.0.1',
   port=6379,
   password='',
   db=1,
   charset="utf-8",
   decode_responses=True
)

rlocalizacao = redis.StrictRedis(
   host='127.0.0.1',
   port=6379,
   password='',
   db=2,
   charset="utf-8",
   decode_responses=True
)

rvendedor = redis.StrictRedis(
   host='127.0.0.1',
   port=6379,
   password='',
   db=3,
   charset="utf-8",
   decode_responses=True
)



