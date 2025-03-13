import time
from functools import wraps

def log(filename=None):
    """Декоратор, который будет логировать начало и конец выполнения функции,
    а также её результаты и возникшие ошибки"""

    def my_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                try:
                    result = func(*args, **kwargs)
                    end_time = time.time()
                    log_message = (
                        f"{func.__name__} started at {start_time} and finished at {end_time} with result: {result}"
                    )
                    if filename is not None:
                        with open(filename, "a", encoding="utf-8") as file:
                            file.write(f"{func.__name__} ok\n")
                    else:
                        print(log_message)

                except Exception as e:
                    log_message_1 = f"{func.__name__} error {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                    if filename:
                        with open(filename, "a", encoding="utf-8") as file:
                            file.write(log_message_1 + "\n")
                    else:
                        print(log_message_1)
                    raise e
                return result
            return wrapper
    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    """Получение суммы двух чисел"""
    return x + y

my_function(1, 2)
