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