import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(name_number_card: str) -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == name_number_card


@pytest.mark.parametrize(
    "inter_format, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ],
)
def test_get_date(inter_format: str, expected: str) -> None:
    assert get_date(inter_format) == expected
