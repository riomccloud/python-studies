opcao: int = 1

while opcao >=1:
	print('1 - Somar')
	print('2 - Subtrair')
	print('3 - Multiplicar')
	print('4 - Dividir')
	print('0 - Sair')

	opcao = int(input('Digite uma opção: '))

	if opcao == 1 or opcao == 2 or opcao == 3 or operacao == 4:
		continuaOperando = True
		operacao = int(input("Digite o primeiro número: "))
		while continuaOperando == True:
			proximoValor = int(input("Digite o próximo número (0 para parar): "))
			if proximoValor == 0:
				continuaOperando = False
			elif opcao == 1:
				operacao = operacao + proximoValor
			elif opcao == 2:
				operacao = operacao - proximoValor
			elif opcao == 3:
				operacao = operacao * proximoValor
			elif opcao == 4:
				operacao = operacao / proximoValor
		print(operacao)
	elif opcao == 0:
		break
	else:
		print("Você digitou um valor inválido. Tente novamente.\n")