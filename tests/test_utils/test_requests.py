import unittest
from unittest.mock import patch
import requests
from app.utils.requests import fetch_data


class TestFetchData(unittest.TestCase):
    @patch('app.utils.requests.requests.get')
    def test_fetch_data_failure(self, mock_get):
        # Simular uma exceção ao fazer a requisição
        mock_get.side_effect = requests.exceptions.HTTPError()

        # URL de exemplo
        url = 'https://example.com/data'

        # Verificar se a função lança uma exceção em caso de falha na requisição
        with self.assertRaises(RuntimeError):
            fetch_data(url)

if __name__ == '__main__':
    unittest.main()
