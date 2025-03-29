import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    "C:/Users/Serg/PycharmProjects/project_homework_10_1/logs/masks.log", "w", encoding="utf-8"
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты
    и возвращает её маску"""
    logger.info("Начало маскировки карты")
    if len(card_number) != 16:
        logger.error("Некорректный номер карты")
        return "Номер должен содержать 16 цифр"
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.info("Номер карты замаскирован")
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    logger.info("Начало маскировки счёта")
    if len(account_number) != 20:
        logger.error("Некорректный номер счёта")
        return "Номер должен содержать 20 цифр"

    masked_number_account = f"**{account_number[-4:]}"
    logger.info("Номер счёта замаскирован")
    return masked_number_account
