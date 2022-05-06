class Counter:
    def start_from(self, start_value=0):
        self.count = start_value
    def increment(self):
        self.count = self.count + 1
    def display(self):
        print(f'Текущее значение счетчика {self.count}')
    def reset(self):
       self.count = self.count * 0


c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"


