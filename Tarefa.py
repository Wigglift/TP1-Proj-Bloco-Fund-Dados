from datetime import date
from Status import Status

# Classe que representa uma tarefa, com os atributos necessários para a criação e gerenciamento de uma tarefa
class Tarefa():

    # Construtor da classe Tarefa, que recebe a descrição, prazo final e urgência da tarefa, e inicializa os outros atributos como data de criação e status
    def __init__(self, descricao: str, prazo_final: date, urgencia: int):
        self.id: int
        self.descricao = descricao
        self.data_de_criacao = date.today()
        self.status = Status.PENDENTE
        self.prazo_final = prazo_final
        self.urgencia = urgencia
    # Método para representar a tarefa como uma string, facilitando a visualização das informações da tarefa
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