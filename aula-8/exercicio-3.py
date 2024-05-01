primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite outro número: "))

if primeiroNumero > segundoNumero:
    numeroMenor = segundoNumero
    numeroMaior = primeiroNumero
else:
    numeroMenor = primeiroNumero
    numeroMaior = segundoNumero

for tabuada in range(numeroMenor,numeroMaior+1):
    for numerosTabuada in range (1, 11):
        print(f"{tabuada} x {numerosTabuada} =", tabuada * numerosTabuada)
    print("")