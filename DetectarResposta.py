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
        
    
    




