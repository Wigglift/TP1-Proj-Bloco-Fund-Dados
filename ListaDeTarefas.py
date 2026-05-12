from Tarefa import Tarefa
from Status import Status

class ListaDeTarefas:
    def __init__(self):
        self.lista: list = []

    def adicionar(self, tarefa: Tarefa) -> str:
        tarefa.id = len(self.lista)
        self.lista.append(tarefa)

        return f"\nTarefa n°{tarefa.id} adicionada com sucesso\n"

    def listar(self) -> None:
        for i in range(len(self.lista)):
            print(self.lista[i])

    def marcar_como_concluída(self, id: int) -> str:
        self.lista[id].status = Status.CONCLUIDO

        return f"\nTarefa n°{id} marcada como concluída\n"

    def remover(self, id: int) -> str:
        self.lista.pop(id)
        self.__atualizar_id()

        return f"\nTarefa n°{id} removida com sucesso\n"
        
    def __atualizar_id(self) -> None:
        for i in range(len(self.lista)):
            self.lista[i].id = i



