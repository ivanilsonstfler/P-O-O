# Crie uma classe em Python para atender as especificações abaixo:
# • O número de municípios de um estado do Brasil.
# • O nome de um estado do Brasil.
# • A população de um estado do Brasil.
# Crie 3 objetos para esta classe, atribua alguns valores para os atributos criados e, ao final,
# exiba na tela os valores armazenados nesses atributos. 
class Estado:
    def __init__(self, nome, num_municipios, populacao):
        self.nome = nome
        self.num_municipios = num_municipios
        self.populacao = populacao
    
estado1 = Estado("maranhao", 645, 50000000)
estado2 = Estado("Alagoas", 92, 10121016)
estado3 = Estado("Roraima", 100, 152030)



print("Estado: ", estado1.nome, "Número de Municípios: ", estado1.num_municipios, "População: ", estado1.populacao)
print("Estado: ", estado2.nome, "Número de Municípios:", estado2.num_municipios, "População: ", estado2.populacao)
print("Estado: ", estado3.nome, "Número de Municípios: ", estado3.num_municipios, "População: ", estado3.populacao)
