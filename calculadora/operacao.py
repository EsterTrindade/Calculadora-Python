import math

class Operacao:

    #Métodos

    def __init__(self): #Construtor
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
        if self.num2 <= 0:
            return "Impossível dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num):
        return math.sqrt(num)

    def exercicio01(self):
        msg = "" #Variável acumuladora
        for i in range(1,11,1):
            msg += f"\n{i}"
        return msg

    def exercicio02(self):
        pares = ""
        for i in range(1,21,1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        soma = 0
        for i in range(1,101):
            soma += i
        return soma

    def exercicio04(self):
        mult = ""
        for i in range(5,51,5):
            mult += f"\n{i}"
        return mult

    def exercicio05(self, num):
        if num % 2 == 0:
            return "Par!"
        else:
            return "Ímpar!"

    def exercicio06(self, num):
        if num < 0:
            return "NEGATIVO!"
        elif num > 0:
            return "POSITIVO!"
        else:
            return "0"

    def exercicio08(self, num):
        for i in range(1, num + 1):
            print(i)

    def exercicio09(self, num):
        result = ""
        for i in range(0, num + 1):
            result += f'\n{num + i}'
        return result












