while True:
    print("-" * 30)

    p1 = input("Escolha a primeira palavra (vertebrado/invertebrado): ")

    animal = None

    if p1 == 'vertebrado':
        p2 = input("Vertebrado: Escolha a classe (ave/mamifero): ")
        
        if p2 == 'ave':
            p3 = input("Ave: Escolha a alimentação (carnivoro/onivoro): ")
            
            if p3 == 'carnivoro':
                animal = 'aguia'
            elif p3 == 'onivoro':
                animal = 'pomba'
            
        elif p2 == 'mamifero':
            p3 = input("Mamifero: Escolha a alimentação (onivoro/herbivoro): ")
            
            if p3 == 'onivoro':
                animal = 'homem'
            elif p3 == 'herbivoro':
                animal = 'vaca'

    elif p1 == 'invertebrado':
        p2 = input("Invertebrado: Escolha a classe (inseto/anelideo): ")
        
        if p2 == 'inseto':
            p3 = input("Inseto: Escolha a alimentação (hematofago/herbivoro): ")
            
            if p3 == 'hematofago':
                animal = 'pulga'
            elif p3 == 'herbivoro':
                animal = 'lagarta'
                
        elif p2 == 'anelideo':
            p3 = input("Anelideo: Escolha a alimentação (hematofago/onivoro): ")
            
            if p3 == 'hematofago':
                animal = 'sanguessuga'
            elif p3 == 'onivoro':
                animal = 'minhoca'

    if animal:
        print(f"\nO animal correspondente é: {animal}")
    else:
        print("\nERRO: Uma das palavras inseridas não é válida para este esquema de classificação.")

    print("-" * 30)
    
    continuar = input("Deseja classificar outro animal? (s/n): ").lower()
    
    if continuar != 's':
        print("Programa encerrado. Até mais!")
        break