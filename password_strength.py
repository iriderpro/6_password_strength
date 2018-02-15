import re
import password_blacklist
import getpass


def password_check(password):
    minimal_length_password = 8
    length_check = len(password) < minimal_length_password
    digit_check = re.search(r"\d.", password) is None
    uppercase_check = re.search(r"[A-Z]", password) is None
    lowercase_check = re.search(r"[a-z]", password) is None
    symbol_check = re.search(
        r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]',
        password,
    ) is None
    date_number_check = re.search(r"\d{6,}", password) is not None
    if password in password_blacklist.list_bad_password:
        score1 = 0
    else:
        if length_check is True:
            score1 = 0
        else:
            score1 = 5
    score2 = sum([
        digit_check,
        uppercase_check,
        lowercase_check,
        symbol_check,
        date_number_check])
    score2 = 5 - score2
    score = score1 + score2
    return score


if __name__ == "__main__":
    print(
        "Сложность пароля по шкале от 1 до 10 :",
        password_check(getpass.getpass(prompt="Введите пароль : "))
    )
