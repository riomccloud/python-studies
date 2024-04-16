numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = str(input("Digite a operação desejada (adicao, subtracao): "))

if operacao == str("adicao"):
    print("O resultado desta adição é", numero1+numero2)
elif operacao == str("subtracao"):
    print("O resultado desta subtração é", numero1-numero2)
else:
    print("A operação que você informou é inválida. Por favor, leia as instruções com atenção e tente novamente.")