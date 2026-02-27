
# ==========================================================
# Exercícios de Introdução ao Python
# Autor: Kevin Vale (adaptado com explicações didáticas)
# ==========================================================

import math

# ----------------------------------------------------------
# 1. Nome completo
# ----------------------------------------------------------
nome = input("Digite seu nome completo: ").strip()

print("\n--- Resultado ---")
print("Maiúsculas:", nome.upper())
print("Minúsculas:", nome.lower())

# conta letras ignorando espaços
total_letras = len(nome.replace(" ", ""))
print("Total de letras:", total_letras)

# troca último sobrenome
partes = nome.split()
if len(partes) > 1:
    novo_nome = " ".join(partes[:-1]) + " do Inatel"
else:
    novo_nome = nome + " do Inatel"

print("Com último sobrenome trocado:", novo_nome)


# ----------------------------------------------------------
# 2. Tabuada dentro de um intervalo
# ----------------------------------------------------------
print("\n--- TABUADA ---")
num = int(input("Escolha o número da tabuada: "))
inicio = int(input("Início do intervalo: "))
fim = int(input("Fim do intervalo: "))

for i in range(inicio, fim + 1):
    print(f"{num} x {i} = {num * i}")


# ----------------------------------------------------------
# 3. Leitura do sexo com validação
# ----------------------------------------------------------
print("\n--- SEXO ---")
while True:
    sexo = input("Digite M para masculino ou F para feminino: ").strip().upper()
    if sexo == "M":
        print("Sexo masculino.")
        break
    elif sexo == "F":
        print("Sexo feminino.")
        break
    else:
        print("Entrada inválida. Tente novamente.")


# ----------------------------------------------------------
# 4. Preço da viagem
# ----------------------------------------------------------
print("\n--- VIAGEM ---")
distancia = float(input("Distância da viagem (Km): "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preço da passagem: R$ {preco:.2f}")


# ----------------------------------------------------------
# 5. Separação de dígitos
# ----------------------------------------------------------
print("\n--- DÍGITOS ---")
while True:
    numero = int(input("Digite um número entre 1000 e 9999: "))
    if 1000 <= numero <= 9999:
        break
    print("Número inválido!")

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)


# ----------------------------------------------------------
# 6. Operações com número decimal
# ----------------------------------------------------------
print("\n--- NÚMERO DECIMAL ---")
valor = float(input("Digite um número decimal: "))

print("Raiz quadrada:", math.sqrt(valor))
print("Teto (ceil):", math.ceil(valor))
print("Chão (floor):", math.floor(valor))
print("Parte inteira:", math.trunc(valor))

print("\nPrograma finalizado com sucesso!")
