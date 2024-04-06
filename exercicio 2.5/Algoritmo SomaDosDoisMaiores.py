valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))
valor3 = float(input("Insira o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    maior1 = valor1
    maior2 = valor2 if valor2 > valor3 else valor3
elif valor2 > valor1 and valor2 > valor3:
    maior1 = valor2
    maior2 = valor1 if valor1 > valor3 else valor3
else:
    maior1 = valor3
    maior2 = valor1 if valor1 > valor2 else valor2

print("A soma dos dois maiores valores é: ", maior1 + maior2)
