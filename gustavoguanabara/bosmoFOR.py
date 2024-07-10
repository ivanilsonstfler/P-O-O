# lista = [1, 2, 3, 4, 5, 6,7]

# for item in lista:
#     print(item)


# for numero in range(1,11):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(5):
#     print(f'{x+1} {nome}')


# for x in range(20,1,-2):
#     print(x)

pedras = ('Rubi','Esmeralda','Quatzo','Diamante','Turmalina')

for pedra in pedras:
    if pedra == 'Quatzo':
        continue
    print(pedra)
