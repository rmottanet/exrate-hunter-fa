import json
import logging
from urllib.parse import urlencode
from app.utils.requests import fetch_data


class ExchangeRatesService:
    @staticmethod
    def get_exchangerates_rates_data(api_url, api_key):
        try:
            # exrates params
            params = urlencode({
                "api_key": api_key,
                "base": "USD"
            })

            full_url = f"{api_url}?{params}"
            
            data = fetch_data(full_url)
            
            exchange_rates_data = json.loads(data)
            
            logging.info("ExchangeRates retrieved")
            
            return exchange_rates_data.get("exchange_rates")

        except Exception as e:
            logging.error(f"Failed to fetch exchange rates data: {str(e)}")
            return None
