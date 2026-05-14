from Tarefa import Tarefa
from Status import Status

"""
Classe que agrupa objetos de tarefa em uma lista

Atributos:
    lista (list): lista que irá armazenar as tarefas
"""
class ListaDeTarefas:

    def __init__(self) -> None:
        """
        Construtor da classe ListaDeTarefas, que inicializa a lista de tarefas como uma lista vazia
        """
        self.lista: list = []

    
    def adicionar(self, tarefa: Tarefa) -> str:
        """
        Método para adicionar uma tarefa à lista, atribuindo um ID único para cada tarefa
        e retornando uma mensagem de sucesso

        Parametros:
            tarefa (Tarefa): A tarefa a ser adicionada à lista
        Retorno:
            str: Mensagem de sucesso indicando que a tarefa foi adicionada com sucesso
        """
        tarefa.id = len(self.lista)
        self.lista.append(tarefa)

        return f"\nTarefa n°{tarefa.id} adicionada com sucesso\n"

    def listar(self) -> None:
        """
        Método para listar todas as tarefas da lista

        Parâmetros:
            None
        Retorno:
            None
        """
        for i in range(len(self.lista)):
            print(self.lista[i])

    def marcar_como_concluída(self, id: int) -> str:
        """
        Método para marcar uma tarefa como concluída,
        
        Parâmetros:
            id (int): id da tarefa que será marcado como concluído
        Retorno:
            str: mensagem de sucesso

        """
        self.lista[id].status = Status.CONCLUIDO

        return f"\nTarefa n°{id} marcada como concluída\n"

    def remover(self, id: int) -> str:
        """
        Método para remover uma tarefa da lista

        Parâmetros:
            id (int): id da tarefa que será removida
        Retorno:
            str: mensagem de sucesso indicando que a tarefa foi removida com sucesso
        """
        self.lista.pop(id)
        self.__atualizar_id()

        return f"\nTarefa n°{id} removida com sucesso\n"
    
    def __atualizar_id(self) -> None:
        """
        Método privado para atualizar os IDs das tarefas na lista

        Parâmetros: 
            None
        Retorno:
            None
        """
        for i in range(len(self.lista)):
            self.lista[i].id = i



