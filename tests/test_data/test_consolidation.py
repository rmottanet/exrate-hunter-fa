import unittest
from app.data.consolidation import DataConsolidator

class TestDataConsolidator(unittest.TestCase):
    def setUp(self):
        # Dados de teste para os serviços
        self.service_1_data = {"USD": 1.0, "EUR": 0.8, "GBP": 0.7}
        self.service_2_data = {"USD": 1.1, "JPY": 110.0}
        self.service_3_data = {"EUR": 0.85, "GBP": 0.72, "AUD": 1.3}

    def test_consolidate(self):
        # Instanciar o objeto DataConsolidator
        consolidator = DataConsolidator(self.service_1_data, self.service_2_data, self.service_3_data)

        # Executar a função consolidate
        consolidated_data = consolidator.consolidate()

        # Criar um dicionário de referência excluindo a chave 'data_base'
        reference_data = {
            "USD": 1.0,  # Prioridade no serviço 1
            "EUR": 0.8,  # Prioridade no serviço 1
            "GBP": 0.7,  # Prioridade no serviço 1
            "JPY": 110.0,  # Prioridade no serviço 2
            "AUD": 1.3  # Prioridade no serviço 3
        }

        # Verificar se os dados consolidados estão corretos
        self.assertDictEqual(
            {key: value for key, value in consolidated_data.items() if key != 'DATA_BASE'},
            {key: value for key, value in reference_data.items() if key != 'DATA_BASE'}
        )

if __name__ == "__main__":
    unittest.main()
