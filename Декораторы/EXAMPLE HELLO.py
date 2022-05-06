class Example:
    def hello ():
        print('Hello')
    def instance_hello (self):
        print(f'Hello {self}')
    @staticmethod
    def static_hello():
        print('statick hello')
    @classmethod
    def class_hello (cls):
        print(f'Hello {cls}')

