L1 =input("escreva o primeiro lado: ")
L2 = input("escreva o segundo lado: ")
L3 = input("escreva o terceiro lado: ")

equilatero = (L1 == L2) and (L2 == L3)
escaleno =  (L1 != L2) and (L2 != L3) and (L1 != L3)
tri = (L1 < L2 + L3) and (L2 < L1 + L3) and (L3 < L1 + L2)

print(f"Pode forma um TRIANGULO ? {tri}")
print(f'O triangulo é EQUILATERO? {equilatero}') 
print(f'O triangulo é ESCALENO ? {escaleno}') 
