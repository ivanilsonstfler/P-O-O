num1 = input("Digite o primeiro numero:")

num2 = input("Digite o segundo numero:")

num3 = input("Digite o terceiro numero:")

if (num1 >= num2) and (num1 >= num3):

    maior = num1
elif (num2 >= num1) and (num2 >= num3):
    maior = num3
else:
    maior = num3    

print("O maior número é", maior)

