# BellAlert
### Campainha usando API do telegram, SpeechRecognition e pyttsx3

<img align="right" width="300" src="https://i2.wp.com/allhtaccess.info/wp-content/uploads/2018/03/programming.gif?fit=1281%2C716&ssl=1" />


## **Utilizando:**  


<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>


## Bibliotecas

*Bibliotecas usadas para rodar o código. Veja também [requirements.txt](https://github.com/matheudsp/campainha-alerta/blob/master/requirements.txt).*

    * requests # enviar nossa mensagem pela API Bot do telegram
    * pyttsx3 # sintetizador de voz
    * SpeechRecognition # reconhecer a nossa fala 
    * emoji # desnecessário 
    * pipwin # usado para instalar o pyaudio
    * #usando pipwin, faça: pipwin install pyaudio 
   
   

## Botão.py - simula um botão da "campainha"
* Recebe hora atual do sistema para receber a visita baseado no horário.
* Ao ser executado, inicializa arquivo "campainha.mp3" que simula o som da campainha.



  *[Veja o código](https://github.com/matheudsp/campainha-alerta/blob/master/Botao.py)*

      from pyttsx3 import speak
      import time
      import os
      from Robot import *


      class Botao(Robot):
          def __init__(self,hora):
              super().__init__("Bell Alert","Fixo","Inicializador\n")
              self.h = hora

        def speak(self,audio):
            engine.say(audio)
            engine.runAndWait()

        def acao(self):
            toqueSonoro = '.\sound\campainha1.mp3'
            os.system(toqueSonoro)
            time.sleep(3)

            if self.h >= 0 and self.h < 12:
                self.speak("Bom dia!")  

            elif self.h >= 12 and self.h < 18:
                self.speak("Boa tarde!")   

            else:
                self.speak("Boa noite!")  
            return "O botão foi pressionado"

        def __str__(self):  
            r = super().__str__()
            r += "\n"+str(self.acao())
            return r
 
 
 
 ## DetectarResposta.py - faz a conversação entre código e visita
 
 * Atribui valor, recebido pela biblioteca SpeechRecognition, a variável "visita".


   *[Veja o código](https://github.com/matheudsp/campainha-alerta/blob/master/DetectarResposta.py)*

        from Robot import *
        import speech_recognition as sr

        class DetectarResposta(Robot):

            def __init__(self):
                super().__init__("Bell Alert","Fixo","Detecta a resposta\n")


            def speak(self,audio):
                engine.say(audio)
                engine.runAndWait()

            def acao(self):
                reconhecer = sr.Recognizer() 
                r = reconhecer
                with sr.Microphone() as source:
                    self.speak("Por favor, se identifique.")
                    print("Escutando...")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    print("Reconhecendo...")

                try:
                    self.visita = r.recognize_google(audio, language='pt-br')
                    self.speak("Notificando o proprietário ")
                    return str(self.visita)

                except Exception as erro:
                    self.speak("Não foi possível entender, tente novamente.")
                    return(erro)

            def __str__(self):
                r = super().__str__()
                r += "\n"+(str(self.acao())) 
                visita = str(self.visita)
                print(r)
                return visita




 ## DetectarResposta.py - se conecta a API do telegram e envia nosso alerta de novas visitas.
 * Necessário obter o Token do BOT.
 * E também ter o idchat, para chat particular(uma só pessoa), ou groupid, para chat com vários membros. 
 * Facilmente obtido pelo Telegram, através do *[Bot Raw](https://t.me/RawDataBot)* ℹ️ Made by @SeanChannel.
 
   *[Veja o código](https://github.com/matheudsp/campainha-alerta/blob/master/Alerta.py)*
 
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





    
    

   
