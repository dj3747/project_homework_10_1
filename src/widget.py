from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_string: str) -> str:
    """Функция принимает тип и номер карты или счета, возвращает маску"""

    element = user_string.split()
    if "Счет" in element:
        account_number = element[-1]
        return f"{element[0]} {get_mask_account(account_number)}"
    elif "Visa" in element or "Maestro" in element:
        card_number = element[-1]
        return f"{' '.join(element[:-1])} {get_mask_card_number(card_number)}"
    else:
        return f"{'Вы ввели некорректные данные'}"


def get_date(international_date: str) -> str:
    """Функция принимает дату в международном формате, возвращает в обычном"""

    international_date_split = international_date.split("T")
    new_date = international_date_split[0].split("-")
    normal_date = ".".join(new_date[::-1])
    return f'"{normal_date}"'
