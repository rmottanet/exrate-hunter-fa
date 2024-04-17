import unittest
from unittest.mock import MagicMock, patch
from app.redis_service.redis_writer import RedisWriter

class TestRedisWriter(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.redis_writer = RedisWriter("localhost", 6379, "password")

    @patch("app.redis_service.redis_writer.redis.StrictRedis")
    def test_write_to_redis(self, mock_redis):
        # Dados de teste para a função write_to_redis
        exchange_rates = {"USD": 1.23, "EUR": 0.89, "GBP": 0.76}

        # Simulando o objeto pipeline
        mock_pipeline = MagicMock()
        mock_redis.return_value.pipeline.return_value = mock_pipeline
        mock_pipeline.execute.side_effect = Exception("Error writing to Redis")

        # Chamando a função write_to_redis e verificando se a exceção é levantada
        with self.assertRaises(Exception) as context:
            self.redis_writer.write_to_redis(exchange_rates)

if __name__ == "__main__":
    unittest.main()
