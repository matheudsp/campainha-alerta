#desafio robot - subclasse-subclasse > superclasse
#ideias de robos
#campainha  manda mensagem ao proprietario
import pyttsx3


engine = pyttsx3.init('sapi5')  #sapi5, nsss, espeak
rate = engine.getProperty('rate')   # define vel da voz
engine.setProperty('rate',170)
voices = engine.getProperty('voices')   #obtem detalhes da voz
engine.setProperty('voice', voices[0].id)   # voices[1].id ou voices[0].id


class Robot:
    def __init__(self,nome,tipo,tarefa):
        self.nome = nome
        self.tipo = tipo
        self.tarefa = tarefa

    def __str__(self):
        r = "\nnome : "+str(self.nome)
        r += "\ntipo : "+str(self.tipo)
        r += "\ntarefa : "+str(self.tarefa)
        return r

    
        

