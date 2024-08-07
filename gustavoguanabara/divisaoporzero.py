n1 = int(input("Digite um numero: "))
n2 = int(input("Digite o segundo numero: "))

try:
    r = round(n1 / n2, 2)
    
except ZeroDivisionError
    print(f'Nao é possivel divvidr por zero!')
else:
    print(f'Resultado: {r}')

print(f'Resultando: {r}')