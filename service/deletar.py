from service.departamento_service import deletar_departamento
from service.especialidade_service import deletar_especialidade
from service.medico_service import deletar_medico
from service.paciente_service import deletar_paciente
from service.consulta_service import deletar_consulta

def del_medico():
    id_medico = int(input("Digite o ID do médico: "))
    deletar_medico(id_medico)

def del_paciente():
    id_paciente = int(input("Digite o ID do paciente: "))
    deletar_paciente(id_paciente)

def del_departamento():
    id_departamento = int(input("Digite o ID do departamento: "))
    deletar_departamento(id_departamento)

def del_especialidade():
    id_especialidade = int(input("Digite o ID da especialidade: "))
    deletar_especialidade(id_especialidade)

def del_consulta():
    id_consulta = int(input("Digite o ID da consulta: "))
    deletar_consulta(id_consulta)