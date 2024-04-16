temperaturaFahrenheit: float
temperaturaCelsius: float

temperaturaFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
temperaturaCelsius = (temperaturaFahrenheit - 32) / 1.8

print("O equivalente da temperatura informada é de " + str(temperaturaCelsius) + "º C.")