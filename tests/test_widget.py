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
    "inter_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ],
)
def test_get_date(inter_format: str, expected: str) -> None:
    assert get_date(inter_format) == expected
