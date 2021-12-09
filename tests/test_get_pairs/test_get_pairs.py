import pytest
import requests
from project_crypto_reader.KrakenAPIConnector import KrakenAPIConnector
import json


def test_get_pairs(monkeypatch):
    """
        DADO un metodo que obtiene los pares disponibles en Kraken
        CUANDO se ejecuta la llamada a la api
        THEN se retorna una lista de pares de criptomoniedas que contiene BTC/USD
    """

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


def test_get_pairs_error(monkeypatch):
    """
        DADO un metodo que obtiene los pares disponibles en Kraken
        CUANDO se ejecuta la llamada a la api
        LUEGO se retorna una lista de pares de criptomoniedas que contiene BTC/USD
    """

    with open('mocks/pairs_error.json', 'r') as f:
        mock_error = json.load(f)

    # Output: {'error': [...]}}
    print(mock_error)
    class MockResponse:

        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse(mock_error)
    )

    try:
        kraken = KrakenAPIConnector()
        kraken.get_pairs()
    except KeyError as e:
        print(e)
        pytest.fail(e)


