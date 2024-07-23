class Pessoa:
    def __init__(self,nome,idade,peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        
    def apresentar(self):
            return f'Olá meu nome é {self.nome} e tenho {self.idade} anos e peso {self.peso} kilos.'
        
        
pessoa1 = Pessoa(nome='Alice', idade=35, peso=60)


print(pessoa1.apresentar())
    
# class Pessoa:
#     def __init__(self, nome, idade, peso):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso

#     def apresentar(self):
#         return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e peso {self.peso} quilos."

# # Criando uma instância da classe Pessoa
# pessoa1 = Pessoa(nome='Alice', idade=35, peso=60)

# # Chamando o método para apresentar a pessoa
# print(pessoa1.apresentar())

            
        