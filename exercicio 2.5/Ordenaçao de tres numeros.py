valorA=input("Digite  primeiro numero:")
valorB=input("Digite o segundo numerp:")
valorC=input("Digite o seu terceiro numero:")

if valorA > valorB:
    Aux = valorA 
    valorA = valorB
    valorB = Aux

if valorA > valorC:
    Aux = valorA
    valorA = valorC
    valorC = Aux

if valorB > valorC:
    Aux = valorB
    valorB = valorC
    valorC = Aux

print("A ordem dos numeros crescentes sao:",valorA, valorB, valorC)

