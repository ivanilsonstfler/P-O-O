# Em uma escola, além dos alunos temos os funcionários, que também precisam
# ser representados em nossa aplicação. Então crie uma classe chamada
# Funcionario que contenha três atributos: o primeiro para o nome o segundo
# para o cargo e o terceiro para o salário dos funcionários. 


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario



        funcionario1 = Funcionario("Carlos", "Professor", 3000)
        funcionario2 = Funcionario("Ana", "Coordenadora", 5000)
        
        funcionario1.salario = 3500

        funcionario2.cargo = "Diretora"