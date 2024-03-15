'''
ladoA: float
ladoB: float
area: float

ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
area = ladoA * ladoB

print("A área do polígono equivale a " + str(area) + ".")

#---#

temperaturaFahrenheit: float
temperaturaCelsius: float

temperaturaFahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
temperaturaCelsius = (temperaturaFahrenheit - 32) / 1.8

print("O equivalente da temperatura informada é de " + str(temperaturaCelsius) + "º C.")

#---#

numeroInteiro1: int
numeroInteiro2: int
numeroReal: float

numeroInteiro1 = int(input("Digite o primeiro número inteiro: "))
numeroInteiro2 = int(input("Digite o segundo número inteiro: "))
numeroReal = float(input("Digite o terceiro número, desta vez real: "))

requisicao1: float
requisicao2: float
requisicao3: float
requisicao4: float

requisicao1 = (numeroInteiro1 * 2) * (numeroInteiro2 / 2)
requisicao2 = (numeroInteiro2 * 3) + numeroReal
requisicao3 = numeroReal ** 3
requisicao4 = numeroInteiro2 ** (1 / 3)

print("O resultado da primeira requisição é " + str(requisicao1) + ".")
print("O resultado da segunda requisição é " + str(requisicao2) + ".")
print("O resultado da terceira requisição é " + str(requisicao3) + ".")
print("O resultado da quarta requisição é " + str(requisicao4) + ".")
'''

descontoImpostoRenda: float
descontoINSS: float
descontoSindicato: float
salarioBruto: float
salarioHora: float
salarioLiquido: float
horasTrabalho: float

salarioHora = float(input("Informe seu salário por hora: "))
horasTrabalho = float(input("Informe quantas horas você trabalha por mês: "))
salarioBruto = salarioHora * horasTrabalho
descontoImpostoRenda = salarioBruto * 0.11
descontoINSS = salarioBruto * 0.08
descontoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - descontoImpostoRenda - descontoINSS - descontoSindicato

print("Seu salário bruto é de R$ " + str(salarioBruto) + ". São descontados R$ " + str(descontoImpostoRenda) + " para o Imposto de Renda, R$ " + str(descontoINSS) + " para o INSS e R$ " + str(descontoSindicato) + " para seu sindicato. Por fim, seu salário líquido é de R$ " + str(salarioLiquido) + ".")
