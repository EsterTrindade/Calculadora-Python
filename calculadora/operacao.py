class Operacao:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1,  num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1,  num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1,  num2)
        return self.num1 / self.num2