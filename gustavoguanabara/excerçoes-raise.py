if __name__ == '__main__':
    try:
        num = float(input("Digite um número positivo: "))
        if num < 0:
            raise ArithmeticError
    except ValueError:
        print("Você deve fornecer um número válido.")
    except ArithmeticError:
        print("Foi fornecido um número negativo!")
    else:
        print(f"A raiz quadrada de {num} é {sqrt(num)}")
    finally:
        print("Fim do cálculo!")
