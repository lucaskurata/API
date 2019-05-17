from Model.mensagem import Mensagem
from Infra.mensagens_db import listarMensagens, novaMensagem


def EnviarMensagem(mensagem_data):
    novaMensagem(Mensagem.cria(mensagem_data))
    return novaMensagem

def LerMensagem(id_Mensagem):
    for msg in mensagens_db:
        if msg.id_Mensagem == id_Mensagem:
            return msg
    return None

