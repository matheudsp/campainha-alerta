from Botao import *
from DetectarResposta import *
from Alerta import *
import datetime

class Testador():
    # botão inicializador
    hora = int(datetime.datetime.now().hour)
    saida1 = Botao(hora)
    print(saida1)


    # reconhecimento da fala e denifir nome do autor do clique
    saida2 = DetectarResposta()

    # envio de mensagem pelo telegram
    saida3 = EnviarAlerta(saida2)
    print(saida3)




