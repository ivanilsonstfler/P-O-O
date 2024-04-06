# Em uma escola, os alunos precisam ser divididos por turmas, que devem ser
# representadas dentro da aplicação. Crie uma classe chamada Turma que
# contenha quatro atributos: o primeiro para o período, o segundo para definir
# a série, o terceiro para sigla e o quarto para o Ɵpo de ensino. 


# Crie dois objetos da classe Turma. Altere os valores dos atributos desses
# objetos e exiba na tela os valores armazenados nesses atributos. 





class Turma:
    def __init__(self, periodo, serie, sigla, tipo_ensino):
        self.periodo = periodo
        self.serie = serie
        self.sigla = sigla
        self.tipo_ensino = tipo_ensino

turma1 = Turma("Manhã", "1º ano", "A", "Ensino Médio")
turma2 = Turma("Tarde", "2º ano", "B", "Ensino Médio")

print(turma1.periodo, turma1.serie, turma1.sigla, turma1.tipo_ensino)
print(turma2.periodo, turma2.serie, turma2.sigla, turma2.tipo_ensino)