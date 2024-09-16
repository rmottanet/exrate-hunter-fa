import logging
from typing import Dict
from app.utils.time_control import TimeCtrl


class DataConsolidator:
    """
    This class consolidates data from multiple external services.

    It takes the data from three services as dictionaries and combines them
    into a single dictionary with priority given to the services in the order
    they are provided.  Duplicate currencies will be populated with the value
    from the last service that provided a value for that currency.

    **Attributes:**

    * services (list): A list containing dictionaries of data from each service.

    **Methods:**

    * consolidate() -> Dict[str, float]: Consolidates data from all services
        and returns a single dictionary containing the combined results.
    """

    def __init__(self, service_1_data: Dict[str, float], service_2_data: Dict[str, float], service_3_data: Dict[str, float]):
        """
        Initializes the DataConsolidator with data from three services.

        **Args:**

        * service_1_data (Dict[str, float]): Dictionary containing data from service 1.
        * service_2_data (Dict[str, float]): Dictionary containing data from service 2.
        * service_3_data (Dict[str, float]): Dictionary containing data from service 3.
        """
        self.services = [service_1_data, service_2_data, service_3_data]

    def consolidate(self) -> Dict[str, float]:
        """
        Consolidates data from all services and returns a single dictionary.

        This method iterates over the data from each service and combines them
        into a single dictionary.  If a currency exists in multiple services,
        the value from the last service encountered will be used.

        **Returns:**

        * Dict[str, float]: A dictionary containing the consolidated data.
            The dictionary key is the currency code and the value is the
            corresponding exchange rate.
        """

        consolidated_data = {'DATA_BASE': TimeCtrl.get_current_utc_time()}

        for service_data in self.services:
            if isinstance(service_data, dict):
                for currency, value in service_data.items():
                    if currency not in consolidated_data:
                        consolidated_data[currency] = value

        return consolidated_data
