from config.db import conect_db

def criar_consulta(data, hora, status, paciente, medico):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO consulta(data_consulta, hora, status, paciente, medico) VALUES (%s, %s, %s, %s, %s);", (data, hora, status, paciente, medico))
        conn.commit()
        print("Consulta Marcada com sucesso!")
    except Exception as e:
        print(f"Erro ao marcar Consulta: {e}")
    finally:
        cursor.close()
        conn.close()

def listar_consultas():
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("select c.id_consulta AS consulta, c.data_consulta, c.hora, c.status, p.nome AS paciente, m.nome AS medico FROM consulta c JOIN paciente p ON c.paciente = p.id_paciente JOIN medico m ON c.medico = m.id_medico")
        data = cursor.fetchall()
        
        consultas = []

        for consulta in data:
            consultas.append({
                "id": consulta[0],
                "data": consulta[1],
                "hora": consulta[2],
                "status": consulta[3],
                "paciente": consulta[4],
                "medico": consulta[5]
            })
        return consultas
    except Exception as e:
        print(f"Erro ao listar consultas: {e}")
    finally:
        cursor.close()
        conn.close()

def atualizar_consulta(id_consulta, status, data_consulta, hora):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE consulta SET status = %s, data_consulta = %s, hora = %s WHERE id_consulta = %s", (status, data_consulta, hora, id_consulta))
        conn.commit()
        print("Status da consulta atualizado!")
    except Exception as e:
        print(f"Erro ao atualizar consulta: {e}")
    finally:
        cursor.close()
        conn.close()

def deletar_consulta(id_consulta):
    conn = conect_db()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM consulta WHERE id_consulta = %s", (id_consulta,))
        conn.commit()
        print("Consulta apagada com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar consulta: {e}")
    finally:
        cursor.close()
        conn.close()