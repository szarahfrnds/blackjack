class Carta:
    def __init__(self, simbolo, valor):
        self.__simbolo = simbolo
        self.__valor = valor

    @property
    def simbolo(self):
        return self.__simbolo

    @property
    def valor(self):
        return self.__valor





