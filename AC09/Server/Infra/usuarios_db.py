import sqlite3
from Model.usuario import Usuario

# Id: int, nome: str, segredo: str
connect = sqlite3.connect('banco_dados')
cursor = connect.cursor()

def CriaDBUsuario():
    try:
        cursor.execute(
            "CREATE TABLE Usuario (\
                id_Usuario integer,\
                nome varchar(30),\
                segredo integer\
                )")
        connect.commit()
        connect.close()
    except Exception as identificador:
        pass


def ListarUsuarios():
    try:
        cursor.execute('SELECT * FROM Usuarios')
        return [Usuario.cria_de_tupla(el) for el in cursor.fetchall()]
    finally:
        connect.close()

def NovoUsuario():
    try:
        cursor.execute('INSERT INTO Usuario(nome, segredo)\
        VALUES (:nome, :segredo)', Usuario.__dict__())
        connect.commit()
    except:
        connect.rollback()
    finally:
        connect.close()
