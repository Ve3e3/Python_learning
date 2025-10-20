A = []

LMin = int(input("Digite o valor de LMin: "))
LMax = int(input("Digite o valor de LMax: "))

if LMax < LMin:
    LMin, LMax = LMax, LMin

N = int(input("Quantos valores deseja digitar? "))

for i in range(N):
    valor = int(input(f"Digite o {i+1}º número inteiro: "))
    if LMin <= valor <= LMax:
        A.append(valor)

print("\nLista A (valores dentro do intervalo):", A)
print("Tamanho efetivo da lista:", len(A))
