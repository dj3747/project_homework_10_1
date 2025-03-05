transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict], currency_code: str = "USD"):
    """Функция фильтрует входящий список транзакций по коду валюты"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


usd_transactions = list(filter_by_currency(transactions, "USD"))
for trans in usd_transactions:
    print(trans)


def transaction_descriptions(transaction):
    """Функция возвращает описание каждой операции"""
    result = (x.get("description") for x in transaction)  # значение по ключу

    for x in result:
        yield x


descriptions = list(transaction_descriptions(transactions))
print(*list(descriptions), sep="\n")


def card_number_generator(start, stop):
    """Функция генерирует номер карты в заданном диапазоне"""
    for card_list in range(start, stop + 1):
        if 0 <= card_list <= 9999999999999999:
            card_num = f"{card_list:016}"
            format_card_num = " ".join([card_num[i:i+4] for i in range(0, 16, 4)])
            yield format_card_num


for card in card_number_generator(0, 5):
    print(card)
