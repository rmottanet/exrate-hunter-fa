import redis
import os

class RedisReader:
    def __init__(self, host, port, password):
        self.redis_client = redis.StrictRedis(host=host, port=port, password=password)

    def read_from_redis(self):
        try:
            # Ler os dados da hash "exrates"
            exrates_data = self.redis_client.hgetall("exrates")
            return exrates_data
        except Exception as e:
            raise RuntimeError(f"Error reading from Redis: {e}")
