N = int(input( "Digite o número de casos de teste: "))

for i in range(N):

    x, y = map(int, input("Digite dois números inteiros: ").split())

    if x > y:
        x, y = y, x

    soma_impares = 0
    
    for j in range(x + 1, y):
        if j % 2 != 0:
            soma_impares += j
            
    print(soma_impares)