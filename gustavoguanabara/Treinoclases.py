class Carro:
    def __init__(self, motor,roda,potencia,ano):
        self.motor = motor
        self.roda = roda
        self.potencia = potencia
        self.ano = ano
        
        
    def viagem(self):
        print(f'Meu carro tem um {self.motor} 2.0 e {self.roda} de liga leve, a {self.potencia} é 160 cavalos e o é novo{self.ano}')
        
        



carro1 = Carro(motor="V6",roda="17 polegadas", potencia="160", ano="2024")

print(carro1.viagem())