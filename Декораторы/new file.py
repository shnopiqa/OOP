from string import digits


class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'abrababar'

    @property
    def secret(self):
        s = input('Введите ваш пароль:')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Ошибочка')

    @property
    def password(self):
        return self.__password

    @staticmethod
    def is_includede_number(password):
        for i in digits:
            return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой')
        if len(value) <= 4:
            raise ValueError('Пароль должен быть 4 символа')
        if len(value) >= 12:
            raise ValueError('Длина слишком велика')
        if not User.is_includede_number(value):
            raise ValueError('Пароль должен содержать хотя бы 1 цифру')
        self.__password = value


a = User('a', 'aaaaaa')
print(a.password)
print(a.secret)
