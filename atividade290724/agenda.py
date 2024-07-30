class Contato:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return f"('{self.nome}', '{self.telefone}', '{self.endereco}')"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print("Seu contato foi inserido")

    def excluir_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            contato = self.contatos.pop(indice)
            print(f"Estamos excluindo.... quase lá...\nO dado da agenda {contato} foi excluído!")
        else:
            print("Índice inválido")

    def imprimir_contatos(self):
        if not self.contatos:
            print("Não há contatos na agenda.")
        else:
            for i, contato in enumerate(self.contatos):
                print(f"Contatos da agenda: {contato} - {i}")


def main():
    agenda = Agenda()
    
    while True:
        print("Digite o número da opção: 1 – adicionar, 2 – excluir, 3 – imprimir ou 4 – sair:")
        opcao = int(input())
        
        if opcao == 1:
            print("Nome:")
            nome = input()
            print("Telefone:")
            telefone = input()
            print("Endereço:")
            endereco = input()
            
            novo_contato = Contato(nome, telefone, endereco)
            agenda.adicionar_contato(novo_contato)
        
        elif opcao == 2:
            agenda.imprimir_contatos()
            if agenda.contatos:
                print(f"Se desistiu, digite {len(agenda.contatos)} para sair!")
                print("Qual o número da informação deseja excluir?")
                indice = int(input())
                if indice == len(agenda.contatos):
                    continue
                agenda.excluir_contato(indice)
        
        elif opcao == 3:
            agenda.imprimir_contatos()
        
        elif opcao == 4:
            print("<< Fechamos sua agenda! >>")
            break
        
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()


      
