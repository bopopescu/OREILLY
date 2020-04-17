from flask import session
from functools import wraps


def check_logged_in(func: object) -> object:  # мой декоратор на проверку авторизации юзера
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'

    return wrapper
