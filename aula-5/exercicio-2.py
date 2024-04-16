import math

forma: str

print("1 - Circulo")
print("2 - Losango")
print("3 - Retangulo")
print("4 - Triangulo")

forma = input("Digite a forma geométrica desejada: ")

if forma == "1" or forma == "Circulo":
    raio: float = float(input("Digite o valor do raio: "))
    print(math.pi * (raio ** 2))
elif forma == "2" or forma == "Losango":
    diagonalMaior: float = float(input("Digite o valor da diagonal maior: "))
    diagonalMenor: float = float(input("Digite o valor da diagonal menor: "))
    print((diagonalMaior * diagonalMenor) / 2)
elif forma == "3" or forma == "Retangulo":
    comprimento: float = float(input("Digite o valor do comprimento: "))
    largura: float = float(input("Digite o valor da largura: "))
    print(comprimento * largura)
elif forma == "4" or forma == "Triangulo":
    altura: float = float(input("Digite o valor da altura: "))
    base: float = float(input("Digite o valor da base: "))
    print((altura * base) / 2)
else:
    print("Você digitou uma forma geométrica inválida. Por favor, reinicie o programa e tente novamente.")