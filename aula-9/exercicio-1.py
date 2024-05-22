import random

numeroSecreto: int = random.randint(1,10000)
numeroDigitado: int = ""

while numeroDigitado != numeroSecreto:
    numeroDigitado = int(input("Digite um número de 1 a 10000: "))
    if numeroDigitado != numeroSecreto:
        print("Errou!")
        if numeroDigitado < numeroSecreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")
print("Você acertou!")