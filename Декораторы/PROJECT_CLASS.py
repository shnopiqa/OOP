




class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 4
    REACT_DEV = 2

    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info1(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def info2(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    @classmethod
    def info3(cls):
        print('infoclass')
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
    @staticmethod
    def statik():
        print('infostatik')
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def make_backend(self):
        print('Python and GO')

    def make_fronted(self):
        print('Reackt')

iti = DepartmentIT()
iti.statik()