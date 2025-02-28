import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "name_number_card_1, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(name_number_card_1: str, expected: str) -> None:
    """Тестиреет функцию на входные данные"""
    assert mask_account_card(name_number_card_1) == expected


def test_mask_account_card_invalid_1() -> None:
    """Проверяет недопустимые входные данные"""
    with pytest.raises(AttributeError):
        mask_account_card("12345678901234567890")


@pytest.mark.parametrize(
    "name_number_card_2, expected",
    [
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(name_number_card_2: str, expected: str) -> None:
    """Тестиреет функцию на входные данные"""
    assert mask_account_card(name_number_card_2) == expected


def test_mask_account_card_invalid_2() -> None:
    """Проверяет недопустимые входные данные"""
    with pytest.raises(AttributeError):
        mask_account_card("12345678901234567890")


@pytest.mark.parametrize(
    "inter_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ],
)
def test_get_date(inter_format: str, expected: str) -> None:
    assert get_date(inter_format) == expected
