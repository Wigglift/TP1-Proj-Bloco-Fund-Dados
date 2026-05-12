from datetime import date
from Status import Status

class Tarefa():
    def __init__(self, id: int, descricao: str, prazo_final: date, urgencia: int):
        self.id = id
        self.descricao = descricao
        self.data_de_criacao = date.today()
        self.status = Status.PENDENTE
        self.prazo_final = prazo_final
        self.urgencia = urgencia

    def __str__(self):
        response = (
            f"Tarefa {self.id}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status.name}\n"
            f"Data de criação: {self.data_de_criacao.strftime('%d/%m/%Y')}\n"
            f"Prazo final: {self.prazo_final.strftime('%d/%m/%Y')}\n"
            f'Urgência: {self.urgencia}"\n'
    
        )

        return response