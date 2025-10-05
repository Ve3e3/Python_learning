positivos = 0
soma = 0

for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1
        soma += valor

media = soma / positivos

print(f"{positivos} valores positivos")
print(f"{media:.1f}")
