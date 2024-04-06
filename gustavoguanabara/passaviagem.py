distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta presta a começar uma viagem de {}km.'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.60
else:
    preco = distancia * 0.25

print("o preço da sua viagem será de R${:.2f}".format(preco))
