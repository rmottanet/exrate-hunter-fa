class DataFilter:
    def __init__(self, data):
        self.data = data

    def filter(self):
        filtered_data = {}
        # Iterar sobre as chaves e valores dos dados
        for key, value in self.data.items():
            # Verificar se a chave possui 3 letras ou se é "DATA_BASE"
            if len(key) == 3 or key == b"DATA_BASE":
                filtered_data[key.decode("utf-8")] = value.decode("utf-8")
        return filtered_data
