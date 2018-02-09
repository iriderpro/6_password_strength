import re


list_bad_password = [
    'Password1',
    '12345',
    '123',
    '1',
    '12',
    '0',
    '111',
    '0000',
    '1111',
    '123456',
    'Password',
    '12345678',
    'qwerty',
    '123456789',
    'letmein',
    '1234567',
    'football',
    'iloveyou',
    'admin',
    'welcome',
    'monkey',
    'login',
    'abc123',
    'starwars',
    '123123',
    'passw0rd',
    'hello',
]


def password_check(password):
    length_check = len(password) < 8
    digit_check = re.search(r"\d.", password) is None
    uppercase_check = re.search(r"[A-Z]", password) is None
    lowercase_check = re.search(r"[a-z]", password) is None
    symbol_check = re.search(
        r"[ !@#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
        password,
    ) is None
    date_number_check = re.search(r"\d{6,}", password) is not None
    if password in list_bad_password:
        score = 0
    else:
        if length_check is True:
            score = 0
        else:
            score = 5

    for check in (
        digit_check,
        uppercase_check,
        lowercase_check,
        symbol_check,
        date_number_check,
    ):
        if check is False:
            score += 1
    return score


if __name__ == '__main__':
    print(
        'Сложность пароля по шкале от 1 до 10 :',
        password_check(input('Введите пароль: '))
    )
