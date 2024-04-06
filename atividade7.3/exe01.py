# Crie um programa em Python que tenha uma classe chamada Aluno para
# definir os objetos que representarão os alunos de uma escola. Nessa classe,
# declare três atributos: o primeiro para o nome, o segundo para o RG e o
# terceiro para a data de nascimento dos alunos. 


# Crie dois objetos da classe Aluno. Altere os valores dos atributos desses
# objetos e exiba na tela os valores armazenados nesses atributos. 





class Aluno:
    def __init__(self, nome, rg, data_nascimento):
        self.nome = nome
        self.rg = rg
        self.data_nascimento = data_nascimento

aluno1 = Aluno("João", "123456789", "01/01/2000")
aluno2 = Aluno("Maria", "987654321", "02/02/2001")


aluno1.nome = "João Pedro"
aluno2.rg = "112233445"

print(aluno1.nome, aluno1.rg, aluno1.data_nascimento)
print(aluno2.nome, aluno2.rg, aluno2.data_nascimento)