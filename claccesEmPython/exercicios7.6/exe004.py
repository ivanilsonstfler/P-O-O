# Leia a descrição abaixo e implemente em Python as classes necessárias para atender a
# demanda especificada.
# IdenƟfique as classes e implemente um programa para a seguinte especificação:
# “O supermercado vende diferentes Ɵpos de produtos. Cada produto tem um preço
# e uma quanƟdade em estoque. Um pedido de um cliente é composto de itens,
# onde cada item especifica o produto que o cliente deseja e a respecƟva
# quanƟdade. Esse pedido pode ser pago em dinheiro, cheque ou cartão.”
# Crie 2 objetos para esta classe, atribua alguns valores para os atributos criados e, ao final,
# exiba na tela os valores armazenados nesses atributos. 
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, itens, forma_pagamento):
        self.itens = itens
        self.forma_pagamento = forma_pagamento


produto1 = Produto("Arroz", 10.99, 50)
produto2 = Produto("Feijão", 8.49, 40)


item1 = ItemPedido(produto1, 2)
item2 = ItemPedido(produto2, 3)


pedido = Pedido([item1, item2], "Cartão de Crédito")


print("Pedido:")
print("Forma de pagamento:", pedido.forma_pagamento)
print("Itens do pedido:")
for item in pedido.itens:
    print("Produto:", item.produto.nome)
    print("Preço unitário:", item.produto.preco)
    print("Quantidade:", item.quantidade)
    print("Subtotal:", item.produto.preco * item.quantidade)
    print()


    