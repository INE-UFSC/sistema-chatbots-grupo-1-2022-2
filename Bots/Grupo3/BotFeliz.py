from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        comandos = {
            "Qual o seu nome?": "Meu nome é {}, meu querido!".format(nome),
            "Quero um conselho": "Você deve ser feliz! Viva sua vida sem se importar com as opiniões dos outros, seja você!!",
            "Como posso ser feliz, igual você?": "Ummmmmmm deixa eu ver, seja você mesmo, beba água, se exercite e tenha um coelho, eu acho.",
            "Conte uma piada": "O que o pato disse para a pata? Vem Quá HAHAHHAHAAHAHAHAHAAHAHAAHHA",
            "Que tipo de pessoas você gosta?": "De pessoas algres, auto astral e sorridentes :) :) :) :)",
            "Para quem você ira torcer nessa copa?": "É OBVIO QUE PARA O BRASILLLLLLLLLLLLLLLLLLL",
            "Está feliz?": "É CLAROOOOOOOOOOOOO"

            }
        super().__init__(nome, comandos)

    def apresentacao(self) -> str:
        return "Olá, me chamo {}, meu trabalho e lhe ajudar, o que você deseja, grande amigo?"

    def boas_vindas(self) -> str:
        return "Muito obrigado por me escolher, a partir de hoje serei seu melhor amigoooooooooo :) :)"
    
    def despedida(self) -> str:
        return "Até mais meu grande amigo, estou muitooooooooooooooooo feliz por te conhecer, espero muito que a gente se veja de novo, meu grande amigoooooooooooo!!!"
