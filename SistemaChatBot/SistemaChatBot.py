from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa

        ##verificar se a lista de bots contém apenas bots
        if all(isinstance(obj, Bot) for obj in lista_bots):
            self.__lista_bots=lista_bots
        else:
            print("A lista de bots não contem apenas bots")

        self.__bot = None

    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        mensagem = f"Olá, esse é o sistema de Chatbots da empresa {self.__empresa}"
        print(mensagem)

    def mostra_menu(self):
        ##mostra o menu de escolha de bots
        print("Os chatbots disponíveis no momento são:")
        i = 0
        for bot in self.__lista_bots:
            print(f"{i} - Bot: {bot.nome()} - Mensagem de apresentação: {bot.apresentacao()}")
            i += 1

    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
        op = int(input("Digite o número do chatbot desejado: "))
        self.__bot = self.__lista_bots[op]

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        comandos = self.__bot.mostra_comandos()
        print(comandos)

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        op = input()
        self.__bot.executa_comando(op)

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()

        ## TODO Rever esse loop infinito
        while True:
            self.mostra_comandos_bot()
            self.le_envia_comando()
