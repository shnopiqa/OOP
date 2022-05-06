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
        my_set = ['123456', 'password', '123456789', '12345', '2345678', 'qwerty', '234567', '111111', '1234567890',
                  '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
                  'Dragon1', 'sunshine', 'princess', 'letmein', '654321', 'monkey', '27653', '1qaz2wsx', '123321',
                  'qwertyuiop', 'superman', 'asdfghjkl']

        for i in my_set:
            return True
        return False

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
        if not Registration.check_password_dictionary(value):
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
