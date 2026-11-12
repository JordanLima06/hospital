import os
from service.medico_service import listar_medicos
from service.especialidade_service import listar_especialidade
from service.cadastros import marcar_consulta
from service.atualizacoes import atual_consulta

def view_paciente(user_auth):
        print(f"Bem vindo: {user_auth[1]}")
        while True:
            os.system("cls")
            print("1 - Marcar Consulta \n2 - Sair")
            opc = int(input("Digite a opção: "))
            if opc == 1:
                os.system("cls")
                especialidades = listar_especialidade()
                print("Especialidades:")
                for especialidade in especialidades:
                    print(f"{especialidade["id"]} - {especialidade["nome"]}")

                escolha = int(input("Digite uma opção: "))
                medicos = listar_medicos()
                medicos_filtrados = []
                os.system("cls")
                print("Médicos Disponiveis: ")

                for medico in medicos:
                    if medico ["especialidade_id"] == escolha:
                        medicos_filtrados.append(medico)
                        print(f"{medico["id"]} - {medico["nome"]}")
                    
                escolha_medico = int(input("\nEscolha o médico: "))
                medico_escolhido = None

                for medico in medicos_filtrados:
                    if medico["id"] == escolha_medico:
                        medico_escolhido = medico
                        break
                
                if medico_escolhido:
                    print(f"\nVocê escolheu {medico_escolhido["nome"]}")
                    marcar_consulta(user_auth[0], medico_escolhido["id"])
                else:
                    print("Médico não encontrado!")

                input("\nPressione Enter para continuar...")        
            elif opc == 2:
                break
            else:
                print("Digite uma opção válida!")