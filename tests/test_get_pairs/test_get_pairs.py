import requests
from project_crypto_reader.KrakenAPIConnector import KrakenAPIConnector


def test_get_pairs(monkeypatch):
    """
        DADO un metodo que obtiene los pares disponibles en Kraken
        CUANDO se ejecuta la llamada a la api
        THEN se retorna una lista de pares de criptomoniedas que contiene BTC/USD
    """
    import json

    with open('mocks/pairs.json', 'r') as f:
        mock_pares = json.load(f)

    # Output: {'error': [], 'result': {'1INCHEUR':{...}}}
    print(mock_pares)

    class MockResponse:

        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse(mock_pares)
    )

    kraken = KrakenAPIConnector()
    pares_disponibles = kraken.get_pairs()
    assert 'XBT/USD' in pares_disponibles
