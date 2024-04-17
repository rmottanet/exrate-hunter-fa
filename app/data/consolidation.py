import logging
from typing import Dict
from app.utils.time_control import TimeCtrl

class DataConsolidator:
    def __init__(self, service_1_data: Dict[str, float], service_2_data: Dict[str, float], service_3_data: Dict[str, float]):
        self.service_1_data = service_1_data
        self.service_2_data = service_2_data
        self.service_3_data = service_3_data

    def consolidate(self) -> Dict[str, float]:
        consolidated_data = {}

        # Função para verificar se uma moeda tem uma resposta não vazia em algum dos serviços
        def has_non_empty_response(currency):
            return any(data.get(currency) for data in [self.service_1_data, self.service_2_data, self.service_3_data])

        # Inserir a chave 'data_base' no início do dicionário consolidado
        consolidated_data['DATA_BASE'] = TimeCtrl.get_current_utc_time()
        
        # Atualiza os dados consolidados por prioridade
        for currency in set(self.service_1_data.keys()) | set(self.service_2_data.keys()) | set(self.service_3_data.keys()):
            if has_non_empty_response(currency):
                if currency in self.service_1_data:
                    consolidated_data[currency] = self.service_1_data[currency]
                elif currency in self.service_2_data:
                    consolidated_data[currency] = self.service_2_data[currency]
                elif currency in self.service_3_data:
                    consolidated_data[currency] = self.service_3_data[currency]
                else:
                    logging.warning(f"Nenhuma resposta válida encontrada para {currency}")

        return consolidated_data

