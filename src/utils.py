import json
import os


def get_financial_transaction(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transaction("C:\Users\Serg\PycharmProjects\project_homework_10_1\data\operations.json")

print(transactions)
