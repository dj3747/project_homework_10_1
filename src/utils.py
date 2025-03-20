import json
import os
import logging


logger = logging.getLogger("utils")
file_handler = logging.FileHandler(
    'C:/Users/Serg/PycharmProjects/project_homework_10_1/logs/utils.log',
    'w', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_financial_transactions(path):
    """Принимает путь до JSON файла и возвращает список словарей
    с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        logger.error("Файл не найден")
        return []
    logger.info("Начало загрузки JSON файла")
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transactions("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/operations.json")

print(transactions)
