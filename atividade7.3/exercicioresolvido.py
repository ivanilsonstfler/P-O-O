class Aluno:
    def __init__(self, nome, rg, data_nascimento):
        self.nome = nome
        self.rg = rg
        self.data_nascimento = data_nascimento

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Turma:
    def __init__(self, periodo, serie, sigla, tipo_ensino):
        self.periodo = periodo
        self.serie = serie
        self.sigla = sigla
        self.tipo_ensino = tipo_ensino

# Criação de dois objetos da classe Aluno
aluno1 = Aluno("João", "123456789", "01/01/2000")
aluno2 = Aluno("Maria", "987654321", "02/02/2001")

# Alteração dos valores dos atributos dos objetos aluno1 e aluno2
aluno1.nome = "João Pedro"
aluno2.rg = "112233445"

# Exibição dos valores armazenados nos atributos dos objetos aluno1 e aluno2
print(aluno1.nome, aluno1.rg, aluno1.data_nascimento)
print(aluno2.nome, aluno2.rg, aluno2.data_nascimento)

# Criação de dois objetos da classe Funcionario
funcionario1 = Funcionario("Carlos", "Professor", 3000)
funcionario2 = Funcionario("Ana", "Coordenadora", 5000)

# Alteração dos valores dos atributos dos objetos funcionario1 e funcionario2
funcionario1.salario = 3500
funcionario2.cargo = "Diretora"

# Exibição dos valores armazenados nos atributos dos objetos funcionario1 e funcionario2
print(funcionario1.nome, funcionario1.cargo, funcionario1.salario)
print(funcionario2.nome, funcionario2.cargo, funcionario2.salario)

# Criação de dois objetos da classe Turma
turma1 = Turma("Manhã", "1º ano", "A", "Ensino Médio")
turma2 = Turma("Tarde", "2º ano", "B", "Ensino Médio")

# Alteração dos valores dos atributos dos objetos turma1 e turma2
turma1.periodo = "Noite"
turma2.serie = "3º ano"

# Exibição dos valores armazenados nos atributos dos objetos turma1 e turma2
print(turma1.periodo, turma1.serie, turma1.sigla, turma1.tipo_ensino)
print(turma2.periodo, turma2.serie, turma2.sigla, turma2.tipo_ensino)
