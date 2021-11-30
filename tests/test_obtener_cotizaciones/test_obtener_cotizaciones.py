from project_crypto_reader.CotizacionCripto import CotizacionCripto
from datetime import datetime
import pandas as pd


def test_obtener_cotizaciones(monkeypatch):
    """
        DADO un metodo que devuelve la cotizacion de una criptomoneda en un periodo seleccionado
        CUANDO se ejecuta la llamada a la api
        LUEGO se retorna una DataFrame de pandas con los precios de la criptomoneda en un intervalo
    """

    fecha_inicio_dt = datetime.strptime("25-08-2021", "%d-%m-%Y")
    par_cripto = CotizacionCripto("XBT/USD", "Diario", fecha_inicio_dt, 10)
    data_crypto = par_cripto.obtener_cotizacion()

    assert isinstance(data_crypto, pd.DataFrame)
