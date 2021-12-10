import emoji
import requests
from Robot import *

class EnviarAlerta(Robot):
    def __init__(self,visitante):
        super().__init__("Bell Alert","Fixo","Enviar alerta ao proprietário\n")
        self.v = visitante
        
    
    def acao(self):
        #parametros da mensagem
        emoji_alerta = (emoji.emojize(':warning:'))
        self.msg = 'Há visita(s)!!'+emoji_alerta+'\n'
        self.msg2 = ' está tocando a campainha.'
        self.TokenBOT = 'bot_telegram_token'
        self.UserID = 'idchat ou groupid do seu telegram'  # id do chat pessoal ou id do grupo
        enviarMensagem = 'https://api.telegram.org/bot' + self.TokenBOT + '/sendMessage?chat_id=' + self.UserID + '&parse_mode=Markdown&text=' + str(self.msg) +'\n'+ str(self.v) + str(self.msg2)

        alerta = requests.get(enviarMensagem)
        return alerta.json()

    def __str__(self):
        r = super().__str__()
        r += "\nA mensagem foi enviada\n"
        r += "\ninfo:"+(str(self.acao()))
        return r
        
        
    


    
    

   