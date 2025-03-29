from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_string: str) -> str:
    """Функция принимает тип и номер карты или счета, возвращает маску"""
    if not isinstance(user_string, str) or not user_string.strip():
        return "Не указаны данные"
    element = user_string.split()
    if "Счет" in element:
        try:
            account_number = element[-1]
            return f"{element[0]} {get_mask_account(account_number)}"
        except Exception as e:
            return f"Ошибка при обработке счёта: {e}"
    card_types = ["Visa", "Maestro", "Mastercard", "American Express", "Discover"]
    for card_type in card_types:
        if card_type in element:
            try:
                card_number = element[-1]
                return f"{' '.join(element[:-1])} {get_mask_card_number(card_number)}"
            except IndexError:
                return f"{user_string}"
    return user_string


def get_date(international_date: str) -> str:
    """Функция принимает дату в международном формате, возвращает в обычном"""
    international_date_split = international_date.split("T")
    new_date = international_date_split[0].split("-")
    normal_date = ".".join(new_date[::-1])
    return f"{normal_date}"
