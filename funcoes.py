import datetime as dt
import json
ARQUIVO = "dados.json"

# ========== DADOS ==========

# Salva as alterações no arquivo json
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding= "utf-8") as f:
        json.dump(dados, f)

# Carrega os dados do arquivo json
def carregar_dados():
    with open(ARQUIVO, "r", encoding= "utf-8") as f:
        return json.load(f)
# ========== DATA ==========

# Reseta as missões diárias
def reset_missoes():
    hoje = dt.datetime.today()

    try:  
        dados = carregar_dados()
    except FileNotFoundError:
        return
    ultima_data = dt.datetime.fromisoformat(dados["ultima_data"])
    if ultima_data.date() != hoje.date():
        for missao in dados["missoes"]:
            tipo = dados["missoes"][missao]["tipo"]
            match tipo:
                case 1:
                    dados["missoes"][missao]["feita"] = False
                case 2:
                    data = dt.datetime.fromisoformat(dados["missoes"][missao]["data"])
                    if (hoje - data).days >= 7:
                        dados["missoes"][missao]["feita"] = False
                        nova_data = hoje - dt.timedelta(days = hoje.weekday())
                        nova_data = nova_data.replace(hour=0, minute=0, second=0, microsecond=0)
                        dados["missoes"][missao]["data"] = nova_data.isoformat()
                case 3:
                    data = dt.datetime.fromisoformat(dados["missoes"][missao]["data"])
                    if hoje.month != data.month or hoje.year != data.year:
                        dados["missoes"][missao]["feita"] = False
                        nova_data = hoje.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                        dados["missoes"][missao]["data"] = nova_data.isoformat()
                case 4:
                        data = dt.datetime.fromisoformat(dados["missoes"][missao]["data"])
                        if hoje > data:
                            dados["missoes"][missao]["tipo"] = 0
                            dados["missoes"][missao]["data"] = ""
                case _:
                    continue
            

    dados["ultima_data"] = hoje.isoformat()
    salvar_dados(dados)



# ========== XP ========== 

# Calcula o Nivel do Jogador
def calc_nivel(xp):
    return xp // 100 + 1


# Carrega o XP do arquivo json
def carregar_xp():
    try:
        dados = carregar_dados()
        return dados["player"]["xp"]
    except FileNotFoundError:
        return 0

# ========== MENU ========== 

# Mostra o Menu para o usuário
def mostrar_menu():

    dados = carregar_dados()

    xp = dados["player"]["xp"]
    nivel = calc_nivel(xp)
    xp_proximo_nivel = nivel * 100

    print(">=====Sistema Solo Leveling =====<")
    print(f"Jogador - Nivel {nivel} | XP - {xp} / {xp_proximo_nivel}" )
    print()
    print("1 - Ver Missões Diarias")
    print("2 - Concluir Missões")
    print("3 - Ver XP")
    print("4 - Sair")

# ========== MISSÕES ==========

# Mostra a missão pro usuário
def mostrar_missoes():
    try:
        dados = carregar_dados()
        
        print("Missões Diárias")
        for missao in dados["missoes"]:
            status = "O" if dados["missoes"][missao]["feita"] else "X"
            print(f"- {missao} [{status}]")
    
    except FileNotFoundError:
        print("Nenhuma Missão Encontrada.")

# Marca uma missão como concuida
def concluir_missao(nome_missao):
    dados = carregar_dados()
    
    if nome_missao in dados["missoes"]:
        if not dados["missoes"][nome_missao]["feita"]:
            dados["missoes"][nome_missao]["feita"] = True
            dados["player"]["xp"] += dados["missoes"][nome_missao]["xp"]
            salvar_dados(dados)
            print("Missão concluida. +", dados["missoes"][nome_missao]["xp"], "XP.")
        else:
            print("Essa missão já foi concluída.")
    else:
        print("Missão inválida.")






