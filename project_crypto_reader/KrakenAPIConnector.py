import requests

import krakenex
from pykrakenapi import KrakenAPI


class KrakenAPIConnector(object):
    """
   Singleton de conexion a la API de Kraken
   """
    __instance = None
    api = KrakenAPI(krakenex.API())
    pares = []
    pares_json = []
    intervalo_velas = {"15 min": 15, "30 min": 30, "Hora": 60, "Diario": 1440, "Semanal": 10080}

    def __str__(self):
        return 'Singleton de conexión a la API de Kraken'

    def __new__(cls):
        if KrakenAPIConnector.__instance is None:
            KrakenAPIConnector.__instance = object.__new__(cls)
        return KrakenAPIConnector.__instance

    def get_pairs(self):
        try:
            response = requests.get("https://api.kraken.com/0/public/AssetPairs")
            pares_json = response.json()['result']
            self.pares_json = pares_json
            self.pares = [pares_json[key]['wsname'] for key in pares_json.keys()]
        except KeyError:
            print("No se puede acceder a los pares disponibles")

        finally:
            return self.pares
