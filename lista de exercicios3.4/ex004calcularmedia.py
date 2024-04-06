soma = 0

for i in (1, 11):
    valor = float(input("Digite o" + str(i) + 'valor: ')) 

    soma += valor 
media = soma /10

print(("A média aritmética dos valores digitados é: ", media))

import os
os.system('cls')