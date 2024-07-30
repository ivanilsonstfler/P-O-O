livros = [
'[0] O universo numa casca de noz',
 '[1] Uma breve história do tempo',
 '[2] O grande projeto',
 '[3] A teoria de tudo',
 '[4] Buracos Negros: Palestra da BBC Reith Lectures',
 '[5] Uma nova história do tempo',
 '[6] Breves respostas para grandes questões',
 '[7] Infinito em todas as direções',
 '[8] O livro que ninguém leu',
 '[9] Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente']

print("Bem-vindo à Biblioteca IVANILSON!")
print("Livros disponíveis para empréstimo:")

for i, livro in enumerate(livros):
    print(f"[{i}] {livro}")


nome_usuario = input("Digite seu nome: ")


try:
    numero_livro = int(input("Digite o número do livro desejado (0 a 9): "))
    livro_escolhido = livros[numero_livro]
    print(f"{nome_usuario}, o empréstimo do livro '{livro_escolhido}' foi realizado. Volte sempre!")
except IndexError:
    print("Número de livro inválido. Certifique-se de escolher um número entre 0 e 9.")
    
    
    
#     class Viagem:
#     def __init__(self, destino):
#         self.destino = destino
        
#     def exibir_info(self):
#         return f"Destino: {self.destino}"
        
# Viagem0 = Viagem("Bonito/MS")
# Viagem1 = Viagem("Foz do Iguaçu")
# Viagem2 = Viagem("Santa Catarina/SC")
# Viagem3 = Viagem("Belo Horizonte/MG")
# Viagem4 = Viagem("Pantanal")

# print("BEM-VINDO")

# viajante = input("Digite seu nome para começar: ")
# print(f"{viajante}, temos 5 destinos que combinam com você:")
# print("[0] Bonito")
# print("[1] Foz do Iguaçu")
# print("[2] Santa Catarina")
# print("[3] Belo Horizonte")
# print("[4] Pantanal")

# opcao_selecionada = int(input("Selecione o número da viagem desejada: "))
# lista_viagem = [Viagem0, Viagem1, Viagem2, Viagem3, Viagem4]

# if 0 <= opcao_selecionada < 5:
#     print(f"{viajante}, sua viagem será para {lista_viagem[opcao_selecionada].exibir_info()}.")
# else:
#     print("Essa opção não está inclusa nos nossos destinos!")
