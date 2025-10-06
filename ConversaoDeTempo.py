N = int(input("insira o valor em segundos:"))

Horas = N // 3600
Minutos = (N % 3600) // 60
Segundos = N % 60

print(f"{Horas} hora(s), {Minutos} minuto(s) e {Segundos} segundo(s)")