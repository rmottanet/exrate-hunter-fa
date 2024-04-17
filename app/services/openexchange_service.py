import json
import logging
from urllib.parse import urlencode
from app.utils.requests import fetch_data


class OpenExchangeService:
    @staticmethod
    def get_openexchange_rates_data(api_url, api_key):
        try:
            # open exchange params
            params = urlencode({
                "app_id": api_key,
                "base": "usd",
                "prettyprint": "false",
                "show_alternative": "true"
            })

            full_url = f"{api_url}?{params}"
            
            data = fetch_data(full_url)
            
            exchange_rates_data = json.loads(data)
            
            logging.info("OpenExchangeRates retrieved")
            
            return exchange_rates_data.get("rates")
            
        except Exception as e:
            logging.error(f"Failed to retrieve OpenExchange rates: {e}")
            return None
