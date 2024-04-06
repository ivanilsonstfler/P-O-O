# Python 3 code
texto = input("Digite uma frase: ")
palavra = input("Escolha uma palavra da frase: ")
palavras = texto.split()
try:
    indice = palavras.index(palavra)
    print("A palavra '", palavra, "' está na posição ", indice, " da frase.")
except ValueError:
    print("A palavra '", palavra, "' não foi encontrada na frase.")

