import redis

r = redis.StrictRedis(
   host='127.0.0.1',
   port=6379,
   password='',
   charset="utf-8",
   decode_responses=True
)



