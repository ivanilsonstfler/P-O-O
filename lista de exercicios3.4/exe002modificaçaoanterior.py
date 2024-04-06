#Ler um valor N e imprimir todos os valores 
#inteiros entre 1 (inclusive) e N (inclusive).
#Considere que o N será sempre maior que ZERO.


n = int(input("Digite um valor para N: ")) 

while n <= 0:
    print("O valor de N deve ser maior que 0. Digite novamente.")
    n = int(input("Digite um valor para N: "))

for i in range(1, n+1):
    print(i)
