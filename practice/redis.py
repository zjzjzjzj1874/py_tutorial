import redis

print(dir(redis))
# redis配置
REDIS_HOST = "localhost"


# 调用redis的hset方法
def hSet_redis(name, data):
    rd = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)
    rd.hset(name, "key", data)


hSet_redis("hset_key", "field value")
