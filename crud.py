tarefas = []

def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição: ")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!\n")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i} - {tarefa['titulo']} ({status})")
        print(f"    Descrição: {tarefa['descricao']}")
    print()


def atualizar_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        indice = int(input("Digite o índice da tarefa: "))

        if indice < 0 or indice >= len(tarefas):
            print("Índice inválido!\n")
            return

        tarefas[indice]["titulo"] = input("Novo título: ")
        tarefas[indice]["descricao"] = input("Nova descrição: ")

        concluida = input("Concluída? (s/n): ").lower()
        tarefas[indice]["concluida"] = (concluida == "s")

        print("Tarefa atualizada!\n")

    except ValueError:
        print("Digite um número válido.\n")


def excluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        indice = int(input("Digite o índice da tarefa para excluir: "))

        if indice < 0 or indice >= len(tarefas):
            print("Índice inválido!\n")
            return

        tarefas.pop(indice)
        print("Tarefa excluída com sucesso!\n")

    except ValueError:
        print("Digite um número válido.\n")


def menu():
    while True:
        print("====== GERENCIADOR DE TAREFAS ======")
        print("1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Atualizar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            atualizar_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!\n")


menu()