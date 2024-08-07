while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        resultado = n1 + n2
        print(f"A soma de {num1} e {num2} é igual a {resultado}")
    except ValueError:
        print("Número digitado inválido. Insira um valor numérico.")


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