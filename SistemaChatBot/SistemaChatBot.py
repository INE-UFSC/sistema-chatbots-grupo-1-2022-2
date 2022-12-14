# from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa

        ##verificar se a lista de bots contém apenas bots
        #if all(isinstance(obj, Bot) for obj in lista_bots):
        self.__lista_bots=lista_bots
        #else:
        #    print("A lista de bots não contem apenas bots")

        self.__bot = None
        self.__end = False

    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        mensagem = f"Olá, esse é o sistema de Chatbots da empresa {self.__empresa}"
        print(mensagem)

    def mostra_menu(self):
        ##mostra o menu de escolha de bots
        print("Os chatbots disponíveis no momento são:")
        i = 0
        for bot in self.__lista_bots:
            print(f"{i} - Bot: {bot.nome} - Mensagem de apresentação: {bot.apresentacao()}")
            i += 1

    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
        op = int(input("Digite o número do chatbot desejado: "))
        self.__bot = self.__lista_bots[op]

        print(self.__bot.dizer(self.__bot.boas_vindas()))

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        comandos = self.__bot.mostra_comandos()
        print(comandos)

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        op = input("Digite o comando desejado (ou -1 para sair): ")

        if not (op.isdigit() or op == "-1"):
            return

        op = int(op)

        ##faz validacao do comando
        ### Se o comando estiver entre [-1, numero maximo de comando] e for diferente de 0 o comando eh valido
        if op <= len(self.__bot.comandos) and op >= -1 and op != 0:
            if op == -1:
                print(self.__bot.dizer(self.__bot.despedida()))
                self.__end = True
            else:
                print(self.__bot.executa_comando(op))

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        self.boas_vindas()
        print()

        self.mostra_menu()
        print()

        self.escolhe_bot()

        ## Enquanto não acabar
        while not self.__end:
            print()
            self.mostra_comandos_bot()
            print()
            
            self.le_envia_comando()
