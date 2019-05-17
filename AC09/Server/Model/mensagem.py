from datetime import time, date

class Mensagem():
    def __init__(self, id_Mensagem, id_Remetente, id_Destinatario, date, time, texto):
        self.id_Mensagem = id_Mensagem
        self.id_Remetente = id_Remetente
        self.id_Destinatario = id_Destinatario
        self.data = date
        self.hora = time
        self.texto = texto

    def __dict__(self):
        dicio = dict()
        dicio['id_Mensagem'] = self.id_Mensagem
        dicio['id_Remetente'] = self.id_Remetente
        dicio['id_Destinatario'] = self.id_Destinatario
        dicio['date'] = self.data
        dicio['time'] = self.hora
        dicio['texto'] = self.texto
        return dicio

    @staticmethod
    def cria(dados):
        try:
            id_Mensagem = dados["id_Mensagem"]
            id_Remetente = dados["id_Remetente"]
            id_Destinatario = dados["id_Destinatario"]
            date = dados["date"]
            time = dados["time"]
            texto = dados["texto"]
            return Mensagem(id_Mensagem = id_Mensagem, id_Remetente = id_Remetente, id_Destinatario = id_Destinatario,date = date, time = time, texto = texto)
        except Exception as e:
            print("Problema ao Enviar Mensagens!")
            print(e)
    
    @staticmethod
    def cria_de_tupla(dados):
        try:
            id_Mensagem = dados[0]
            id_Remetente = dados[1]
            id_Destinatario = dados[2]
            date = dados[3]
            time = dados[4]
            texto = dados[5]
            return Mensagem(id_Mensagem = id_Mensagem, id_Remetente = id_Remetente, id_Destinatario = id_Destinatario,date = date, time = time, texto = texto)
        except Exception as e:
            print("Problema ao Enviar Mensagens!")
            print(e)

