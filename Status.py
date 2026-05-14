from enum import Enum

class Status(Enum):
    """
    Enumeração para representar o status de uma tarefa, podendo ser pendente ou concluída
    """
    PENDENTE = 1
    CONCLUIDO = 2