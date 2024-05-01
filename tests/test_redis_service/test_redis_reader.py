import unittest
from app.redis_service.redis_reader import RedisReader
from unittest.mock import patch

class TestRedisReader(unittest.TestCase):
    def setUp(self):
        # Dados de teste para a função read_from_redis
        self.exrates_data = {"USD": "1.23", "EUR": "0.89", "GBP": "0.76"}

    @patch("app.redis_service.redis_reader.redis.StrictRedis")
    def test_read_from_redis(self, mock_redis):
        # Configurando o mock
        mock_redis_instance = mock_redis.return_value
        mock_redis_instance.hgetall.return_value = self.exrates_data

        # Instanciando o objeto RedisReader
        redis_reader = RedisReader("localhost", 6379, "password")

        # Chamando a função read_from_redis
        result = redis_reader.read_from_redis()

        # Verificando se os dados retornados correspondem aos dados fictícios
        self.assertEqual(result, self.exrates_data)

if __name__ == "__main__":
    unittest.main()
