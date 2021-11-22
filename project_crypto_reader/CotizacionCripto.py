import pandas as pd
from KrakenAPIConnector import KrakenAPIConnector
from ta.volume import VolumeWeightedAveragePrice


class CotizacionCripto:
    """
   Estuctura de datos de cotización de criptomoneda
   """

    def __init__(self, par, intervalo, desde, intervalo_vwap=10):
        self.par = par
        self.intervalo = intervalo
        self.desde = desde
        self.intervalo_vwap = intervalo_vwap
        self.altname = None
        self.base = None

    def __call__(self):
        print(f"{self.par} desde {self.desde}")

    def __str__(self):
        print(f"{self.par} desde {self.desde}")

    def __calcular_vwap(self, dataframe):
        dataframe["indicador_vwap"] = VolumeWeightedAveragePrice(high=dataframe['high'], low=dataframe['low'],
                                                                 close=dataframe["close"], volume=dataframe['volume'],
                                                                 window=self.intervalo_vwap,
                                                                 fillna=True).volume_weighted_average_price()
        return dataframe

    def obtener_cotizacion(self):
        print("obteniendo cotización de " + self.par)
        kraken = KrakenAPIConnector()
        # obtenemos la divisa base del par seleccionado
        critpto_seleccionada = [value for key, value in kraken.pares_json.items() if value['wsname'] == self.par]
        self.base = critpto_seleccionada[0]['quote'][1:]
        self.altname = critpto_seleccionada[0]["altname"]
        print(int(self.desde.timestamp()))
        crypto_response, last = kraken.api.get_ohlc_data(self.altname, interval=kraken.intervalo_velas[self.intervalo],
                                                         since=int(self.desde.timestamp()), ascending=True)

        # Creamos el dataset
        data_crypto = pd.DataFrame(crypto_response)
        # calculamos el date con formato
        data_crypto['date'] = pd.to_datetime(data_crypto.index).date

        # calculamos el vwap
        # vwap: Suma [ordenes*precio promedio]/ volumen
        self.__calcular_vwap(data_crypto)

        return data_crypto
