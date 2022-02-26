from utils.perceptron import Perceptron


class Game:
    def __init__(self, gabarito, amostras, dominio_pesos):
        self.operacoes = {    
            "or": Perceptron(0.1, -1, 1000, 0, gabarito, amostras, dominio_pesos),
            "and": Perceptron(0.1, -1, 1000, 1, gabarito, amostras, dominio_pesos),
            "nor": Perceptron(0.1, -1, 1000, 2, gabarito, amostras, dominio_pesos),
            "nand": Perceptron(0.1, -1, 1000, 3, gabarito, amostras, dominio_pesos)
        }

        self.operacao = 0

        self.treinar()

    def treinar(self) -> None:
        for perceptron in self.operacoes.values():
            perceptron.treinar()

    def selecionar_operacao(self) -> None:
        print("[1] - OR")
        print("[2] - AND")
        print("[3] - NOR")
        print("[4] - NAND")
        print("[5] - XOR")
        print("[0] - Sair")

        self.operacao = int(input("Selecione uma operação: "))

        if self.operacao not in [0, 1, 2, 3, 4, 5]:
            print("Digite uma opção valida!")
            self.selecionar_operacao()

    def selecionar_entradas(self) -> tuple:
        x1 = int(input("Digire o valor de x1: "))
        x2 = int(input("Digire o valor de x2: "))

        if x1 not in [0, 1] or x2 not in [0, 1]:
            print("Digite uma entradas validas!")
            self.selecionar_entradas()

        return x1, x2

    def menu(self) -> None:
        while True:
            self.selecionar_operacao()

            if self.operacao == 0:
                print("Saindo...")
                break

            entradas = self.selecionar_entradas()
            
            if self.operacao == 1:
                print(self.operacoes["or"].testar(entradas))

            elif self.operacao == 2:
                print(self.operacoes["and"].testar(entradas))

            elif self.operacao == 3:
                print(self.operacoes["nor"].testar(entradas))

            elif self.operacao == 4:
                print(self.operacoes["nand"].testar(entradas))

            elif self.operacao == 5:
                x_oculto = self.operacoes["nand"].testar(entradas)
                y_oculto = self.operacoes["or"].testar(entradas)

                print(self.operacoes["and"].testar([x_oculto, y_oculto]))