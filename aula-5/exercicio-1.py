numero1: float
numero2: float
forma: str

print("1 - Adicao")
print("2 - Subtracao")
print("3 - Multiplicacao")
print("4 - Divisao")

forma = input("Digite a opção desejada: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if forma == "1" or forma == "Adicao":
    print(numero1 + numero2)
elif forma == "2" or forma == "Subtracao":
    print(numero1 - numero2)
elif forma == "3" or forma == "Multiplicacao":
    print(numero1 * numero2)
elif forma == "4" or forma == "Divisao":
    print(numero1 / numero2)
else:
    print("Você digitou uma operação inválida. Por favor, reinicie o programa e tente novamente.")