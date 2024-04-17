import os

class Config:
    # Security token
    COINSNARK_TOKEN = os.getenv("COINSNARK_TOKEN")
    
    # Configurações do Redis
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    REDIS_KEY = os.getenv("REDIS_KEY")
    
    # Configurações das APIs externas
    BCBQUOTES_API_URL = "https://www.bcb.gov.br/api/servico/sitebcb/indicadorCambio"
    
    EXCHANGE_RATES_API_URL = "https://exchange-rates.abstractapi.com/v1/live/"
    EXCHANGE_RATES_API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
    
    OPEN_EXCHANGE_API_URL = "https://openexchangerates.org/api/latest.json"
    OPEN_EXCHANGE_API_KEY = os.getenv("OPEN_EXCHANGE_API_KEY")
