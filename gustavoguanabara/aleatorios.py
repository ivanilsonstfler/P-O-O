import random


# print('Gera cinco numeros Aleatorios entre 1 e 60')

# for i in range(5):
#     n = random.randint(1,60)
#     print(f'Número Gerado: {n}')

# valor = random.random()
# print(f' gerado: {round(valor * 10,2)}')


# valorr = random.uniform(1, 100)
# print(f'Númmero: {round(valorr, 2)}')

lista = [100, 90 , 80, 70, 60 , 50, 40, 30, 20, 10]

# n = random.choice(lista)

# print(f'Numero escolhido: {n}')

# n = random.sample(lista, 3)
# print(f'Numeros escolhidos: {n}')

print(f'Exibir a lista original: {lista}')
print(f'Embaralha a lista e exibi-la:')
n = random.shuffle(lista)
print(lista)
