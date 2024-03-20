'''
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
maiorQue = numero1>numero2
maiorIgual = numero1>=numero2
menorQue = numero1<numero2
menorIgual = numero1<=numero2
igual = numero1==numero2
diferente = numero1!=numero2

print("O número 1 é maior que o número 2? " + str(maiorQue))
print("O número 1 é maior ou igual ao número 2? " + str(maiorIgual))
print("O número 1 é menor que o número 2? " + str(menorQue))
print("O número 1 é menor ou igual ao número 2? " + str(menorIgual))
print("O número 1 é igual ao número 2? " + str(igual))
print("O número 1 é diferente do número 2? " + str(diferente))

==========

x: int = 7
menorQue10MaiorQue5 = (10 > x) and (x > 5)

print("O número X é menor que 10 e maior que 5? " + str(menorQue10MaiorQue5))

==========

numero = float(input("Digite um número: "))
resto = numero % 2

if resto == 0:
    print("O dividendo é par, porque não houve resto na divisão euclidiana.")
else:
    print("O dividendo é ímpar, porque houve resto na divisão euclidiana.")

==========

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print("O maior número é o", numero1)
else:
    print("O maior número é o", numero2)

'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = str(input("Digite a operação desejada (adicao, subtracao): "))

if operacao == str("adicao"):
    print("O resultado desta adição é", numero1+numero2)
elif operacao == str("subtracao"):
    print("O resultado desta subtração é", numero1-numero2)
else:
    print("A operação que você informou é inválida. Por favor, leia as instruções com atenção e tente novamente.")