valores = []
for _ in range(100):
    valores.append(int(input()))

maior = max(valores)
posicao = valores.index(maior) + 1  # posição começa em 1

print(maior)
print(posicao)
