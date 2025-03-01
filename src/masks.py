def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты
    и возвращает её маску"""
    if len(card_number) != 16:
        return "Номер должен содержать 16 цифр"
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    if len(account_number) != 20:
        return "Номер должен содержать 20 цифр"

    masked_number_account = f"**{account_number[-4:]}"
    return masked_number_account
