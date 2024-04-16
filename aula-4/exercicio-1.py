peso = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (m): "))

# Arrendonda os decimais em até duas casas
imc = round(peso / (altura ** 2), 2)

if imc < 16:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Magreza Grave'.")
elif imc < 17:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Magreza Moderada'.")
elif imc < 18.6:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Magreza Leve'.")
elif imc < 25:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Peso Ideal'.")
elif imc < 30:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Sobrepeso'.")
elif imc < 35:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Obesidade Grau 1'.")
elif imc < 40:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Obesidade Grau 2 - Severa'.")
else:
    print("Seu índice de massa corporal é de " + str(imc) + ", classificado como 'Obesidade Grau 3 - Mórbida'.")
