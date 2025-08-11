def add_task(task,task_list):
    #Tarefa: nome da terfa
    #completada: indicar se essa tarefa foi completada ou não
    
    new_task={"tarefa":task, "completada":False}
    task_list.append(new_task)
    print(f"Tarefa, {task}, foi adicionada com sucesso.")
    return

def show_task(task_list):
    print("\n Lista de tarefas:")
    for index,task in enumerate(task_list,start=1):
        status = "✓" if task["completada"] else ""
        task_name = task["tarefa"]
        print(f"{index}. [{status}] {task_name}")
    return

task_list =[]

while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite sua escolha:")

    if escolha == '1':
        task_name = input("Digite o nome da tarefa? ")
        add_task(task_name,task_list)
    if escolha == '2':
        show_task(task_list)
    elif escolha == '6':
        break

