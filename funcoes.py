from datetime import date
import json
ARQUIVO = "dados.json"

# ========== DADOS ==========

# Salva as alterações no arquivo json
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding= "utf-8") as f:
        json.dump(dados, f)

# ========== DATA ==========

# Reseta as missões diárias
def reset_diario():
    hoje = date.today().isoformat()

    try:
        with open(ARQUIVO, "r", encoding= "utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        return
    
    if dados.get("ultima_data") != hoje:
        for missao in dados["missoes"]:
            dados["missoes"][missao] = False

        dados["ultima_data"] = hoje
        salvar_dados(dados)



# ========== XP ========== 


# Carrega o XP do arquivo json
def carregar_xp():
    try:
        with open(ARQUIVO, "r", encoding= "utf-8") as f:
            dados = json.load(f)
            return dados.get("xp", 0)
    except FileNotFoundError:
        return 0

# ========== MENU ========== 

# Mostra o Menu para o usuário
def mostrar_menu():
    print(">=====Sistema Solo Leveling =====<")
    print("Seja Bem Vindo Jogador.")

    print("1 - Ver Missões Diarias")
    print("2 - Concluir Missões")
    print("3 - Ver XP")
    print("4 - Sair")

# ========== MISSÕES ==========

# Mostra a missão pro usuário
def mostrar_missoes():
    try:
        with open(ARQUIVO, "r", encoding= "utf-8") as f:
            dados = json.load(f)
        
        print("Missões Diárias")
        for missao, feita in dados["missoes"].items():
            status = "O" if feita else "X"
            print(f"- {missao} [{status}]")
    
    except FileNotFoundError:
        print("Nenhuma Missão Encontrada.")

# Marca uma missão como concuida
def concluir_missao(nome_missao):
    with open(ARQUIVO, "r", encoding= "utf-8") as f:
        dados = json.load(f)
    
    if nome_missao in dados["missoes"]:
        if not dados["missoes"][nome_missao]:
            dados["missoes"][nome_missao] = True
            dados["xp"] += 50
            salvar_dados(dados)
            print("Missão concluida. +50 XP.")
        else:
            print("Essa missão já foi concluída.")
    else:
        print("Missão inválida.")






