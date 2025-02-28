import pytest


@pytest.fixture
def card_num():
    return "7000 79** ****6361"

@pytest.fixture
def account_num():
    return "**4305"

@pytest.fixture
def name_number_card_1():
    return "Visa Platinum 7000 79** ****6361"


@pytest.fixture
def name_number_card_2():
    return "Maestro 7000 79** ****6361"


@pytest.fixture
def name_account():
    return "Счет **4305"

@pytest.fixture
def inter_format():
    return "11.03.2024"



@pytest.fixture
def not_16_digits():
    return "Номер должен содержать 16 цифр"

@pytest.fixture
def not_20_digits():
    return "Номер должен содержать 20 цифр"

@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
