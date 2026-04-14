from Tarefa import Tarefa

class ListaDeTarefas:
    def __init__(self):
        self.lista: list = []

    def adicionar(self, tarefa: Tarefa) -> str:
        tarefa.id = len(self.lista)
        self.lista.append(tarefa)

        return f"Tarefa n°{tarefa.id} adicionada com sucesso"

    def listar(self) -> None:
        for i in range(len(self.lista)):
            print(self.lista[i])

    def marcar_como_concluída(self, id: int) -> str:
        self.lista[id].concluida = True

        return "Tarefa marcada como concluída"

    def remover(self, id: int) -> str:
        self.lista.pop(id)
        self.__atualizar_id()

        return "Tarefa removida com sucesso"
        
    def __atualizar_id(self) -> None:
        for i in range(len(self.lista)):
            self.lista[i].id = i



