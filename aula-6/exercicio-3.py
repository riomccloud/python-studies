maiorNumero: float
numeroMediano: float
menorNumero: float

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Você digitou números iguais. Esse algoritmo é feito para números distintos.")
    exit()
elif numero1 > numero2 and numero1 > numero3:
    maiorNumero = numero1
    if numero2 > numero3:
        numeroMediano = numero2
        menorNumero = numero3
    else:
        numeroMediano = numero3
        menorNumero = numero2
elif numero2 > numero1 and numero2 > numero3:
    maiorNumero = numero2
    if numero1 > numero3:
        numeroMediano = numero1
        menorNumero = numero3
    else:
        numeroMediano = numero3
        menorNumero = numero1
elif numero3 > numero1 and numero3 > numero2:
    maiorNumero = numero3
    if numero1 > numero2:
        numeroMediano = numero1
        menorNumero = numero2
    else:
        numeroMediano = numero2
        menorNumero = numero1

print(float(maiorNumero))
print(float(numeroMediano))
print(float(menorNumero))