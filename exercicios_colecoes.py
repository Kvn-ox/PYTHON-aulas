
# ==========================================================
# Exercícios com Coleções em Python
# Listas • Tuplas • Conjuntos • Dicionários
# ==========================================================

# ----------------------------------------------------------
# 1. Tabela de campeonato (Lista)
# ----------------------------------------------------------
print("\n=== CAMPEONATO ===")

tabela = ["Real Madrid", "Manchester City", "Barcelona", "Bayern", "PSG"]

print("Top 5:", tabela)
print("3 primeiros:", tabela[:3])
print("Últimos 2:", tabela[-2:])
print("Ordem alfabética:", sorted(tabela))

if "Barcelona" in tabela:
    print("Barcelona está na posição:", tabela.index("Barcelona") + 1)
else:
    print("Barcelona não está na tabela.")


# ----------------------------------------------------------
# 2. Smartphones nas lojas (Conjuntos)
# ----------------------------------------------------------
print("\n=== LOJAS DE SMARTPHONES ===")

loja1 = {"iPhone 15", "Samsung S23", "Xiaomi 13", "Motorola Edge"}
loja2 = {"Samsung S23", "iPhone 15", "Galaxy A54", "Poco X5"}

print("Modelos disponíveis no total:", loja1 | loja2)   # união
print("Modelos nas duas lojas:", loja1 & loja2)        # interseção


# ----------------------------------------------------------
# 3. Dicionário com aluno e situação
# ----------------------------------------------------------
print("\n=== SITUAÇÃO DO ALUNO ===")

aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média: "))

aluno["situacao"] = "AP" if aluno["media"] >= 50 else "RP"

print("Dados do aluno:", aluno)


# ----------------------------------------------------------
# 4. Pessoas mais pesada e mais leve
# ----------------------------------------------------------
print("\n=== PESO DAS PESSOAS ===")

pessoas = []

for i in range(3):
    nome = input(f"Nome da pessoa {i+1}: ")
    peso = float(input("Peso: "))
    pessoas.append((nome, peso))

mais_pesada = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print("Mais pesada:", mais_pesada[0])
print("Mais leve:", mais_leve[0])


# ----------------------------------------------------------
# 5. Dados de várias pessoas
# ----------------------------------------------------------
print("\n=== GRUPO DE PESSOAS ===")

total_idade = 0
mulheres_menos_20 = 0
quantidade = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(quantidade):
    print(f"\nPessoa {i+1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()

    total_idade += idade

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

media = total_idade / quantidade

print("\nMédia de idade do grupo:", round(media, 2))
print("Mulheres com menos de 20 anos:", mulheres_menos_20)

print("\nPrograma finalizado!")
