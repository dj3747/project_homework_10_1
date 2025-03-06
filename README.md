# Проект 
widget_bank

## Описание: 
Проект widget_bank - это обработка банковских операций клиента.

## Установка:
1. Клонируйте репозиторий: git clone https://github.com/dj3747/project_homework_10_1
2. Стандартная библиотека Python.

## Структура проекта
Проект состоит из следующих модулей:
1. `masks`
2. `widget`
3. `processing`
4. `generators`

## Проверка кода
В проекте выполнены проверки линтерами:
- `flake8`: для проверки стиля кода
- `mypy`: для статической типизации
- `black`: для автоматического форматирования кода
- `isort`: для сортировки импортов

## Тестирование
Для тестирования используется библиотека `pytest`.
Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`
- `widget`: функции `mask_account_card` и `get_date`
- `processing`: функции `filter_by_state` и `sort_by_date`
- `generators`: функцию `filter_by_currency`,
   функцию-генератор `transaction_descriptions`, генератор `card_number_generator` `

Покрытие тестами составляет не менее 80% кода проекта.
## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE)