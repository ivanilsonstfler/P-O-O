valor = float(input('Digite o valo: '))
Anos = float(input('Digite os anos: '))
taxa = float(input('Digite a taxa de juros: '))

juros = valor *  (taxa / 100) * Anos

print('Exibir juros: {} '.format(juros))