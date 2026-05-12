from Tarefa import Tarefa
from Status import Status

# Classe para gerenciar a lista de tarefas, com métodos para adicionar, listar, marcar como concluída e remover tarefas
class ListaDeTarefas:
    # Construtor da classe ListaDeTarefas, que inicializa a lista de tarefas como uma lista vazia
    def __init__(self):
        self.lista: list = []

    # Método para adicionar uma tarefa à lista, atribuindo um ID único para cada tarefa e retornando uma mensagem de sucesso
    def adicionar(self, tarefa: Tarefa) -> str:
        tarefa.id = len(self.lista)
        self.lista.append(tarefa)

        return f"\nTarefa n°{tarefa.id} adicionada com sucesso\n"

    # Método para listar todas as tarefas da lista, imprimindo cada tarefa utilizando o método __str__ da classe Tarefa
    def listar(self) -> None:
        for i in range(len(self.lista)):
            print(self.lista[i])

    # Método para marcar uma tarefa como concluída, recebendo o ID da tarefa e atualizando seu status para CONCLUIDO, retornando uma mensagem de sucesso
    def marcar_como_concluída(self, id: int) -> str:
        self.lista[id].status = Status.CONCLUIDO

        return f"\nTarefa n°{id} marcada como concluída\n"

    # Método para remover uma tarefa da lista, recebendo o ID da tarefa e atualizando os IDs das tarefas restantes, retornando uma mensagem de sucesso
    def remover(self, id: int) -> str:
        self.lista.pop(id)
        self.__atualizar_id()

        return f"\nTarefa n°{id} removida com sucesso\n"
    
    # Método privado para atualizar os IDs das tarefas na lista, garantindo que cada tarefa tenha um ID único e sequencial após a remoção de uma tarefa
    def __atualizar_id(self) -> None:
        for i in range(len(self.lista)):
            self.lista[i].id = i



