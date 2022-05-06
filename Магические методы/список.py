class Vector:

    @staticmethod
    def p_sort_num(p_list):
        num_list = []
        for el in p_list:
            if isinstance(el, int):
                num_list += [el]
        num_list.sort()
        return num_list

    def __init__(self, *p):
        self.values = self.p_sort_num(p)

    def __str__(self):
        if len(self.values) == 0:
            return f'Пустой вектор'
        else:
            s = 'Вектор(' + str(self.values[0])
            n = len(self.values)
            for i in range(1, n):
                s = s + ', ' + str(self.values[i])
            return s + ')'


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"
