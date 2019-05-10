from datetime import time, date

class Mensagem():
    def __init__(self, idMensagem, idRemetente, idDestinatario, date, time, texto):
        self.idMensagem = idMensagem
        self.idRemetente = idRemetente
        self.idDestinatario = idDestinatario
        self.data = date
        self.hora = time
        self.texto = texto
