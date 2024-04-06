from msilib.schema import Media
from statistics import median_low


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segumda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))


Media = (nota1 + nota2 + nota3 + nota4) / 4

print('A media é:', Media)