#Calculadora de partidas rankeadas  

# saldo_vitorias, nivel_heroi
# 0 - 10: Ferro 
# 11 - 20: Bronze
# 21 - 50: Prata        
# 51 - 80: Ouro
# 81 - 90: Diamante
# 91 - 100: Lendário
# 101 ou mais: Imortal


def definir_nivel_heroi (saldo_vitorias):
    if saldo_vitorias <= 10:
        return "Ferro"
    elif 11 <= saldo_vitorias <= 20:
        return "Bronze"
    elif 21 <= saldo_vitorias <= 50:
        return "Prata"
    elif 51 <= saldo_vitorias <= 80:
        return "Ouro"
    elif 81 <=saldo_vitorias <= 90:
        return "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

vitorias = int(input("Digite o número total de vitórias: "))
derrotas = int(input("Digite o número total de derrotas: "))

saldo_vitorias = vitorias - derrotas
nivel_heroi = definir_nivel_heroi(saldo_vitorias)
print(f"O herói tem saldo de {saldo_vitorias} vitórias e está classificado no nível {nivel_heroi}.")




