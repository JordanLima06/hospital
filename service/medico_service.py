from config.db import conect_db

def inserir_medico(nome, crm, telefone, email, especialidade, departamento):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO medico (nome, crm, telefone, email, especialidade, departamento) VALUES (%s, %s, %s, %s, %s, %s);", (nome, crm, telefone, email, especialidade, departamento))
        conn.commit()
        print("Medico inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o Médico(a): {e}")
    finally:
        cursor.close()
        conn.close()

def listar_medicos():
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT m.id_medico, m.nome, m.crm, m.telefone, m.email, e.id_especialidade, e.nome AS especialidade, d.nome AS departamento FROM medico m JOIN especialidade e ON m.especialidade = e.id_especialidade JOIN departamento d ON m.departamento = d.id_departamento")
        data = cursor.fetchall()

        medicos = []
        for medico in data:
            medicos.append({
                "id": medico[0],
                "nome": medico[1],
                "crm": medico[2],
                "telefone": medico[3],
                "email": medico[4],
                "especialidade_id": medico[5],
                "especialidade": medico[6],
                "departamento": medico[7]
            })
        return medicos
    except Exception as e:
        print(f"Erro ao inserir Médico(a): {e}")
    finally:
        cursor.close()
        conn.close()

def atualizar_medico(id_medico, nome, crm, telefone, email, especialidade, departamento):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE medico SET nome = %s, crm = %s, telefone = %s, email = %s, especialidade = %s, departamento = %s WHERE id_medico = %s", (nome, crm, telefone, email, especialidade, departamento,id_medico))
        conn.commit()
        print("Médico atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar Médico(a): {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_medico(id_medico):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM consulta WHERE medico = %s",(id_medico,))
        cursor.execute("DELETE FROM medico WHERE id_medico = %s", (id_medico,))
        conn.commit()
        print("Médico deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar Médico(a): {e}")
    finally:
        cursor.close()
        conn.close()
        
def buscar_medico_nome(nome):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT m.id_medico, m.nome, m.crm, m.telefone, m.email, e.nome AS especialidade, d.nome AS departamento FROM medico m JOIN especialidade e ON m.especialidade = e.id_especialidade JOIN departamento d ON m.departamento = d.id_departamento WHERE m.nome ILIKE %s", (f"%{nome}%",))
                       
        data = cursor.fetchall()

        medicos = []

        for medico in data:

            medicos.append({
                "id": medico[0],
                "nome": medico[1],
                "crm": medico[2],
                "telefone": medico[3],
                "email": medico[4],
                "especialidade": medico[5],
                "departamento": medico[6]
            })
        return medicos
    except Exception as e:
        print(f"Erro ao buscar Médico(a): {e}")
    finally:
        cursor.close()
        conn.close()