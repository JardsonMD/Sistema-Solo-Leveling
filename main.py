import funcoes

xp = funcoes.carregar_xp()
opcao = 0
while opcao != "4": 
    funcoes.mostrar_menu()
    opcao = input("Escolha uma opção: ")

    
    match opcao:
        case "1":
            print("Missões Diárias:")
            print("- Treinar")
            print("- Estudar Python")
            print("- Estudar Japonês")
        case "2":
            xp += 50
            funcoes.salvar_xp(xp)
            print("Tarefa Concluída.")
            print("Você Ganhou 50 XP.")
        case "3":
            print("Seu XP atual é: ", xp)
        case "4":
            print("Encerrando Sistema.")
        case _:
            print("Opção Inválida.")
    print()