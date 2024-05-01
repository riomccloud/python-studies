numeroMaximo = int(input("Digite um número: "))

for numerosIntermediarios in range(1,numeroMaximo+1):
    if numerosIntermediarios % 2 == 0:
        print(numerosIntermediarios)