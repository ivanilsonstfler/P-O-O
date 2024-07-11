# n1 = [5, 7, 8, 9, 6]
# n2 = [1, 2,  3, 4, 6]

# valores = n1 + n2
# # valores[0] = 9 
# # print(len(valores))
# # print(sorted(valores, reverse=True))
# # print(sum(valores))

# # valores.append(100)
# # print(valores)

# # valores.pop(3)
# # print(valores)

# # valores.insert(3, 200)
# # print(valores)
# # print(100 in valores)
# planetas = ['Mercurio', ' Marte', ' venus', 'saturno', 'urano', 'neturno']
# for planeta in planetas:
#     print(planeta)

bebidas = []

for i in range(5):
    print(f"Digite uma bebida favorita:")
    bebida = input()
    bebidas.append(bebida)
    
bebidas.sort()

print(f'\nBebidas escolhidas:')

for bebida in bebidas:
    print(bebida)

print(f'\nSaúde!')

