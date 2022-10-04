#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotInteligente import BotInteligente
from Bots.Grupo3.BotFeliz import BotFeliz

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotInteligente("Salomão"), BotFeliz("FELIZ")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
