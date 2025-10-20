A = []
R = []
LMin = int(input("Digite o valor de LMin: "))
LMax = int(input("Digite o valor de LMax: "))

if LMax < LMin:
    LMin, LMax = LMax, LMin

N = int(input("Quantos valores deseja digitar? "))

for i in range(N):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    if LMin <= valor <= LMax:
        A.append(valor)
    else:
        R.append(valor)

print("\nLista A (valores aceitos):", A)
print("Quantidade de aceitos:", len(A))
print("\nLista R (valores rejeitados):", R)
print("Quantidade de rejeitados:", len(R))
