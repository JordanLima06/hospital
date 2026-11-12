import os
from service.cadastros import cadastro_paciente
from service.login_service import login_paciente, login_admin

while(True):
    os.system("cls")
    print("1 - Entrar como paciente")
    print("2 - Entrar como administrador")
    print("3 - Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        os.system("cls")
        print("1 - Cadastrar\n2 - Logar")
        escolha = int(input("Digite sua opção: "))
        if escolha == 1:
            os.system("cls")
            cadastro_paciente()
            input("Enter para continuar")
        elif escolha == 2:
            os.system("cls")
            login_paciente()
    elif opc == "2":
        os.system("cls")
        login_admin()
    elif opc == "3":
        break
    else:
        print("Opção Inválida")
