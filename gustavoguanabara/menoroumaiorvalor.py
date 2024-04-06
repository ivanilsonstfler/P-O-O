valor1 = float(input('Valor 01: '))
valor2 = float(input('Valor 02: '))
valor3 = float(input('Valor 03: '))
menor = valor1

# Verificando quem é o menor valor
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3

# Inicializando a variável maior
maior = valor1

# Verificando quem é o maior valor
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:  # Faltava um ':' no final desta linha
    maior = valor3
    
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
