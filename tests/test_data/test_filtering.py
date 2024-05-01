import unittest
from app.data.filtering import DataFilter

class TestDataFilter(unittest.TestCase):
    def test_filter(self):
        # Dados de entrada no mesmo formato que os dados retornados do Redis
        data = {
            b'USD': b'1.23',
            b'EUR': b'0.89',
            b'GBP': b'0.76',
            b'DATA_BASE': b'2024-04-17 12:00:00 UTC',
            b'OTHER_KEY': b'OTHER_VALUE'
        }

        # Instanciar a classe DataFilter com os dados de entrada
        data_filter = DataFilter(data)

        # Executar o método filter() e verificar se os dados foram filtrados corretamente
        filtered_data = data_filter.filter()

        # Verificar se as chaves 'USD', 'EUR', 'GBP' e 'DATA_BASE' estão presentes no resultado
        self.assertIn('USD', filtered_data)
        self.assertIn('EUR', filtered_data)
        self.assertIn('GBP', filtered_data)
        self.assertIn('DATA_BASE', filtered_data)

if __name__ == "__main__":
    unittest.main()
