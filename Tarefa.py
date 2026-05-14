from datetime import date
from Status import Status

class Tarefa():
    """
    Classe que representa uma tarefa

    Atributos:
        id (int): id da tarefa
        descricao (str): conteúdo da tarefa
        data_de_criacao (date): data em que a tarefa foi criada
        status (Status): estado da tarefa, podendo estar pendente ou concluída
        prazo_final (date): prazo final para a conclusão da tarefa
        urgencia (int): nível de urgência da tarefa
    """

    def __init__(self, descricao: str, prazo_final: date, urgencia: int):
        """
        Construtor da classe Tarefa, que inicializa os atributos da tarefa com os
        valores fornecidos pelo usuário e atribui um ID único para cada tarefa
        """
        self.id: int
        self.descricao = descricao
        self.data_de_criacao = date.today()
        self.status = Status.PENDENTE
        self.prazo_final = prazo_final
        self.urgencia = urgencia

    def __str__(self):
        """
        Método para representar a tarefa como uma string,
        formatando os atributos da tarefa de forma legível para o usuário
        """
        response = (
            f"Tarefa {self.id}\n"
            f"Descrição: {self.descricao}\n"
            f"Status: {self.status.name}\n"
            f"Data de criação: {self.data_de_criacao.strftime('%d/%m/%Y')}\n"
            f"Prazo final: {self.prazo_final.strftime('%d/%m/%Y')}\n"
            f'Urgência: {self.urgencia}"\n'
        )

        return response