def divisao(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Ocorreu um erro ao ler o valor. Tente novamente.")
    else:
        try:
            r = divisao(n1, n2)
        except ZeroDivisionError:
            print("Não é possível dividir por zero!")
        except Exception as e:
            print(f"Erro desconhecido: {e}")
        else:
            print(f"Resultado: {r}")
    finally:
        print("\nFim do cálculo!")


