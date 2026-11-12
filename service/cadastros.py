from utils.validacao import *
import pwinput
from service.paciente_service import inserir_paciente, buscar_paciente_nome
from service.medico_service import inserir_medico, buscar_medico_nome
from service.especialidade_service import inserir_especialidade
from service.departamento_service import inserir_departamento
from service.consulta_service import criar_consulta

def cadastro_paciente():
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
        senha = pwinput.pwinput("Digite uma senha: ")
        if validar_senha(senha):
            break
        else:
            print("Senha Inválida!")

    while True:
        dt_nascimento = input("Digite data de nascimento (yyyy-mm-dd): ")
        if validar_data(dt_nascimento):
            break
        else:
            print("Digite a data correta")
    endereco = input("Digite o endereco: ")
    inserir_paciente(nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha)

def cadastro_medico():
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
    
    especialidade = input("Digite a especialidade: ")
    departamento = input("Digite o setor: ")

    inserir_medico(nome, crm, telefone, email, especialidade, departamento)

def cadastro_especialidade():
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

    inserir_especialidade(nome, descricao)

def cadastro_departamento():
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

    inserir_departamento(nome, localizacao)

def marcar_consulta(id_paciente, id_medico):
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
    
    status = "Marcada"
    
    criar_consulta(data, hora, status, id_paciente, id_medico)

def buscar_medico():
    nome = input("Digite o nome do médico: ")

    medicos = buscar_medico_nome(nome)

    for medico in medicos:
        print(f"ID: {medico["id"]} \nNome: {medico["nome"]} \nCRM: {medico["crm"]} \nTelefone: {medico["telefone"]} \nEmail: {medico["email"]} \nEspecialidade: {medico["especialidade"]} \nDepartamento: {medico["departamento"]} \n-----------------------------------")
        
    if not medicos:
        print("Nenhum médico encontrado")
        return
    
def buscar_paciente():
    nome = input("Digite o nome do paciente: ")
    pacientes = buscar_paciente_nome(nome)

    if not pacientes:
        print("\nNenhum paciente encontrado!")
    else:
        for paciente in pacientes:
            print(f"ID: {paciente["id"]} \nNome: {paciente["nome"]} \nCPF: {paciente["cpf"]} \Data de Nascimento: {paciente["dt_nascimento"]} \nTelefone: {paciente["telefone"]} \Endereço: {paciente["endereco"]} \Email: {paciente["email"]} \n-----------------------------------")
