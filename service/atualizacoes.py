import pwinput
from service.paciente_service import atualizar_paciente
from service.medico_service import atualizar_medico
from service.departamento_service import atualizar_departamento
from service.especialidade_service import atualizar_especialidade
from service.consulta_service import atualizar_consulta
from utils.validacao import validar_cpf, validar_crm, validar_data, validar_descricao,validar_email, validar_localizacao, validar_nome, validar_senha, validar_sexo, validar_telefone, validar_hora
from service.especialidade_service import listar_especialidade
from service.departamento_service import listar_departamento

def atual_paciente():
    id_paciente = int(input("Digite o id do paciente: "))
    while True:
        nome = input("Digite o nome: ")
        if validar_nome(nome):
            break
        else:
            print("Nome Inválido!")
    while True:
        cpf = input("Digite o cpf: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF Inválido!")

    while True:       
        sexo = input("M - Para masculino / F - Para feminino: ").lower()
        if validar_sexo(sexo):
            break
        else:
            print("Sexo Inválido!")

    while True:
        telefone = input("Digite o telefone: ")
        if validar_telefone(telefone):
            break
        else:
            print("Telefone Inválido!")
    
    while True:
        email = input("Digite o email: ").strip()
        if validar_email(email):
            break
        else:
            print("Email Inválido")

    while True:
        senha = pwinput.pwinput("Digite uma nova senha: ")
        if validar_senha(senha):
            break
        else:
            print("Senha Inválida!")

    while True:
        dt_nascimento = input("Digite data de nascimento (yyyy-mm-dd): ")
        if validar_data(dt_nascimento):
            break
        else:
            print("Digite a data correta: ")

    endereco = input("Digite o endereco: ")

    atualizar_paciente(id_paciente, nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha)

def atual_medico():
    id_medico = int(input("Digite o ID do médico: "))

    while True:
        nome = input("Digite o nome: ")
        if validar_nome(nome):
            break
        else:
            print("Nome Inválido!")

    while True:
        crm = input("Digite o CRM: ")
        if validar_crm(crm):
            break
        else:
            print("CRM Inválido!")
    

    while True:
        telefone = input("Digite o telefone: ")
        if validar_telefone(telefone):
            break
        else:
            print("Telefone Inválido!")

    while True:
        email = input("Digite o email: ").strip()
        if validar_email(email):
            break
        else:
            print("Email Inválido!")
    
    especialidades = listar_especialidade()
    for especialidade in especialidades:
        print(f"ID: {especialidade["id"]} \nNome: {especialidade["nome"]}")
    especialidade = input("Digite a especialidade: ")
    departamentos = listar_departamento()
    
    for departamento in departamentos:
        print(f"ID: {departamento["id"]} \nNome: {departamento["nome"]}")
    departamento = input("Digite o setor: ")

    atualizar_medico(id_medico, nome, crm,telefone, email, especialidade, departamento)

def atual_especialidade():
    id_especialidade = int(input("Digite o ID da especialidade: "))
    while True:
        nome = input("Digite a especialidade: ")
        if validar_nome(nome):
            break
        else:
            print("Nome Inválido!")
    
    while True:
        descricao = input("Descrição: ")
        if validar_descricao(descricao):
            break
        else:
            print("Descrição Inválida")   

    atualizar_especialidade(id_especialidade, nome, descricao)

def atual_departamento():
    id_departamento = int(input("Digite o ID do Departamento: "))

    while True:
        nome = input("Digite o nome: ")
        if validar_nome(nome):
            break
        else:
            print("Nome Inválido!")

    while True:
        localizacao = input("Digite a localização: ")
        if validar_localizacao(localizacao):
            break
        else:
            print("Erro ao inserir!")

    atualizar_departamento(id_departamento, nome, localizacao)

def atual_consulta():
    id_consulta = input("Digite o ID da consulta: ")

    if not id_consulta.isdigit():
        print("Digite apenas números.")
        return

    status = input("Novo status: ")
    while True:
        data = input("Digite a data (AAAA-MM-DD): ")
        if validar_data(data):
            break
        else:
            print("Erro na Data!")
    
    while True:
        hora = input("Digite a hora (HH:MM): ")
        if validar_hora(hora):
            break
        else:
            print("Erro no Horário!")
    atualizar_consulta(id_consulta, status, data, hora)
