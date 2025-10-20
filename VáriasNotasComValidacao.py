while True:
    notas = []
    while len(notas) < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("nota invalida")
    media = sum(notas) / 2
    print(f"media = {media:.2f}")
    while True:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        if opcao in [1, 2]:
            break
    if opcao == 2:
        break