# Crie uma classe em Python para atender as especificações abaixo:
# • A altura de uma pessoa em metros.
# • O peso de uma pessoa em quilos.
# • A temperatura corporal de uma pessoa.
# • O sexo de uma pessoa.
# • A altura de uma pessoa em milímetros.
# Crie 2 objetos para esta classe, atribua alguns valores para os atributos criados e, ao final,
# exiba na tela os valores armazenados nesses atributos. 
class Pessoa:
    def __init__(self, altura, peso, sexo, altura_milimetros):
        self.altura = altura
        self.peso = peso
        self.sexo = sexo
        self.altura_milimetros = altura_milimetros

pessoa1 = Pessoa(1.61, 60, 'Masculino', 1610)
pessoa2 = Pessoa(175, 60, 'Feminino', 1750) 


print("Pessoa 1:")
print("Altura: ",pessoa1.altura )
print("Peso: ", pessoa1.peso)
print("Sexo: ", pessoa1.sexo)
print("Altura em mm:",pessoa1.altura_milimetros)


print("Pessoa 2:")
print("Altura: ", pessoa2.altura)
print("Peso: ", pessoa2.peso)
print("Sexo: ", pessoa2.sexo)
print("Altura em mm", pessoa2.altura_milimetros)