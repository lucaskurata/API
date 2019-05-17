import sqlite3
from Model.mensagem import Mensagem


# Id da mensagem: int;
# id do remetente: int;
# id do destinatário: int; - pode ser 0, para indicar que a mensagem é visível a todos.
# data/hora: str - use a biblioteca datetime para validar isso;
# texto: str

con = sqlite3.connect('banco_dados')

def criaDBMensagem():
    try:
        cur = con.cursor()
        cur.execute("create table Mensagem ( \
            id_Mensagem integer,\
            id_Remetente integer,\
            id_Destinatario integer,\
            data date,\
            hora time,\
            texto varchar(300)\
            )")
        con.commit()
        con.close()
    except Exception as identificador:
        pass

def listarMensagens():
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute('select * from Mensagem')
        return [Mensagem.cria_de_tupla(el) for el in cur.fetchall()]
    finally:
        con.close()

def novaMensagem(Mensagem):
    con = sqlite3.connect('banco_dados')
    try:
        cur = con.cursor()
        cur.execute("insert into Mensagem(id_Remetente, id_Destinatario, data, hora, texto) \
            values (:id_Remetente, :id_Destinatario, :data, :hora, :texto)", Mensagem.__dict__())
        con.commit()
    except:
        con.rollback()
    finally:        
        con.close()