ano = int(input("Digite o ano que você deseja verificar: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("Este ano é bissexto.")
else:
    print("Este ano não é bissexto.")