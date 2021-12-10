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