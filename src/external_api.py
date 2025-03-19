import requests
from dotenv import load_dotenv
import os

from src.utils import transactions

# Загрузка переменных из .env файла
load_dotenv()


def currency_conversion(transaction):
    """Принимает транзакцию и конвертирует из иностранной валюты в рубли с запросом на API сайт"""
    if "operationAmount" not in transaction:
        print("Ошибка: ключ 'operationAmount' отсутствует в транзакции")
        return 0.0

    amount = float(transaction["operationAmount"]["amount"]) # получение суммы транзакции
    currency = transaction["operationAmount"]["currency"]["code"] # получение валюты

    if currency != "RUB":
        apikey = os.getenv("API_KEY")

        if not apikey:
            print("Ошибка: API ключ не найден")
            return 0.0

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": f"{apikey}"}
        response = requests.get(url, headers=headers)
        response_data = response.json()

        # Отладочная информация
        print(f"Запрос: {url}")
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ: {response_data}")

        try:
            return round(response_data["result"], 2)
        except KeyError:
            print("Ошибка: ключ 'result' отсутствует в ответе API")
            return 0.0
    return amount

def process_all_transactions(transaction):
    """Обрабатывает все транзакции и возвращает список конвертируемых сумм в рублях"""
    converted_amounts = []
    for transaction in transactions:
        converted_amounts = currency_conversion(transaction)
        converted_amounts.append(converted_amounts)
    return converted_amounts

converted_results = process_all_transactions(transactions)
for result in converted_results:
    print(result)
