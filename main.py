import funcoes

funcoes.reset_diario()

xp = funcoes.carregar_xp()
opcao = 0
while opcao != "4": 
    funcoes.mostrar_menu()
    opcao = input("Escolha uma opção: ")

    
    match opcao:
        case "1":
           funcoes.mostrar_missoes()
        case "2":
            missao = input("Digite o nome da missão: ")
            funcoes.concluir_missao(missao)
        case "3":
            print("Seu XP atual é: ", funcoes.carregar_xp())
        case "4":
            print("Encerrando Sistema.")
        case _:
            print("Opção Inválida.")
    print()