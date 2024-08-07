# Criando os arquivos e escrevendo os nomes de gatos e cachorros
try:
    with open("cats.txt", "w") as cats_file:
        cats_file.write("Whiskers\n")
        cats_file.write("Luna\n")
        cats_file.write("Simba\n")

    with open("dogs.txt", "w") as dogs_file:
        dogs_file.write("Buddy\n")
        dogs_file.write("Max\n")
        dogs_file.write("Bailey\n")

    print("Arquivos criados com sucesso!")

except FileNotFoundError:
    print("Ops! Parece que um dos arquivos não foi encontrado. Verifique se os nomes estão corretos.")


import shutil



#except FileNotFoundError:
  #  print("O arquivo cats.txt não foi encontrado na localização original.")


try:
    with open("catss.txt", "r") as cats_file:
        print("\nConteúdo do arquivo cats.txt:")
        print(cats_file.read())

    with open("dogs.txt", "r") as dogs_file:
        print("\nConteúdo do arquivo dogs.txt:")
        print(dogs_file.read())

except FileNotFoundError:
    print("Ops! Algo deu errado ao tentar ler os arquivos.")

# Exception - Classe base para todas as excerçoes
# ArithmeticError - Classe base para o erros que ocorrem em calculos numericos
# OverflowError - Um calculo excedeu o limite maxximo de um tipo numerico
# ZeroDivisionError - Lançada quando uma divisao ou modulo por zero é exerdutada em tipos numericos
# ImportError - Lançada quando uma declaraçao import falha
# NameError - Um Identificador(nome) nao foi encontrado no namespace local ou global
# IOError - Ocorre quando uma operaçao de E/S, como ler ou escrever em  Arquivo,falha
# IndentationError - Aidentaçao nao foi aplicada corretamente.
# RecursionError - O interpretador detectou que a profundidade maxima de recursao foi excerdida
# TypeError - Lançada quando uma funçao ou operaççao é invalida para o tpo de dados espercificado.