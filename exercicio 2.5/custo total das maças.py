numero_Macas = int(input("Digite o numero de maçãs compradas:"))



if numero_Macas < 12:
    custo_Total = numero_Macas * 1.30

else:
    custo_Total = numero_Macas *1.00


print("O custo total da compra é: R$", custo_Total)


