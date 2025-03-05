from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date, list_of_dictionaries
from src.widget import get_date, mask_account_card


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
    print(filter_by_state(list_of_dictionaries))
    print(sort_by_date(list_of_dictionaries))
