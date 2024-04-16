forma: float

lado1 = input("Digite o valor do lado 1 do triângulo: ")
lado2 = input("Digite o valor do lado 2 do triângulo: ")
lado3 = input("Digite o valor do lado 3 do triângulo: ")

if lado1 == lado2 and lado1 == lado3:
    print("Este é um triângulo equilátero.")
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
    print("Este é um triângulo escaleno.")
else:
    print("Este é um triângulo isósceles.")