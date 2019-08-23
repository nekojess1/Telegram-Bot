import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("928981439:AAFX_6Vw4FRdX80cO77lQmHEbMiUxcf7iaA")
bot = Chatbot("Nexus")
def recebendomensagem(msg):
    frase = bot.escuta(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)
    tipoMsg, tipoChat, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, resp)



telegram.message_loop(recebendomensagem)


while True:
    pass
