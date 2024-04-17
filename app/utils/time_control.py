from datetime import datetime
import pytz

class TimeCtrl:
    @staticmethod
    def get_current_utc_time():
        # Obter a data e hora atual em UTC
        utc_now = datetime.now(pytz.utc)
        # Formatar a data e hora em UTC com o nome completo do fuso horário
        formatted_time = utc_now.strftime('%Y-%m-%d %H:%M:%S %Z')
        return formatted_time

