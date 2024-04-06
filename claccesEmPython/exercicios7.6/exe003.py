# Crie uma classe em Python para atender as especificações abaixo:
# • O nome de um bolo.
# • O peso de um bolo.
# • O recheio de um bolo.
# • A data de vencimento de um bolo.
# Crie 2 objetos para esta classe, atribua alguns valores para os atributos criados e, ao final,
# exiba na tela os valores armazenados nesses atributos. 
class ReceitaBolo:
    def __init__(self, nome, peso, recheio, data_vencimento):
        self.nome = nome
        self.peso = peso
        self.recheio = recheio
        self.data_vencimento = data_vencimento

bolo1 = ReceitaBolo("Bolo de Laranja", "2.200", "Laranja", "07/04/2024")
bolo2 = ReceitaBolo("Bolo Formigueiro", "3 kg", "Formigueiro","10/04/2024")


print("Bolo 1:")
print("Nome", bolo1.nome)
print("Peso:", bolo1.peso)
print("Recheio:", bolo1.recheio)
print("Data de Vencimento:", bolo1.data_vencimento)

print("\nBolo 2:")
print("Nome:", bolo2.nome)
print("Peso:", bolo2.peso)
print("Recheio:", bolo2.recheio)
print("Data de Vencimento:", bolo2.data_vencimento)