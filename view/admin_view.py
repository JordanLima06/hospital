import os
from service.medico_service import listar_medicos
from service.paciente_service import listar_pacientes
from service.especialidade_service import listar_especialidade
from service.departamento_service import listar_departamento
from service.consulta_service import listar_consultas
from service.cadastros import cadastro_departamento, cadastro_especialidade, cadastro_medico, cadastro_paciente, buscar_medico, buscar_paciente
from service.atualizacoes import atual_medico, atual_paciente, atual_departamento, atual_especialidade, atual_consulta
from service.deletar import del_departamento, del_especialidade, del_medico, del_paciente, del_consulta

def panel(user_auth):
    while True:
        os.system("cls")
        print("O que deseja fazer:")
        print("--------------CADASTROS---------------------")
        print("1 - Cadastrar Médico | 2 - Cadastrar Especialidade\n3 - Cadastrar Departamento | 4 - Cadastrar Paciente")

        print("--------------LISTAR---------------------")
        print("5 - Listar Médico | 6 - Listar Especialidade\n7 - Listar Departamento | 8 - Listar Paciente\n9 - Listar consultas")
        print("--------------ATUALIZAÇÕES---------------------")

        print("10 - Atualizar Médico | 11 - Atualizar Especialidade\n12 - Atualizar Departamento | 13 - Atualizar Paciente\n14 - Atualizar consultas")

        print("--------------DELETAR---------------------")
        print("15 - Deletar Médico | 16 - Deletar Especialidade\n17 - Deletar Departamento | 18 - Deletar Paciente\n19 - Deletar consultas")
        print("20 - Buscar médico por nome | 21 - Buscar paciente por nome ")
        print("0 - SAIR")
        
        opc = input("Escolha uma opção: ")
        if opc == "1":
            os.system("cls")
            cadastro_medico()
            input("Aperte ENTER para continuar")
        elif opc == "2":
            os.system("cls")
            cadastro_especialidade()
            input("Aperte ENTER para continuar")
        elif opc == "3":
            os.system("cls")
            cadastro_departamento()
            input("Aperte ENTER para continuar")
        elif opc == "4":
            os.system("cls")
            cadastro_paciente()
            input("Aperte ENTER para continuar")
        elif opc == "5":
            os.system("cls")
            medicos = listar_medicos()
            for medico in medicos:
                print(f"ID: {medico["id"]} \nNome: {medico["nome"]} \nCRM: {medico["crm"]} \nTelefone: {medico["telefone"]} \nEmail: {medico["email"]} \nEspecialidade: {medico["especialidade"]} \nDepartamento: {medico["departamento"]} \n-----------------------------------")

            input("Aperte ENTER para continuar")
        elif opc == "6":
            os.system("cls")
            especialidades = listar_especialidade()
            for especialidade in especialidades:
                print(f"ID: {especialidade["id"]} \nNome: {especialidade["nome"]} \nDescrição: {especialidade["descricao"]} \n-----------------------------------")
            
            input("Aperte ENTER para continuar")
        elif opc == "7":
            os.system("cls")
            departamentos = listar_departamento()
            for departamento in departamentos:
                print(f"ID: {departamento["id"]} \nNome: {departamento["nome"]} \nDescrição: {departamento["localizacao"]} \n-----------------------------------")

            input("Aperte ENTER para continuar")
        elif opc == "8":
            os.system("cls")
            pacientes = listar_pacientes()

            for paciente in pacientes:
                print(f"ID: {paciente["id"]} \nNome: {paciente["nome"]} \nCPF: {paciente["cpf"]} \Data de Nascimento: {paciente["dt_nascimento"]} \nTelefone: {paciente["telefone"]} \Endereço: {paciente["endereco"]} \Email: {paciente["email"]} \n-----------------------------------")

            input("Aperte ENTER para continuar")
        elif opc == "9":
            os.system("cls")
            consultas = listar_consultas()

            for consulta in consultas:
                print(f"ID: {consulta["id"]} \nData: {consulta["data"]} \nHora: {consulta["hora"]} \nStatus: {consulta["status"]} \nPaciente: {consulta["paciente"]} \nMédico: {consulta["medico"]}\n-----------------------------------")

            input("Aperte ENTER para continuar")
        elif opc == "10":
            os.system("cls")
            medicos = listar_medicos()
            for medico in medicos:
                print(f"ID: {medico["id"]} \nNome: {medico["nome"]} \nCRM: {medico["crm"]} \nTelefone: {medico["telefone"]} \nEmail: {medico["email"]} \nEspecialidade: {medico["especialidade"]} \nDepartamento: {medico["departamento"]} \n-----------------------------------")
            atual_medico()
            input("Aperte ENTER para continuar")
        elif opc == "11":
            os.system("cls")
            especialidades = listar_especialidade()
            for especialidade in especialidades:
                print(f"ID: {especialidade["id"]} \nNome: {especialidade["nome"]} \nDescrição: {especialidade["descricao"]} \n-----------------------------------")
            atual_especialidade()
            input("Aperte ENTER para continuar")
        elif opc == "12":
            os.system("cls")
            departamentos = listar_departamento()
            for departamento in departamentos:
                print(f"ID: {departamento["id"]} \nNome: {departamento["nome"]} \nDescrição: {departamento["localizacao"]} \n-----------------------------------")

            atual_departamento()
            input("Aperte ENTER para continuar")
        elif opc == "13":
            os.system("cls")
            pacientes = listar_pacientes()

            for paciente in pacientes:
                print(f"ID: {paciente["id"]} \nNome: {paciente["nome"]} \nCPF: {paciente["cpf"]} \Data de Nascimento: {paciente["dt_nascimento"]} \nTelefone: {paciente["telefone"]} \Endereço: {paciente["endereco"]} \Email: {paciente["email"]} \n-----------------------------------")

            atual_paciente()
            input("Aperte ENTER para continuar")
        elif opc == "14":
            os.system("cls")
            consultas = listar_consultas()

            for consulta in consultas:
                print(f"ID: {consulta["id"]} \nData: {consulta["data"]} \nHora: {consulta["hora"]} \nStatus: {consulta["status"]} \nPaciente: {consulta["paciente"]} \nMédico: {consulta["medico"]}\n-----------------------------------")

            atual_consulta()
            input("Aperte ENTER para continuar")
        elif opc == "15":
            os.system("cls")
            medicos = listar_medicos()
            for medico in medicos:
                print(f"ID: {medico["id"]} \nNome: {medico["nome"]} \nCRM: {medico["crm"]} \nTelefone: {medico["telefone"]} \nEmail: {medico["email"]} \nEspecialidade: {medico["especialidade"]} \nDepartamento: {medico["departamento"]} \n-----------------------------------")
            del_medico()
            input("Aperte ENTER para continuar")
        elif opc == "16":
            os.system("cls")
            especialidades = listar_especialidade()
            for especialidade in especialidades:
                print(f"ID: {especialidade["id"]} \nNome: {especialidade["nome"]} \nDescrição: {especialidade["descricao"]} \n-----------------------------------")
            del_especialidade()
            input("Aperte ENTER para continuar")
        elif opc == "17":
            os.system("cls")
            departamentos = listar_departamento()
            for departamento in departamentos:
                print(f"ID: {departamento["id"]} \nNome: {departamento["nome"]} \nDescrição: {departamento["localizacao"]} \n-----------------------------------")

            del_departamento()
            input("Aperte ENTER para continuar")
        elif opc == "18":
            os.system("cls")
            pacientes = listar_pacientes()

            for paciente in pacientes:
                print(f"ID: {paciente["id"]} \nNome: {paciente["nome"]} \nCPF: {paciente["cpf"]} \Data de Nascimento: {paciente["dt_nascimento"]} \nTelefone: {paciente["telefone"]} \Endereço: {paciente["endereco"]} \Email: {paciente["email"]} \n-----------------------------------")

            del_paciente()
            input("Aperte ENTER para continuar")
        elif opc == "19":
            os.system("cls")
            consultas = listar_consultas()

            for consulta in consultas:
                print(f"ID: {consulta["id"]} \nData: {consulta["data"]} \nHora: {consulta["hora"]} \nStatus: {consulta["status"]} \nPaciente: {consulta["paciente"]} \nMédico: {consulta["medico"]}\n-----------------------------------")
            del_consulta()
            input("Aperte ENTER para continuar")
        elif opc == "20":
            os.system("cls")
            buscar_medico()
            opc = input("1 - Atualizar | 2 - Deletar | 3 - Sair: ")
            if opc == "1":
                atual_medico()
            elif opc == "2":
                del_medico()
            elif opc == "3":
                break

            input("Aperte ENTER para continuar")
        elif opc == "21":
            os.system("cls")
            buscar_paciente()
            opc = input("1 - Atualizar | 2 - Deletar | 3 - Sair: ")
            if opc == "1":
                atual_paciente()
            elif opc == "2":
                del_paciente()
            elif opc == "3":
                break

            input("Aperte ENTER para continuar")
        elif opc == "0":
            break
        else:
            print("Digite uma opção válida!")
       
       
