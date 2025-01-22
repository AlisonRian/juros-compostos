opc = 0
while opc != 1:
    try:
        print("Funcionalidade principal")
        capital = float(input("Digite o capital inicial (C): "))
        taxa = float(input("Digite a taxa de juros (em %): ")) / 100
        tempo = int(input("Digite o tempo em períodos (t): "))

        montante = capital * (1 + taxa) ** tempo
        print(f"O montante após {tempo} períodos será de R$ {montante:.2f}.")
    except ValueError:
        print("Por favor, insira valores válidos.")

    opc = int(input("Digite 0 para continuar e 1 para sair"))

print('Encerrando...')
