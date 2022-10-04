##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos = None):
        self.__nome = nome
        self.__comandos = {} if comandos is None else comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def dizer(self, frase: str):
        return f"--> {self.__nome} diz: {frase}"

    def mostra_comandos(self):
        return "\n".join(
            f"{i+1} - {comando}" for i, comando in enumerate(self.comandos)
        )

    def executa_comando(self, cmd: str):
        comandos = list(self.comandos.items())

        pergunta_resposta = comandos[int(cmd) - 1]

        if pergunta_resposta is None:
            return "\n".join((
                self.dizer("Eu não sei o que você disse."),
                self.mostra_comandos()
            ))

        pergunta, resposta = pergunta_resposta

        return "\n".join((
            f"--> Você disse: {pergunta}",
            self.dizer(resposta)
        ))

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass

    @abstractmethod
    def despedida(self):
        pass
