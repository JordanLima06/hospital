from config.db import conect_db
from view.paciente_view import view_paciente
from view.admin_view import panel
from config.crypt import checar_password, criptografar
import pwinput


def logar_admin(username, senha):
    conn = conect_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM administrador WHERE username=%s"
    cursor.execute(sql, (username,))
    user = cursor.fetchone()
    if user and checar_password(senha, user[2]):
        return user
    
    return None

def login_admin():
    while True:
        username = input("Digite seu usuario: ")
        senha = pwinput.pwinput("Digite sua senha: ")
        user_auth = logar_admin(username, senha)
        if user_auth:
            panel(user_auth)
            break
        else:
            print("Usuário ou senha inválidos!")
    
def logar_paciente(nome, senha):
    conn = conect_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM paciente WHERE nome=%s"
    cursor.execute(sql, (nome,))
    user = cursor.fetchone()
    if user and checar_password(senha, user[8]):
        return user

    return None

def login_paciente():
    while True:
        nome = input("Digite seu nome: ")
        senha = pwinput.pwinput("Digite sua senha: ")
        user_auth = logar_paciente(nome, senha)
        if user_auth:
            view_paciente(user_auth)
            break
        else:
            print("Usuário ou senha inválidos!")

def cadastrar_admin(username, senha):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        senha = criptografar(senha)
        cursor.execute(
            """
            INSERT INTO administrador(username, senha)
            VALUES (%s, %s)
            """,
            (username, senha)
        )
        conn.commit()
        print("Administrador cadastrado com sucesso!")
    except Exception as e:
        conn.rollback()
        print(f"Erro ao cadastrar administrador: {e}")
    finally:
        cursor.close()
        conn.close()