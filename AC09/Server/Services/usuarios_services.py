from .Model.usuario import Usuario
from .Infra.usuarios_db import NovoUsuario, ListarUsuarios

def CriarUser (Usuario_data):
    NovoUsuario(Usuario.cria(Usuario_data))
    return NovoUsuario

def Listar():
    return ListarUsuarios
