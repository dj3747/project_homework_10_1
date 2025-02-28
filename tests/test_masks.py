from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_invalid(not_16_digits: str) -> None:
    assert get_mask_card_number("12345678901234567890") == not_16_digits
    assert get_mask_card_number("123456789012345") == not_16_digits
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account_invalid(not_20_digits: str) -> None:
    assert get_mask_account("123") == not_20_digits
    assert get_mask_account("1233333333333333333333333") == not_20_digits
    assert get_mask_account("73654108430135874305") == "**4305"
