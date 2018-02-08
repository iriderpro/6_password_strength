import re
import password_blacklist


def password_check(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d.", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(
        r"[ !@#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
        password,
    ) is None
    date_error = re.search(r"\d{6,}", password) is not None
    if password in password_blacklist.list_password:
        score = 0
    else:
        score = 4

    for item in (
        length_error,
        digit_error,
        uppercase_error,
        lowercase_error,
        symbol_error,
        date_error,
    ):
        if item is False:
            score += 1
    return score


if __name__ == '__main__':
    print(password_check(input('Введите пароль: ')))
