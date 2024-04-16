numeroInteiro1: int
numeroInteiro2: int
numeroReal: float

numeroInteiro1 = int(input("Digite o primeiro número inteiro: "))
numeroInteiro2 = int(input("Digite o segundo número inteiro: "))
numeroReal = float(input("Digite o terceiro número, desta vez real: "))

requisicao1: float
requisicao2: float
requisicao3: float
requisicao4: float

requisicao1 = (numeroInteiro1 * 2) * (numeroInteiro2 / 2)
requisicao2 = (numeroInteiro2 * 3) + numeroReal
requisicao3 = numeroReal ** 3
requisicao4 = numeroInteiro2 ** (1 / 3)

print("O resultado da primeira requisição é " + str(requisicao1) + ".")
print("O resultado da segunda requisição é " + str(requisicao2) + ".")
print("O resultado da terceira requisição é " + str(requisicao3) + ".")
print("O resultado da quarta requisição é " + str(requisicao4) + ".")