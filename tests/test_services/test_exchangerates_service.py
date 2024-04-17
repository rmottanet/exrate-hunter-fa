import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

# test
from app.services.exchangerates_service import ExchangeRatesService

class TestExchangeRatesService(unittest.TestCase):
    @patch("app.services.exchangerates_service.fetch_data")
    def test_get_exchangerates_rates_data_success(self, mock_fetch_data):
        # Dados de exemplo retornados pela API de taxas de câmbio
        mock_data = """
        {
            "exchange_rates": {
                "USD": 1,
                "EUR": 0.8333,
                "GBP": 0.7222
            }
        }
        """
        # Configurando o retorno do mock da função fetch_data
        mock_fetch_data.return_value = mock_data

        # URL de exemplo da API de taxas de câmbio
        api_url = "https://example.com/exchangerates"
        api_key = "api_key"

        # Instanciando o objeto ExchangeRatesService e chamando a função get_exchangerates_rates_data
        exchange_rates_service = ExchangeRatesService()
        result = exchange_rates_service.get_exchangerates_rates_data(api_url, api_key)

        # Verificando se os dados foram obtidos e processados corretamente
        self.assertEqual(result, {
            "USD": 1,
            "EUR": 0.8333,
            "GBP": 0.7222
        })

    @patch("app.services.exchangerates_service.fetch_data")
    def test_get_exchangerates_rates_data_failure(self, mock_fetch_data):
        # Simulando uma exceção ao fazer a requisição
        mock_fetch_data.side_effect = Exception("API error")

        # URL de exemplo da API de taxas de câmbio
        api_url = "https://example.com/exchangerates"
        api_key = "api_key"

        # Instanciando o objeto ExchangeRatesService e chamando a função get_exchangerates_rates_data
        exchange_rates_service = ExchangeRatesService()

        # Verificando se a função retorna None em caso de falha
        result = exchange_rates_service.get_exchangerates_rates_data(api_url, api_key)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
