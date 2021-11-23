from project_crypto_reader.CotizacionCripto import CotizacionCripto
from datetime import datetime
import pandas as pd


def test_get_pairs(monkeypatch):
    """
        DADO un metodo que obtiene los pares disponibles en Kraken
        CUANDO se ejecuta la llamada a la api
        THEN se retorna una lista de pares de criptomoniedas que contiene BTC/USD
    """

    fecha_inicio_dt = datetime.strptime("25-08-2021", "%d-%m-%Y")
    par_cripto = CotizacionCripto("XBT/USD", "Diario", fecha_inicio_dt, 10)
    data_crypto = par_cripto.obtener_cotizacion()

    assert isinstance(data_crypto, pd.DataFrame)
