import redis


class RedisWriter:
    def __init__(self, host, port, password):
        self.redis_client = redis.StrictRedis(host=host, port=port, password=password)

    def write_to_redis(self, exchange_rates):
        try:
            # Open connection
            with self.redis_client.pipeline() as pipe:
                # Adicionar todas as operações ao pipeline para execução atômica
                pipe.hmset("exrates", exchange_rates)
                pipe.execute()
        except Exception as e:
            raise e
