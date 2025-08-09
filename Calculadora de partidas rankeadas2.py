#Calculadora de partidas rankeadas  

# saldo_vitorias, nivel_heroi
# 0 - 10: Ferro 
# 11 - 20: Bronze
# 21 - 50: Prata        
# 51 - 80: Ouro
# 81 - 90: Diamante
# 91 - 100: Lendário
# 101 ou mais: Imortal

def definir_nivel_heroi(saldo_vitorias):
    if saldo_vitorias < 0:
        return "indefinido"
    # Definindo os limites e níveis
    niveis = [
        (0, 10, "Ferro"),
        (11, 20, "Bronze"),
        (21, 50, "Prata"),
        (51, 80, "Ouro"),
        (81, 90, "Diamante"),
        (91, 100, "Lendário"),
        (101, float('inf'), "Imortal")
    ]

    for minimo, maximo, nivel in niveis:
        if minimo <= saldo_vitorias <= maximo:
            return nivel
        
    return "Nível desconhecido"

vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))
saldo_vitorias = vitorias - derrotas
nivel_heroi = definir_nivel_heroi(saldo_vitorias)
print(f"O herói tem saldo de {saldo_vitorias} vitorias e está no nível {nivel_heroi}")

