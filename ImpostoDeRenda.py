salario = float(input())
imposto = 0.0

if salario <= 2000.00:
    print("Isento")
else:
    if salario > 2000.00:
        faixa = min(salario, 3000.00) - 2000.00
        imposto += faixa * 0.08
    if salario > 3000.00:
        faixa = min(salario, 4500.00) - 3000.00
        imposto += faixa * 0.18
    if salario > 4500.00:
        faixa = salario - 4500.00
        imposto += faixa * 0.28
    
    print(f"R$ {imposto:.2f}")
