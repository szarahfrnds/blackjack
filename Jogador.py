from Carta import Carta
from dealer import Dealer


class Jogador:
    def __init__(self, nickname, age):
        self.__nickname = nickname
        self.__age = age
        self.__points = []
        self.cartas = []

    @property
    def identificacao(self):
        return self.__nickname, self.__age

    @property
    def valor_mao(self):
        return sum(self.cartas)


todomundo = []

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    jogador = Jogador(nome, idade)
    todomundo.append(jogador.identificacao)

    maisjogador = input("Quer inserir mais um jogador? S//N").upper()
    if maisjogador == "S":
        continue
    else:
        break

print("Sejam bem vindos, a identificação de vocês é ", todomundo)


dealernome = input("Dealer, insira seu nome: ")

meudealer = Dealer(dealernome)
print("seja bem vindo", meudealer.identificacao())

for i in todomundo:
    cartaselecionada = meudealer.escolha()
    todomundo[i] = jogador.cartas.append(cartaselecionada)










