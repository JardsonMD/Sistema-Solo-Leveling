import json

# ========== XP ========== 
ARQUIVO = "dados.json"

# Salva o XP Atual
def salvar_xp(xp):
    dados = {"xp" : xp}
    with open(ARQUIVO, "w") as f:
        json.dump(dados,f)

# Carrega o XP do arquivo json
def carregar_xp():
    try:
        with open(ARQUIVO, "r") as f:
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





# ========== DADOS ==========




