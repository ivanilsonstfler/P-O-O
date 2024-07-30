class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
    def apresentar(self):
            return f'Olá meu nome é {self.nome} e tenho {self.idade} anos e peso {self.peso} kilos.'
        
        
pessoa1 = Pessoa(nome='Alice', idade=35, peso=60)


print(pessoa1.apresentar())
    

            
        