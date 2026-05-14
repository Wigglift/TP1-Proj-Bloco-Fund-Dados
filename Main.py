from Tarefa import Tarefa
from datetime import datetime
from ListaDeTarefas import ListaDeTarefas
import time

def main():
    """
    Função principal do programa
    apresenta um menu para o usuário escolher as opções de gerenciamento de tarefas,
    utilizando a classe ListaDeTarefas para armazenar e manipular as tarefas criadas pelo usuário
    """
    
    sair: bool = False
    lista_de_tarefas: ListaDeTarefas = ListaDeTarefas()
    print("Bem vindo ao sistema de registro de tarefas")

    while not sair:
        print("\nEscolha uma das opções a seguir:")

        print("1 - Adicionar nova tarefa\n" \
        "2 - Listar tarefas \n" \
        "3 - Marcar tarefa como concluída \n" \
        "4 - Remover tarefa\n" \
        "5 - Sair do sistema\n")
        user_input: str = input(">")
        print("\n")

        # Estrutura de controle de fluxo para as opções do menu
        match user_input:
            case "1":
                nova_tarefa:Tarefa = criar_tarefa()
                print(lista_de_tarefas.adicionar(nova_tarefa))
                time.sleep(1)
                pass

            case "2":
                lista_de_tarefas.listar()
                time.sleep(1)
                pass

            case "3":
                print("Escolha qual tarefa marcar como concluída")
                lista_de_tarefas.listar()
                user_input: int = int(input(">"))
                print(lista_de_tarefas.marcar_como_concluída(user_input))
                time.sleep(1)
                pass

            case "4":
                print("Escolha qual tarefa será removida")
                lista_de_tarefas.listar()
                user_input: int = int(input(">"))
                print(lista_de_tarefas.remover(user_input))
                time.sleep(1)
                pass

            case "5":
                print("Obrigado por usar o sistema, volte sempre")
                sair = True
                pass

            case _:
                    print("Opção inválida")
                    pass
                
def criar_tarefa():
    """
    Função auxiliar para criar uma tarefa, solicitando os dados necessários para a criação da tarefa
    retornando a tarefa criada
    Parâmetros:
        None
    Retorno:
        tarefa (Tarefa): A tarefa criada a partir dos dados fornecidos pelo usuário
    """
    descricao = input("Digite a descrição da tarefa: ")
    prazo_str = input("Digite o prazo final (dd/mm/aaaa): ")
    prazo_final = datetime.strptime(prazo_str, "%d/%m/%Y").date()
    urgencia = int(input("Digite o nível de urgência (1 a 5): "))

    tarefa = Tarefa(descricao, prazo_final, urgencia)

    return tarefa

# Ponto de entrada do programa
if __name__ == "__main__":
    main()