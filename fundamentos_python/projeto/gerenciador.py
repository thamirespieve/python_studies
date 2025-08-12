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

def update_task(index,updted_task,task_list):
    correct_index = int(index)-1
    if correct_index >=0 and correct_index < len(task_list):
       task_list[correct_index]["tarefa"] = updted_task
       print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa escolhida não existe")
    
    return

def complete_taks(index,task_list):
    correct_index= int(index)-1
    if correct_index >=0 and correct_index < len(task_list):
        task_list[correct_index]["completada"] = True
        print(f"Tarefa {index} completada com sucesso!")
    else:
      print("Tarefa escolhida não existe")
    return
    
def delete_task(index,task_list):
    correct_index = int(index) - 1
    if correct_index >=0 and correct_index < len(task_list):
        task_list.pop(correct_index)
        print(f"Tarefa {index} removida da lista.")
    else:
        print("Tarefa escolhida não existe")
    return

def delete_complete_task(task_list):
    for task in task_list:
        if task["completada"]:
            task_list.remove(task)
    print('Tarefas completadas foram deletadas')
    return

task_list =[]

while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas")
    print("6. Deletar tarefas completadas")
    print("7. Sair")

    escolha = input("Digite sua escolha:")

    if escolha == '1':
        task_name = input("Digite o nome da tarefa? ")
        add_task(task_name,task_list)
    elif escolha == '2':
        show_task(task_list)
    elif escolha == '3':
        show_task(task_list)
        index = input("Qual número da tarefa que deseja atualizar?")
        new_task = input("Qual a nova tarefa ?")
        update_task(index,updted_task=new_task,task_list=task_list)    
    elif escolha =='4':
        show_task(task_list)
        index= input("Qual o número da tarefa a ser completada ?")
        complete_taks(index,task_list)
    elif escolha == '5':
        show_task(task_list)
        index = input("Qual o número da tarefa que deseja excluir?")
        delete_task(index,task_list)
    elif escolha == '6':
        delete_complete_task(task_list)
        show_task(task_list)
    elif escolha == '7':
        break

