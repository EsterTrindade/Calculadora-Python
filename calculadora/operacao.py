import math


class Operacao:

    # Métodos

    def __init__(self):  # Construtor
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
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
        msg = ""  # Variável acumuladora
        for i in range(1, 11, 1):
            msg += f"\n{i}"
        return msg

    def exercicio02(self):
        pares = ""
        for i in range(1, 21, 1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        soma = 0
        for i in range(1, 101):
            soma += i
        return soma

    def exercicio04(self):
        mult = ""
        for i in range(5, 51, 5):
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

    # Resolver exercício 9
    def exercicio09(self, num):
        result = ""
        for i in range(1, num + 1):
            result += f'{num} + {i} = {num + i}\n'
        return result

    def exercicio10(self):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O {num} é primo'
        return f'O {num} não é primo'

    # Resolver exercício 12
    def exercicio12(self):
        n = 6
        if n == 0:
            return 1
        for i in range(1, n):
            fat = i * i
        return fat

    def exercicio13(self, num):
        fib = 0
        fib1 = 1
        for i in range(0, num):
            fib2 = fib + fib1
            fib = fib1
            fib1 = fib2
            print(fib2)
        return fib2

    # Resolver exercício 14
    def exercicio14(self, num):
        fib = 0
        fib1 = 1
        for i in range(0, num):
            fib2 = fib + fib1
            fib = fib1
            fib1 = fib2
            print(fib2)
        return fib2

    def exercicio15(self, num):
        soma = 0
        for digito in str(num):
            if digito.isdigit():
                soma += int(digito)
        return soma

    def exercicio16(self, num):
        for i in range(1, num):
            if i % 2 == 0:
                print(f'PAR:\n{i}\n')
            else:
                print(f'ÍMPAR:\n{i}\n')

    def exercicio17(self, num):
        for i in range(1, num):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                print(f'PRIMOS:\n{i}\n')

    def exercicio18(self, num):
        for i in range(1, num):
            if 0 == 2:
                return 0
            elif i % 2 == 0:
                print(1 + i//2)
            else:
                print(1 + (3*i+1))

    #19 & 20

    def viceversa1(self):
        a = 10
        b = 20
        if a == 10 and b == 20:
            a = 20
            b = 10
        return f'Variavel A = {a} ' \
               f'\nVarialve B = {b}'

    def antecessor2(self, num):
        return num - 1

    def basealtura(self, base, altura):
        return base * altura

    def leiaidade(self, anos, meses, dias):
        result = anos * 365 + meses * 30
        return result

    def eleitores(self, elei, votosbrancos, votosnulos, votosvalidos):






































