A1, qtd1, valor1 = input().split()
A1, qtd1, valor1 = int(A1), int(qtd1), float(valor1)

B2, qtd2, valor2 = input().split()
B2, qtd2, valor2 = int(B2), int(qtd2), float(valor2)

total = (qtd1 * valor1) + (qtd2 * valor2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
