from Bots.Bot import Bot


COMANDOS = {
    "Bom dia": "Só se for pra você.",
    "Qual o seu nome?":"Te interessa?",
    "Quero um conselho":"E eu tenho cara de psicólogo por acaso?",
    "Do que você gosta?":"De tudo que você odeia",
    "Como você está se sentindo?":"Zangado!!",
    "Por quê você está zangado?": "Porque você está aqui"
}


class BotZangado(Bot):
    def __init__(self,nome, comandos = COMANDOS):
        super().__init__(nome, comandos)


    def apresentacao(self):
        return f"Olá, meu nome é {self.__nome}. Eu estou tendo um péssimo dia, então por favor não faça nada para me irritar."
            
            
    def boas_vindas(self):
        return f"Nao consigo acreditar que eu tenho que fazer novamente...\n De qualquer maneira, boas-vindas caro cliente. Espero que a sua estadia seja breve e dolorosa."

    def despedida(self) -> str:
        return "Finalmente!! Espero nunca te ver novamente, seu chato!"
        