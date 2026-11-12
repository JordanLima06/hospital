from config.db import conect_db

def inserir_departamento(nome, localizacao):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO departamento(nome, localizacao) VALUES (%s, %s);", (nome, localizacao))
        conn.commit()
        print("Setor inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o Setor: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_departamento():
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM departamento")
        data = cursor.fetchall()

        departamentos = []
        for departamento in data:
            departamentos.append({
                "id": departamento[0],
                "nome": departamento[1],
                "localizacao": departamento[2],
            })
        return departamentos
    except Exception as e:
        print(f"Erro as listar os Setores: {e}")
    finally:
        cursor.close()
        conn.close()

def atualizar_departamento(id_departamento, nome, localizacao):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE departamento SET nome = %s, localizacao = %s WHERE id_departamento = %s", (nome, localizacao, id_departamento))
        conn.commit()
        print("Setor atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar Setor: {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_departamento(id_departamento):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE medico SET departamento = NULL WHERE departamento = %s",(id_departamento,))
        cursor.execute("DELETE FROM departamento WHERE id_departamento = %s", (id_departamento,))
        conn.commit()
        print("Setor deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar Setor: {e}")
    finally:
        cursor.close()
        conn.close()