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