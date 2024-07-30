# from random import shuffle
# j1 = ['Jose', 'Bruno', 'Ivanilson', 'Eduardo', 'Vitoria',]
# j2 = ['Davi', 'Milena', 'Anderson', 'Matheus', 'Paulo',]
# j3 = ['Artur', 'Anderson', 'Gustavo', 'Rogerio', 'Marcus',]

# shuffle(j1)
# shuffle(j2)
# shuffle(j3)

# for n, (c1, c2, c3) in enumerate(zip(j1, j2, j3), start=1):
#     print(f'Equipe {n}: {c1}, {c2}, {c3}')
    
    
import random

while True:
    aluno = input('Digite o nome do aluno (ou 0 para parar): ')
    if aluno == '0':
        break
    sorteio = random.choice(aluno)
    print(f'{sorteio} é o sorteado!')
