from unittest.mock import patch

import requests

from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion_rub(mock_get):
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "RUB"}}}
    assert currency_conversion(transaction) == 100.0


@patch("requests.get")
def test_currency_conversion_usd(mock_get):
    mock_response = {"result": 7500.0}
    mock_get.return_value.json.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}

    assert currency_conversion(transaction) == 7500.0


@patch.dict("os.environ", {"API_KEY": "test"})
@patch("requests.get")
def test_api_error_handling(mock_get):
    mock_get.side_effect = requests.RequestException("API error")

    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}

    assert currency_conversion(transaction) == 0.0
