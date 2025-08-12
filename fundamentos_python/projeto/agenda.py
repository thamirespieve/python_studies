
def add_contact(name,tel,email,contact_list):
    new_contact = {"nome":name,"telefone":tel,"email":email,"favorito":False}
    contact_list.append(new_contact)
    print("Contato salvo com sucesso!")
    return

def show_contact(contact_list):
    print("Lista de contatos:\n")
    for index,contact in enumerate(contact_list,start=1):
        fav = "♡" if contact["favorito"] else "x"
        print(f"{index} - Nome: {contact['nome']} \
              \nTelefone: {contact['telefone']} \
              \nEmail: {contact['email']} \
              \nFavorito: {fav}")
        print("------")
    return

def update_contact(index,new_name,new_tel,new_email,contact_list):
    correct_index= int(index) - 1 
    if new_name != "":
        contact_list[correct_index]["nome"] = new_name
    if new_tel != "":
        contact_list[correct_index]["telefone"]=new_tel
    if new_email != "":
        contact_list[correct_index]["email"]=new_email
    
    print(f"Contato atualizado!")

    return

def mark_unmark_fav_contact(index,contact_list):
    correct_index = int(index) - 1 
    update_fav = False if contact_list[correct_index]["favorito"] else True
    contact_list[correct_index]["favorito"] = update_fav
    print("Favoritos atualizado")
    return

def show_fav_contact(contact_list):
    print("Lista de contatos favoritos:\n")
    for contact in contact_list:
        if contact["favorito"]:
            print(f"Nome: {contact['nome']} \
              \nTelefone: {contact['telefone']} \
              \nEmail: {contact['email']} ")
            print("------")
    return

def delete_contact(index,contact_list):
    correct_index= int(index) - 1
    contact_list.pop(correct_index)
    return
contact_list=[]
while True:
    print("Agenda:\n")

    print("1- Adicionar contato")
    print("2- Listar contatos")
    print("3- Editar contato")
    print("4- Marcar/Desmarcar contato como favorito")
    print("5- Listar contatos favoritos")
    print("6- Deletar contato")
    print("7- Sair")

    choice = input("Escolha uma opção:")

    if choice =='1':
        name = input("Informe o nome do contato: ")
        tel= input("Informe o telefone do contato: ")
        email= input("Informe o email do contato: ")
        add_contact(name,tel,email,contact_list)
    elif choice =='2':
        show_contact(contact_list)
    elif choice =='3':
         show_contact(contact_list)
         index = input("Qual o contato a ser atualizado ?")
         new_name = input("Qual o novo nome ? ")
         new_tel = input("Qual o novo telefone ? ")
         new_email = input("Qual o novo email ? ")
         update_contact(index,new_name,new_tel,new_email,contact_list)
    elif choice =='4':
        show_contact(contact_list)
        index = input("Qual o contato a ser atualizado ?")
        mark_unmark_fav_contact(index,contact_list)
    elif choice =='5':
        show_fav_contact(contact_list)
    elif choice =='6':
        show_contact(contact_list)
        index = input("Qual contato deseja excluir ?")
        delete_contact(index,contact_list)
    elif choice =='7':
        break