velocidade = float(input('Digite sua velocidade do Carro?' ))
 
if velocidade > 80:
     print('MULTADO!voce excedeu o limite de velocidade permitida')
     multa = (velocidade-80) * 8
     print('O valor da multa é{}'.format(multa))