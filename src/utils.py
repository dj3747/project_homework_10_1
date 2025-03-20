import json
import os


def get_financial_transactions(path):
    """Принимает путь до JSON файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transactions("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/operations.json")

print(transactions)
