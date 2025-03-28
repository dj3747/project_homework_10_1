import json
import os
import re
from collections import Counter

import pandas as pd
from pandas import read_excel

from src.file_reader import read_csv
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, filtered_list, sort_by_date, sorted_list
from src.widget import get_date, mask_account_card


def read_file_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_transactions_by_description(transactions, search_string):
    """Функция для поиска операций по заданной строку в описании"""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions):
    """Функция для подсчёта количества операций по категориям"""
    categories = [transaction["description"] for transaction in transactions]
    return dict(Counter(categories))


def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по коду валюты для CSV/Excel и JSON"""
    filtered = []
    target_currency = currency_code.upper()
    for transaction in transactions:
        # Для JSON: operationAmount -> currency -> code
        currency_json = transaction.get("operationAmount", {}).get("currency", {}).get("code", "").upper()
        # Для CSV/XLSX: currency_code
        currency_csv = str(transaction.get("currency_code", "")).upper()
        if currency_json.upper() == target_currency or currency_csv == target_currency:
            filtered.append(transaction)
    return filtered

def get_currency(transaction):
    """Возвращает код валюты для JSON/CSV/XLSX данных"""
    if "currency_code" in transaction:
        return transaction.get("currency_code", "не указана")
    if "operationAmount" in transaction:
        return transaction["operationAmount"].get("currency", {}).get("code", "не указана")
    return "не указана"


def get_amount(transaction):
    """Функция для получения суммы транзакции независимо от структуры данных"""
    amount_keys = [["operationAmount", "amount"], ["amount"], ["value"], ["transactionAmount", "value"]]
    for keys in amount_keys:
        value = transaction
        try:
            for key in keys:
                value = value[key]
            return value if value else "не указана"
        except (KeyError, TypeError):
            continue
    return "не указана"


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию из XLSX-файла")

    work_file = input("Ваш выбор: ").strip()

    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            read_file = read_file_json(os.path.join(os.path.dirname(__file__), "data/operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            read_file = read_csv(os.path.join(os.path.dirname(__file__), "data/transactions.csv"))
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            df = read_excel(os.path.join(os.path.dirname(__file__), "data/transactions_excel.xlsx"))
            read_file = df.to_dict('records')
            break
        else:
            work_file = input("Данного варианта нет в списке, попробуйте ещё раз:\nВаш выбор:").strip()

    status_operation = (
        input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:\nВвод: "
        )
        .strip()
        .upper()
    )

    while True:
        if status_operation in {"EXECUTED", "CANCELED", "PENDING"}:
            status_operation_filter = filter_by_state(read_file, status_operation)
            break
        else:
            status_operation = (
                input(
                    f"Статус {status_operation} не доступен. \n"
                    "\nВведите статус, по которому необходимо выполнить фильтрацию"
                    "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: \nВвод: "
                )
                .strip()
                .upper()
            )
    # print(f"Транзакций после фильтрации по статусу EXECUTED: {len(status_operation_filter)}")
    # print("Пример транзакции:", status_operation_filter[0] if status_operation_filter else "Нет данных")

    while True:
        question_sort_data = input("Отсортировать операции по дате? Да/Нет \nВаш выбор: ").lower()
        if question_sort_data == "да":
            question_sort_data_reverse = (
                input("Отсортировать по возрастанию или по убыванию?\nВаш выбор: ").strip().lower()
            )
            reverse = question_sort_data_reverse == "по убыванию"
            status_operation_filter.sort(key=lambda t: t.get("date", ""), reverse=reverse)
            break
        elif question_sort_data == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте ещё раз:")

    while True:
        question_currency = input("Выводить транзакции по определенной валюте? Да/Нет\nВаш выбор: ").lower()
        if question_currency == "да":
            currency_code = input("Введите код валюты (например, RUB, USD): ").strip().upper()
            status_operation_filter = filter_by_currency(status_operation_filter, currency_code)
            break
        elif question_currency == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте ещё раз:")

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВаш выбор: "
        ).lower()
        if question_description == "да":
            search_string = input("Введите строку поиска: ").strip()
            finaly_filter = search_transactions_by_description(status_operation_filter, search_string)
            break
        elif question_description == "нет":
            finaly_filter = status_operation_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте ещё раз:")

    print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(finaly_filter)}\n")
    if finaly_filter:
        for trans in finaly_filter:
            amount = get_amount(trans)
            currency = get_currency(trans)

            description = trans.get("description", "Без описания")
            from_account = mask_account_card(trans.get("from"))
            to_account = mask_account_card(trans.get("to"))

            if "Открытие вклада" in description:
                print(
                    f"{get_date(trans.get('date', ''))} Открытие вклада\n"
                    f"{to_account if to_account else 'Счёт не указан'}\n"
                    f"\nСумма: {amount} {currency}.\n"
                )
            else:
                print(
                    f"{get_date(trans.get('date', ''))} {description}\n"
                    f"{from_account if from_account else 'Источник не указан'} ->"
                    f"{to_account if to_account else 'Получатель не указан'}\n"
                    f"Сумма: {amount} {currency}.\n"
                )

        print("\nСтатистика по категориям операций:")
        category_stats = count_transactions_by_category(finaly_filter)
        for category, count in category_stats.items():
            print(f"• {category}: {count} операций")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
