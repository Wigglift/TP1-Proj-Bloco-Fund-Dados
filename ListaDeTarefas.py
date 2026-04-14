from Tarefa import Tarefa

class ListaDeTarefas:
    def __init__(self):
        self.lista = []

    def adicionar(self, tarefa: Tarefa) -> str:
        pass

    def listar(self) -> None:
        for i in range(len(self.lista)):
            print(self.lista[i])

    def marcar_como_concluída() -> str:
        pass

    def remover(self, tarefa: Tarefa) -> str:
        pass
