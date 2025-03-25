from unittest.mock import patch


@patch("src.file_reader.read_csv")
def test_read_csv(mock_read_csv):
    """Настраиваем mock для функции read_csv"""
    mock_read_csv.return_value = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }

    result = mock_read_csv("some_file.csv")

    expected_result = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }

    assert result == expected_result


if __name__ == "__main__":
    test_read_csv()


@patch("src.file_reader.read_exel")
def test_read_exel(mock_read_exel):
    """Настраиваем mock для функции read_exel"""
    mock_read_exel.return_value = {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }

    result = mock_read_exel("some_file.xlsx")

    expected_result = {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }

    assert result == expected_result


if __name__ == "__main__":
    test_read_exel()
