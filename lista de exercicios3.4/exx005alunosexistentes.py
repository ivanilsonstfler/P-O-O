import os
os.system('cls')


num_alunos = int(input("Digite uo numero de alunos: ")) 
soma = 0

for i in range(0, num_alunos +1):
    nota = float(input("Digite a nota do " + str(i) + "º aluno: "))

    soma += nota

media = soma / num_alunos
print("A média aritmética das notas dos alunos é: ", media)


