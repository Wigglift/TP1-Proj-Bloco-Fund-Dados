from Tarefa import Tarefa
from ListaDeTarefas import ListaDeTarefas

def main():
    sair = False

    while not sair:
        print("Bem vindo ao sistema de registro de tarefas")
        print("Escolha uma das opções a seguir:")

        print("1 - Adicionar nova tarefa\n" \
        "2 - Listar tarefas \n" \
        "3 - Marcar tarefa como concluída \n" \
        "4 - Remover tarefa\n" \
        "5 - Sair do sistema")

        user_input = input(">")

        match user_input:
            case "1":
                nova_tarefa = criar_tarefa()
                print(ListaDeTarefas.adicionar(nova_tarefa))
                break

            case "2":
                ListaDeTarefas.listar()
                break

            case "3":
                print("Escolha qual tarefa marcar como concluída")
                ListaDeTarefas.listar()
                user_input = input(">")
                print(ListaDeTarefas.marcar_como_concluída(user_input))
                break

            case "4":
                print("Escolha qual tarefa será removida")
                ListaDeTarefas.listar()
                user_input = input(">")
                print(ListaDeTarefas.remover(user_input))
                break

            case "5":
                print("Obrigado por usar o sistema, volte sempre")
                sair = True
                break

            case _:
                    pass
                
def criar_tarefa() -> Tarefa:
    return Tarefa


main()