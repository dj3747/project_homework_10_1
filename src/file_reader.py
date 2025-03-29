import logging
import os

import pandas as pd

logger = logging.getLogger("CSV_Excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/Serg/PycharmProjects/project_homework_10_1/logs/file_reader.log", "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv(file_path):
    """Считывает данные из csv и возвращает в формате словаря"""
    try:
        df = pd.read_csv(file_path, sep=";")
        return df.to_dict("records")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []


transaction = read_csv("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/transactions.csv")


def read_exel(filename):
    """Функция считывает информацию из Exel файла и выдаёт
    список словарей с транзакциями"""
    if not os.path.exists(filename):
        logger.error("Файл не найден")
        return []  # В случае ошибки возвращает пустой список
    logger.info("Начало загрузки Exel файла")
    reading_exel = pd.read_excel(filename)
    # Конвертируем DataFrame в список
    transactions_list = reading_exel.to_dict("records")
    logger.info("Окончание загрузки Exel файла")
    return transactions_list


operation_exel = read_exel("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/transactions_excel.xlsx")
