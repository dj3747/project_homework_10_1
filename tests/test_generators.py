import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions, usd_transactions


def test_filter_by_currency(filter_by_cur):
    result = list(filter_by_currency(transactions, "USD"))
    assert result == filter_by_cur


def test_transaction_descriptions(trans_des):
    assert list(transaction_descriptions(usd_transactions)) == trans_des


@pytest.mark.parametrize(
    "transaction, expected",
    [
        ({"description": "Перевод организации"}, "Перевод организации"),
        ({"description": "Перевод со счета на счет"}, "Перевод со счета на счет"),
        ({ "description": "Перевод с карты на карту"}, "Перевод с карты на карту"),
    ]
)

def test_transaction_descriptions(transaction, expected):
    description = transaction_descriptions([transaction])
    assert list(description) == [expected]



@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1000000000000000,
            1000000000000005,
            [
                "1000 0000 0000 0000",
                "1000 0000 0000 0001",
                "1000 0000 0000 0002",
                "1000 0000 0000 0003",
                "1000 0000 0000 0004",
                "1000 0000 0000 0005",
            ],
         ),
    ],
)

def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
