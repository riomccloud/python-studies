areaCirculo: float
circunferenciaCirculo: float
diametroCirculo: float

raioCirculo = float(input("Digite o valor do raio do círculo: "))

areaCirculo = 3.14 * (raioCirculo ** 2)
circunferenciaCirculo = 2 * 3.14 * raioCirculo
diametroCirculo = 2 * raioCirculo

print("Este círculo possui área de valor " + str(areaCirculo) + ", circunferência de valor " + str(circunferenciaCirculo) + " e diâmetro de valor " + str(diametroCirculo) + ".")