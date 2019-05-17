import requests as R
import random

def CriarUser():
    response = R.get('http://localhost:9099/usr')
    json = response.json()

    nome = input('Digite o nome do usuário para cadastrar: ')
    Print('nome')

    if nome in sql.user:
        return error 409
    if nome in sql.Aluno or nome in sql.Professor:
        
    # segredo = random.randint 







