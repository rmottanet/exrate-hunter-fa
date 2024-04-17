import os
import sys
import unittest
from unittest.mock import patch

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app')))

# test
from app.services.bcb_service import BCBQuotesService

class TestBCBQuotesService(unittest.TestCase):
    @patch("app.services.bcb_service.fetch_data")
    def test_get_bcb_rates_data_success(self, mock_fetch_data):
        # Dados de exemplo retornados pela API do BCB
        mock_data = """
        {
            "conteudo": [
                {"moeda": "Dólar", "valorCompra": "5.0"},
                {"moeda": "Euro", "valorCompra": "6.0"}
            ]
        }
        """
        # Configurando o retorno do mock da função fetch_data
        mock_fetch_data.return_value = mock_data

        # URL de exemplo da API do BCB
        api_url = "https://example.com/bcb_quotes"

        # Instanciando o objeto BCBQuotesService e chamando a função get_bcb_rates_data
        bcb_service = BCBQuotesService()
        result = bcb_service.get_bcb_rates_data(api_url)

        # Verificando se os dados foram obtidos e processados corretamente
        self.assertEqual(result, {"USD": 1, "BRL": 5.0, "EUR": 0.8333})

    @patch("app.services.bcb_service.fetch_data")
    def test_get_bcb_rates_data_failure(self, mock_fetch_data):
        # Simulando uma exceção ao fazer a requisição
        mock_fetch_data.side_effect = Exception("API error")

        # URL de exemplo da API do BCB
        api_url = "https://example.com/bcb_quotes"

        # Instanciando o objeto BCBQuotesService e chamando a função get_bcb_rates_data
        bcb_service = BCBQuotesService()

        # Verificando se a função retorna None em caso de falha
        result = bcb_service.get_bcb_rates_data(api_url)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
