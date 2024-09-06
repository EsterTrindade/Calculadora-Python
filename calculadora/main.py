from operacao import Operacao
# Executa as transações entre classes

if __name__ == '__main__':
    opera = Operacao()
    num1  = int(input("Informe o primeiro número: "))
    num2  = int(input("Informe o segundo número: "))

    print(f'A soma dos números é: {opera.somar(num1, num2)}')
    print(f'A subtração dos números é: {opera.subtrair(num1, num2)}')
    print(f'A multiplicação dos números é: {opera.multiplicar(num1, num2)}')
    print(f'A divisão dos números é: {opera.dividir(num1, num2)}')