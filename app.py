#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotInteligente import BotInteligente
from Bots.Grupo3.BotFeliz import BotFeliz
from Bots.Grupo5.BotTriste import BotTriste
from Bots.Grupo6.BotGrupo6 import BotGrupo6

###construa a lista de bots disponíveis aqui
lista_bots = [
    BotZangado("Yoda"),
    BotInteligente("Salomão"),
    BotFeliz("FELIZ"),
    BotTriste(),
    BotGrupo6("1")
    
]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
