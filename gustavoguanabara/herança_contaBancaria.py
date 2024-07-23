class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        self.consultar_saldo()

    def sacar(self, valor):
        self.saldo -= valor
        self.consultar_saldo()

    def consultar_saldo(self):
        print(self.saldo)

class ContaPoupança(ContaBancaria):
    def _consulta_rentabilidade(self):
        return 0.4
    
    def rentabilidade(self):  # Corrigido o nome do método
        rentabilidade = self._consulta_rentabilidade()

        if rentabilidade < 0.5:  # Corrigido o nome da variável
            print('Consulte seu gerente')
        else:
            print(rentabilidade)

conta_poupança = ContaPoupança()  
conta_poupança.rentabilidade()
conta_poupança.depositar(100) 
conta_poupança.sacar(50)
conta_poupança.consultar_saldo()