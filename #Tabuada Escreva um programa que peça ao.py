#Tabuada Escreva um programa que peça ao usuário para digitar um número e mostre a tabuada desse número.
num = int(input("Digite um numero: "))

for i in range(1, 11):
    print(num,"+",i, num*i)