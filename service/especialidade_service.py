from config.db import conect_db

def inserir_especialidade(nome, descricao):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO especialidade(nome, descricao) VALUES (%s, %s);", (nome, descricao))
        conn.commit()
        print("Especialidade inserida com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir especialidade: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_especialidade():
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM especialidade")
        data = cursor.fetchall()

        especialidades = []
        for especialidade in data:
            especialidades.append({
                "id": especialidade[0],
                "nome": especialidade[1],
                "descricao": especialidade[2],
            })
        return especialidades
    except Exception as e:
        print(f"Erro ao listar especialidades: {e}")
    finally:
        cursor.close()
        conn.close()

def atualizar_especialidade(id_especialidade, nome, descricao):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE especialidade SET nome = %s, descricao = %s WHERE id_especialidade = %s", (nome, descricao, id_especialidade))
        conn.commit()
        print("Especialidade atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar Setor: {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_especialidade(id_especialidade):
    conn = conect_db()

    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM especialidade WHERE id_especialidade = %s", (id_especialidade,))
        conn.commit()
        print("Especialidade deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar Especialidade: {e}")
    finally:
        cursor.close()
        conn.close()