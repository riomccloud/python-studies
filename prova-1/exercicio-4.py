numeroMediano: float

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))
terceiroNumero = float(input("Digite o terceiro número: "))

if (primeiroNumero > segundoNumero and primeiroNumero < terceiroNumero) or (primeiroNumero < segundoNumero and primeiroNumero > terceiroNumero):
    numeroMediano = primeiroNumero
elif (segundoNumero > primeiroNumero and segundoNumero < terceiroNumero) or (segundoNumero < primeiroNumero and segundoNumero > terceiroNumero):
    numeroMediano = segundoNumero
elif (terceiroNumero > primeiroNumero and terceiroNumero < segundoNumero) or (terceiroNumero < primeiroNumero and terceiroNumero > segundoNumero):
    numeroMediano = terceiroNumero
else:
    print("Você digitou números iguais. Você deve informar números distintos.")
    exit()
print("O número mediano é " + str(numeroMediano) + ".")