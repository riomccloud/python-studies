numeroMaximo = int(input("Digite um número: "))

if numeroMaximo <= 1:
    print("Palhaço")
    exit()

for i in range (2,numeroMaximo+1):
    statusPrimo = ""
    for j in range (2,i):
        if i % j == 0:
            statusPrimo = 0
            break
    if not statusPrimo == 0:
        print(f"{i} é primo.")

'''
statusPrimo = ""
supostoPrimo = int(input("Digite um número: "))

if supostoPrimo == 1:
    print("se mata")
    exit()

for i in range (2,supostoPrimo):
    if supostoPrimo % i == 0:
        statusPrimo = 0
        print(f"{supostoPrimo} não é primo.")
        exit()

if not statusPrimo == 0:
    print(f"{supostoPrimo} é primo.")
'''