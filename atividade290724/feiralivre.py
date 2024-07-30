frutas = [
'Laranja',
 'Maçã',
 'Pêra',
 'Uva']
print("Nosssa Feira Livre tem disponivel hoje: 0 - Laranja, 1 - Maçã, 2 - Pêra, 3 - Uva")
    
nome_usuario = input("Digite seu nome para comprar: ")
numero_fruta = int(input("Digite o numero da fruta que deseja adquirir: "))
if 0 <= numero_fruta < len(frutas):
   
    fruta_escolhida = frutas[numero_fruta]
    
    print(f"{nome_usuario},agradecemos por adquirir a fruta{fruta_escolhida}. Volte Sempre!")
else:
    print("Opçao invalida.POr favor escolha um numero da fruta Valido!")



