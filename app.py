#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotInteligente import BotInteligente

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotInteligente("Salomão")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
