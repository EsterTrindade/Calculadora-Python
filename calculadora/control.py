from operacao import Operacao


class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarMenu(self):
        print('\n----- MENU -----\n\n' +
              '\n0. Sair' +
              '\n1. Somar' +
              '\n2. Subtrair' +
              '\n3. Dividir' +
              '\n4. Multiplicar' +
              '\n5. Potencia' +
              '\n6. Raiz' +
              '\n7. Tabuada' +
              '\n8. Exercício 1' +
              '\n9. Exercício 2' +
              '\n10. Exercício 3' +
              '\n11. Exercício 4' +
              '\n12. Exercício 5' +
              '\n13. Exercício 6' +
              '\n14. Exercicio 7' +
              '\n15. Exercicio 8' +
              '\n16. Exercício 9' +
              '\n17. Exercício 10' +
              '\n18. Exercício 11' +
              '\n19. Exercício 12' +
              '\n20. Exercício 13' +
              '\n21. Exercicio 14' +
              '\n22. Exercício 15' +
              '\n23. Exercício 16' +
              '\n24. Exercício 17' +
              '\n25. Exercício 18' +
              '\n26. Exercício 19' +
              '\n27. Exercício 20' +
              '\n\n----- MENU SEGUNDA LISTA -----\n' +
              '\n28. Exercício 1'+
              '\n29. Exercício 2'+
              '\n30. Exercício 3'+
              '\n31. Exercício 4')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro numero: '))
        self.num2 = int(input('Informe o segundo numero: '))

    def coletarr(self):
        self.num1 = int(input('Informe um número: '))

    def operacao(self):

        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('\nEscolha uma das opções acima: '))

            if self.opcao == 0:
                print('Obrigado!')

            if self.opcao == 1:
                self.coletar()  # Chamando o input
                print(f'A soma dos numeros é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()  # Chamando o input
                print(f'A subtração dos numeros é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()  # Chamando o input
                print(f'A divisão dos numeros é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()  # Chamando o input
                print(f'A multiplicação dos numeros é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                print(f'O resultado da potencia de {self.num1} é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()  # Chamando o input
                print(f'A raiz de {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()  # Chamando o input
                print(f'A tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                print(self.opera.exercicio01())

            elif self.opcao == 9:
                print(self.opera.exercicio02())

            elif self.opcao == 10:
                print(f'A soma dos números de 1 a 100 é: {self.opera.exercicio03()}')

            elif self.opcao == 11:
                print(f'Os múltiplos de 5 de 1 até 50 são: {self.opera.exercicio04()}')

            elif self.opcao == 12:
                self.coletarr()
                print(f'O número é: {self.opera.exercicio05(self.num1)}')

            elif self.opcao == 13:
                self.coletarr()
                print(f'O número é: {self.opera.exercicio06(self.num1)}')

            elif self.opcao == 14:
                self.coletarr()  # Chamando o input
                print(f'A tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')

            elif self.opcao == 15:
                self.coletarr()
                print(self.opera.exercicio08(self.num1))

            elif self.opcao == 16:
                self.coletarr()
                print(self.opera.exercicio09(self.num1))

            elif self.opcao == 17:
                print(self.opera.exercicio10())

            elif self.opcao == 18:
                self.coletarr()
                print(self.opera.exercicio11(self.num1))

            elif self.opcao == 19:
                print(self.opera.exercicio12())

            elif self.opcao == 20:
                self.coletarr()
                print(self.opera.exercicio13(self.num1))

            elif self.opcao == 21:
                self.coletarr()
                print(self.opera.exercicio14(self.num1))

            elif self.opcao == 22:
                self.coletarr()
                print(self.opera.exercicio15(self.num1))

            elif self.opcao == 23:
                self.coletarr()
                print(self.opera.exercicio16(self.num1))

            elif self.opcao == 24:
                self.coletarr()
                print(self.opera.exercicio17(self.num1))

            elif self.opcao == 25:
                self.coletarr()
                print(self.opera.exercicio18(self.num1))

            #19 & 20

            elif self.opcao == 28:
                print(self.opera.viceversa1())

            elif self.opcao == 29:
                self.coletarr()
                print(self.opera.antecessor2(self.num1))

            elif self.opcao == 30:
                self.coletar()
                print(f'A área do retângulo é: {self.opera.basealtura(self.num1, self.num2)}')

            elif self.opcao == 31:
                self.anos = input("Informe sua idade em anos: ")
                self.meses = input("Informe sua idade em meses: ")
                self.dias = input("Informe sua idade em dias: ")
                print(f'A sua idade em dias é: {self.opera.leiaidade(self.anos, self.meses, self.dias)}')