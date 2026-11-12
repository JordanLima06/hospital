import re
from datetime import datetime
import os


def validar_nome(nome):
    return len(nome.strip()) >= 3

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    return len(cpf) == 11

def validar_sexo(sexo):
    return sexo.lower() in ['m', 'f']

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

def validar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone))
    return len(telefone) in [10, 11]

def validar_crm(crm):
    return len(crm.strip()) >= 5

def validar_descricao(descricao):
    return len(descricao) >= 20

def validar_localizacao(localizacao):
    return len(localizacao) >= 10

def validar_senha(senha):
    return len(senha) >= 5

def validar_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
    
def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
