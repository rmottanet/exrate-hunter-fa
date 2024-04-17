import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

# test
from app.services.openexchange_service import OpenExchangeService

class TestOpenExchangeService(unittest.TestCase):
    @patch("app.services.openexchange_service.fetch_data")
    def test_get_openexchange_rates_data_success(self, mock_fetch_data):
        # Dados de exemplo retornados pela API do OpenExchangeRates
        mock_data = '{"rates": {"USD": 1, "EUR": 0.83}}'

        # Configurando o retorno do mock da função fetch_data
        mock_fetch_data.return_value = mock_data

        # URL de exemplo da API do OpenExchangeRates
        api_url = "https://example.com/openexchange_quotes"
        api_key = "12345"

        # Instanciando o objeto OpenExchangeService e chamando a função get_openexchange_rates_data
        openexchange_service = OpenExchangeService()
        result = openexchange_service.get_openexchange_rates_data(api_url, api_key)

        # Verificando se os dados foram obtidos e processados corretamente
        self.assertEqual(result, {"USD": 1, "EUR": 0.83})

    @patch("app.services.openexchange_service.fetch_data")
    def test_get_openexchange_rates_data_failure(self, mock_fetch_data):
        # Simulando uma falha na obtenção dos dados da API
        mock_fetch_data.side_effect = Exception("API error")

        # URL de exemplo da API do OpenExchangeRates
        api_url = "https://example.com/openexchange_quotes"
        api_key = "12345"

        # Instanciando o objeto OpenExchangeService e chamando a função get_openexchange_rates_data
        openexchange_service = OpenExchangeService()
        result = openexchange_service.get_openexchange_rates_data(api_url, api_key)

        # Verificando se a função retorna None em caso de falha
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
