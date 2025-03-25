import csv

import pandas as pd


def read_csv(filename):
    """Принимает путь к файлу, считывает информацию из CSV файла"""
    with open(filename, encoding="utf-8") as file:
        reading_csv = csv.DictReader(file, delimiter=";")
        reading = [row for row in reading_csv]
        return reading


transaction = read_csv("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/transactions.csv")
print(transaction)


def read_exel(filename):
    """Функция считывает информацию из Exel файла и выдаёт
    список словарей с транзакциями"""
    reading_exel = pd.read_excel(filename)
    # Конвертируем DataFrame в список
    transactions_list = reading_exel.to_dict(orient="records")
    return transactions_list


operation_exel = read_exel("C:/Users/Serg/PycharmProjects/project_homework_10_1/data/transactions_excel.xlsx")
print(operation_exel)
