from menu import Menu #Conecta a main a Classe, geralmente, um arquivo para cada Classe nova, para conectar mais de uma classe
# Executa as transações entre classes

if __name__ == '__main__':
    men = Menu()
    men.operacao()


#    opera = Operacao()
#    num1  = int(input("Informe o primeiro número: "))
#    num2  = int(input("Informe o segundo número: "))
#
#    print(f'A soma dos números é: {opera.somar(num1, num2)}')
#    print(f'A subtração dos números é: {opera.subtrair(num1, num2)}')
#    print(f'A multiplicação dos números é: {opera.multiplicar(num1, num2)}')
#    print(f'A divisão dos números é: {opera.dividir(num1, num2)}\n')
#    print(f'A Tabuada do {num1} é: \n{opera.tabuada(num1)}\n')
#    print(f'Tabuada do {num2} é: \n{opera.tabuada(num2)}\n')
#    print(f'O resultado da potência é: {opera.potencia(num1, num2)}')
#    print(f'A Raiz de {num1} é: {opera.raiz(num1)}')
#    print(f'A Raiz de {num2} é: {opera.raiz(num2)}')