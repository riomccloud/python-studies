numero = float(input("Digite um número: "))
resto = numero % 2

if resto == 0:
    print("O dividendo é par, porque não houve resto na divisão euclidiana.")
else:
    print("O dividendo é ímpar, porque houve resto na divisão euclidiana.")