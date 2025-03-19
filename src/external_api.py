import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env файла
load_dotenv()


def currency_conversion(transaction):
    """Конвертирует сумму транзакций в рубли"""
    try:
        amount = float(transaction["operationAmount"]["amount"])  # получение суммы транзакции
        currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты

        if currency == "RUB":
            return amount

        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY не задан в .env")

        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"from": currency, "to": "RUB", "amount": amount}
        headers = {"apikey": api_key}

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return round(response.json()["result"], 2)

    except (KeyError, requests.RequestException, ValueError) as e:
        print(f"Ошибка конвертации: {e}")
        return 0.0
