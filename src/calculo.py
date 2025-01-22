opc = 0
while opc != 1:
    capitalInicial = float(input('Adicione o valor do capital inicial:'))
    taxa = float(input('Informe a taxa de juros:'))
    tempo = int(input('Informe o tempo(meses):'))
    montante = capitalInicial * (1+taxa)**tempo
    print(montante)
    opc = int(input("Digite 0 para continuar e 1 para sair"))

print('Encerrando...')
