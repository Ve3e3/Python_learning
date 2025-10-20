NEG = []
POS = []

while True:
    N = int(input("Digite o valor de N (0 < N ≤ 50): "))
    if 0 < N <= 50:
        break
    print("Valor inválido! Digite um número entre 1 e 50.")

for i in range(N):
    valor = float(input(f"Digite o {i+1}º número real: "))
    if valor < 0:
        NEG.append(valor)
    else:
        POS.append(valor)

print("\nLista NEG (valores negativos):", NEG)
print("Quantidade de negativos:", len(NEG))
print("\nLista POS (valores positivos e zero):", POS)
print("Quantidade de positivos/zero:", len(POS))
