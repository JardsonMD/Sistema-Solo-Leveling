import funcoes as fun

fun.reset_missoes()

xp = fun.carregar_xp()
opcao = 0
while opcao != "4": 
    fun.mostrar_menu()
    opcao = input("Escolha uma opção: ")

    
    match opcao:
        case "1":
           fun.mostrar_missoes()
        case "2":
            missao = input("Digite o nome da missão: ")
            fun.concluir_missao(missao)
        case "3":
            print("Seu XP atual é: ", fun.carregar_xp())
        case "4":
            print("Encerrando Sistema.")
        case _:
            print("Opção Inválida.")
    print()