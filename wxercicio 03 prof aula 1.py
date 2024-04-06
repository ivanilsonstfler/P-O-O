eleitores = int(input('Digite o total de eleitores: '))
votobranco = int(input('Quantidade de votos brancos: '))
votonulo = int(input('Quantidades de votos nulos: '))

percbranco = (votobranco * 100) / eleitores
percnulo = (votonulo * 100) / eleitores
percvalido = 100 - (percbranco + percnulo)

print("Percentual de votos brancos: ", percbranco, "%")
print("Percentual de votos nulos: ", percnulo, "%")
print("Percentual de votos válidos: ", percvalido, "%")

