from Carta import Carta
import random


class Dealer:
    def __init__(self, nome):
        self.nome = nome
        self.minhacarta = [2,
                            1,
                           10,
                           10,
                           10,
                           3,
                           4,
                           5,
                           6,
                           7,
                           8,
                           9,
                           10
                           ]

    def identificacao(self):
        return self.nome

    def escolha(self):
        escolha = random.randrange(0, len(self.minhacarta))
        carta_escolhida = self.minhacarta[escolha]

        return carta_escolhida











