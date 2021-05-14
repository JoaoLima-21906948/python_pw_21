class automovel():

    def __init__(self, capacidade, quantidade, consumo):
        self.cap_dep = capacidade
        self.quant_comb = quantidade
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return int((self.quant_comb / self.consumo) * 100)

    def abastece(self, n_litros):
        if (n_litros + self.quant_comb) < self.cap_dep:
            self.quant_comb = n_litros + self.quant_comb
            return self.autonomia()
        else:
            print("Erro: Excedeu capacidade de combustivel")

    def percorre(self, n_km):
        if (self.autonomia() > n_km):
            self.quant_comb -= (n_km * self.consumo) / 100
            return self.autonomia()
        else:
            return -1


def main():
    a1 = automovel(60, 10, 15)
    opcao = 1
    while(opcao != 0):
        print("-------------------")
        print("MENU CARRO")
        print("1 - Autonomia Carro")
        print("2 - Abastecer Carro")
        print("3 - Percorrer (Km)")
        print("4 - Combustivel (L)")
        print("0 - Sair")
        print("-------------------")
        opcao = int(input("Escolha a opçao:"))
        while 0 > opcao > 4:
            print("Opçao invalida! Tente novamente")
            opcao = int(input("Escolha a opçao: "))

        if(opcao == 1):
            print(f"O Carro tem {a1.autonomia()} Km de Autonomia")
        elif(opcao == 2):
            print(f"Combustivel atual é de {a1.abastece(int(input()))} Litros")
        elif(opcao == 3):
            if(a1.percorre(int(input())) == -1):
                print(f"Trajecto nao foi efectuado ({a1.percorre(int(input()))} Km)")
            else:
                print(f"Percorreu {a1.percorre(int(input()))} Km")
        elif(opcao == 4):
            print(f"O Carro contem {a1.combustivel()} Litros de Combustivel")
        else:
            break

if __name__ == "__main__":
    main()
