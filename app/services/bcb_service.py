import json
import logging
from app.utils.requests import fetch_data


class BCBQuotesService:
    @staticmethod
    def get_bcb_rates_data(api_url):
        try:
            data = fetch_data(api_url)
            
            bcb_rates_data = json.loads(data)
            currency_rates = {}

            # Get buy price
            for item in bcb_rates_data["conteudo"]:
                currency_name = item["moeda"]
                currency_buy_value = float(item["valorCompra"])
                
                currency_rates[currency_name] = currency_buy_value

            # BRL rate
            usd_to_brl = currency_rates["Dólar"]

            # Determine EUR rate
            brl_to_eur = 1 / currency_rates["Euro"]
            usd_to_eur = usd_to_brl * brl_to_eur

            logging.info("BCB Quotes retrieved")
            
            return {"USD": 1, "BRL": usd_to_brl, "EUR": round(usd_to_eur, 4)}
            
        except Exception as e:
            logging.error(f"Failed to retrieve BCB Quotes: {str(e)}")
            return None
