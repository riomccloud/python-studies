print("1 - Categoria A")
print("2 - Categoria B")
print("3 - Categoria C")

categoriaProduto = str(input("\nInforme a categoria do produto: "))
precoProduto = float(input("Informe o preço do produto: "))

if categoriaProduto == "1" or categoriaProduto == "Categoria A":
    precoFinal = precoProduto - (precoProduto * 0.1)
    print("O preço do produto é de R$ " + str(precoFinal) + ".")
elif categoriaProduto == "2" or categoriaProduto == "Categoria B":
    precoFinal = precoProduto - (precoProduto * 0.15)
    print("O preço do produto é de R$ " + str(precoFinal) + ".")
elif categoriaProduto == "3" or categoriaProduto == "Categoria C":
    precoFinal = precoProduto - (precoProduto * 0.2)
    print("O preço do produto é de R$ " + str(precoFinal) + ".")
else:
    print("Você digitou uma categoria inválida. Por favor, tente novamente.")