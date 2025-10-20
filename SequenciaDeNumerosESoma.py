while True:

    m, n = map(int, input("Digite dois números inteiros: ").split())

    if m <= 0 or n <= 0:
        break

    if m > n:
        menor = n
        maior = m
    else:
        menor = m
        maior = n

    soma = 0
    sequencia_numeros = []

    for i in range(menor, maior + 1):
        sequencia_numeros.append(str(i))
        soma += i

    sequencia_str = " ".join(sequencia_numeros)
    print(f"{sequencia_str} Sum={soma}")