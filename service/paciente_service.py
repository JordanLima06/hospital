from config.db import conect_db
from config.crypt import criptografar

def inserir_paciente(nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        senha = criptografar(senha)
        cursor.execute("INSERT INTO paciente (nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha))
        conn.commit()
        print("Cadastrado com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir paciente: {e}")

    finally:
        cursor.close()
        conn.close()

def listar_pacientes():
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM paciente")
        data = cursor.fetchall()

        pacientes = []

        for paciente in data:
            pacientes.append({
                "id": paciente[0],
                "nome": paciente[1],
                "cpf": paciente[2],
                "sexo": paciente[3],
                "dt_nascimento": paciente[4],
                "telefone": paciente[5],
                "endereco": paciente[6],
                "email": paciente[7],
                "senha": paciente[8]
            })
        return pacientes
    except Exception as e:
        print(f"Erro ao listar paciente: {e}")
    finally:
        cursor.close()
        conn.close()

def atualizar_paciente(id_paciente, nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE paciente SET nome = %s, cpf = %s, sexo = %s, dt_nascimento = %s, telefone = %s, endereco = %s, email = %s, senha = %s WHERE id_paciente = %s", (nome, cpf, sexo, dt_nascimento, telefone, endereco, email, senha, id_paciente))
        conn.commit()
        print("Paciente atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar Paciente: {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_paciente(id_paciente):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM consulta WHERE paciente = %s",(id_paciente,))
        cursor.execute("DELETE FROM paciente WHERE id_paciente = %s", (id_paciente,))
        conn.commit()
        print("Paciente deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar Paciente: {e}")
    finally:
        cursor.close()
        conn.close()

def buscar_paciente_nome(nome):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute(" SELECT id_paciente, nome, cpf, dt_nascimento, telefone, endereco, email FROM paciente WHERE nome ILIKE %s", (f"%{nome}%",))

        data = cursor.fetchall()

        pacientes = []

        for paciente in data:
            pacientes.append({
                "id": paciente[0],
                "nome": paciente[1],
                "cpf": paciente[2],
                "dt_nascimento": paciente[3],
                "telefone": paciente[4],
                "endereco": paciente[5],
                "email": paciente[6]
            })
        return pacientes
    except Exception as e:
        print(f"Erro ao buscar paciente: {e}")
    finally:
        cursor.close()
        conn.close()