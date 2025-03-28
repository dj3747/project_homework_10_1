import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_number, expected_masked",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_number: str, expected_masked: str) -> None:
    assert mask_account_card(card_number) == expected_masked


@pytest.mark.parametrize(
    "card_number, expected_masked",
    [
        # Дополнительные тесты для карт
        ("Mastercard 5308276796905321", "Mastercard 5308 27** **** 5321"),
        ("Discover 6011894492395579", "Discover 6011 89** **** 5579"),
    ],
)
def test_mask_account_card_edge_cases(card_number: str, expected_masked: str) -> None:
    assert mask_account_card(card_number) == expected_masked


@pytest.mark.parametrize(
    "card_number, expected_masked",
    [
        # Тесты для некорректных данных
        ("", "Не указаны данные"),
        # Тесты с лишними пробелами
        ("  Mastercard  5308276796905321  ", "Mastercard 5308 27** **** 5321"),
        ("Счет  73654108430135874305  ", "Счет **4305"),
        # Неподдерживаемые типы карт
        ("MIR 1234567812345678", "MIR 1234567812345678"),
    ],
)
def test_mask_account_card_additional_cases(card_number: str, expected_masked: str) -> None:
    assert mask_account_card(card_number) == expected_masked


@pytest.mark.parametrize(
    "inter_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ],
)
def test_get_date(inter_format: str, expected: str) -> None:
    assert get_date(inter_format) == expected


@pytest.mark.parametrize(
    "inter_format, expected",
    [
        # Разные варианты времени
        ("2024-01-01T00:00:00Z", "01.01.2024"),
        ("2023-02-28T23:59:59.999999", "28.02.2023"),
        # Дата без времени
        ("2025-12-31", "31.12.2025"),
    ],
)
def test_get_date_edge_cases(inter_format: str, expected: str) -> None:
    assert get_date(inter_format) == expected
