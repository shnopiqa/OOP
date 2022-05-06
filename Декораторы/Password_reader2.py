from string import (
    ascii_letters,  # digits - цифры
    ascii_lowercase,  # ascii_letters - все латинские буквы
    ascii_uppercase,  # ascii_lowercase - нижний регистр
    digits  # ascii_uppercase - верхний регистр
)


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.password

    @staticmethod
    def is_include_digit(password2):
        for i in digits:
            return True
        return False

    @staticmethod
    def is_include_all_register(password1):
        for i in ascii_lowercase and ascii_uppercase:
            return True
        return False

    @staticmethod
    def is_include_only_latin(password3):
        for i in ascii_letters:
            return True
        return False

    @staticmethod
    def check_password_dictionary(password4):
        with open('easy_passwords.txt') as file:
            return password4 in [row.rstrip() for row in file]


    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if not 5 <= len(value) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы 1 цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not Registration.is_include_only_latin(value):
            raise ValueError ('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError ('Ваш пароль содержится в списке самых легких')

        self.__password = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value_new):
        if value_new.count('@') < 1:
            raise ValueError("Логин должен содержать хотя бы один символ '@'")
        if '.' not in value_new[value_new.find('@'):]:
            raise ValueError("Логин должен содержать хотя бы один символ '.'")
        self.__login = value_new

