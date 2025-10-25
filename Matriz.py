
def ler_numero():
    """Lê um número par entre 6 e 32. Continua pedindo até ser válido."""
    while True:
        try:
            n = int(input("Digite um número inteiro N (par, entre 6 e 32): "))
            if n < 6 or n > 32 or n % 2 != 0:
                print(f"O número {n} é inválido")
            else:
                return n
        except ValueError:
            print("Entrada inválida. Digite um número inteiro, para ser valido.")


def desenhar_retangulo(n):
    """Desenha o retângulo com largura N e espessura 2 de asteriscos."""
    for linha in range(n):
        # Primeira e última linha -> preenchidas
        if linha < 2 or linha >= n - 2:
            print("*" * n)
        else:
            # Linhas do meio: 2 asteriscos à esquerda e à direita
            print("**" + " " * (n - 4) + "**")


def main():

    n = ler_numero()
    print("\nSaída:\n")
    desenhar_retangulo(n)


if __name__ == "__main__":
    main()
