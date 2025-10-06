A = int(input("insira o primeiro valor:"))
B = int(input("insira o segundo valor:"))
C = int(input("insira o terceiro valor:"))
D = int(input("insira o quarto valor:"))

if (B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")