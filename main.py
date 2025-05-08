#Listas
pendente_lista = []
concluido_lista = []
tarefas_totais = pendente_lista + concluido_lista

#Funções
def tarefasPendentes():
    print("Tarefas Pendentes: ")
    return pendente_lista

def tarefasConcluidas():
    print("Tarefas Concluídas: ")
    return concluido_lista

def listarPendentes():
    for i, tp in enumerate(pendente_lista, start=1):
        print(f"{i} - {tp}")

def listarConcluidas():
    for i, tc in enumerate(concluido_lista, start=1):
        print(f"{i} - {tc}")

def listarTotais():
    for i, tt in enumerate(tarefas_totais, start=1):
        print(f"{i} - {tt}")

#Loop while / Menu principal
while True:

    print("------Bem-Vindo ao To-Do-List------")
    print("Começe a organizar suas tarefas diárias!")

    print("Menu de Opções:")
    print("[1] Adicionar nova tarefa.")
    print("[2] Listar tarefas.")
    print("[3] Marcar tarefa como concluída.")
    print("[4] Remover tarefa.")
    print("[5] Sair.")

    options = int(input("Insira a opção que deseja: "))

    if options == 1:
        while True:
            print('Digite "Sair" para voltar ao menu.')
            tarefa = str(input("Insira as tarefas que deseja: "))

            if tarefa.lower() == "sair":
                break

            pendente_lista.append(tarefa)
    elif options == 2:
        print('Digite "Sair" para voltar ao menu.')

        print("Tarefas Pendentes:")
        listarPendentes()

        print("\nTarefas Concluídas:")
        listarConcluidas()

        s = input(": ")

        if s.lower() == "sair":
            continue
        else:
            print("Você digitou errado, insira novamente.")
    elif options == 3:
        while True:
            listarPendentes()
            numero_tarefa = int(input("Escolha a tarefa pelo número: "))

            indice = numero_tarefa - 1

            task = pendente_lista.pop(indice) #Ele vai remover a tarefa que corresponde o index que está na lista de pendentes
            concluido_lista.append(task) #E aqui ele vai incluir tal tarefa na lista de concluídos

            o = input("Tudo pronto! Deseja marcar outra tarefa como concluída (sim/nao)? ")

            if o.lower() == "sim":
                continue
            else:
                break

    elif options == 4:
        while True:
            desejo = int(input("Você deseja remover uma tarefa (1 - pendente), (2 - concluída) ou (3 - Sair)? "))
            
            if desejo == 1:
                listarPendentes()
                numero_tarefa = int(input("Escolha a tarefa que deseja remover pelo número: "))

                indice = numero_tarefa - 1

                task2 = pendente_lista.pop(indice)

                while True: 
                    desejo2 = input("Deseja excluir mais algo dessa lista (sim/não)? ")

                    if desejo2.lower() == "sim":
                        listarPendentes()
                        numero_tarefa = int(input("Escolha a tarefa que deseja remover pelo número: "))

                        indice = numero_tarefa - 1

                        task2 = pendente_lista.pop(indice)
                    elif desejo2.lower() == "nao":
                        break
            elif desejo == 2:
                listarConcluidas()
                numero_tarefa = int(input("Escolha a tarefa que deseja remover pelo número: "))

                indice = numero_tarefa - 1

                task3 = concluido_lista.pop(indice)

                while True:
                    desejo2 = input("Deseja excluir mais algo dessa lista (sim/não)? ")

                    if desejo2.lower() == "sim":
                        listarConcluidas()
                        numero_tarefa = int(input("Escolha a tarefa que deseja remover pelo número: "))

                        indice = numero_tarefa - 1

                        task3 = concluido_lista.pop(indice)
                    elif desejo2.lower() == "nao":
                        break
            elif desejo == 3:
                break
            else:
                print("Comando inválido, tente novamente.")
                continue
    elif options == 5:
        print("Encerrando...")
        exit()
    else:
        print("Comando inválido, tente novamente.")
        continue