class  Calculator

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    @staticmethod
    def execute():
        calc = Calculator(5, 7)
        print(f'첫번째수:{calc.first}')
        print(f'두번째수:{calc.second}')
        print('{calc.first} + {calc.second}')

if __name__ == '__main__':
    Calculator.execute()