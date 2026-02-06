print("CALCULADORA DE DESCONTO")


carrinho_compra = []

while True:
    valores = float(input("\nInsira o valor do produto:"))
    carrinho_compra.append(valores)

    print("\nDeseja inserir mais um? (1 => sim || 2 => não)")
    opcao = int(input("\n"))
    if opcao == 2:
        print("\nProdutos Inseridos!\n")
        break
    elif opcao == 1:
        continue

porcent_desconto = float(input("insira o valor em (%) do desconto:"))

if porcent_desconto < 0 or porcent_desconto > 100:
    print("Valor invalido! Ele deve ser entre 0 e 100%\n")
else:
    valor_desconto = sum(carrinho_compra) * (porcent_desconto/100)
    valor_final = sum(carrinho_compra) - valor_desconto


print("O valor do desconto foi de R$", valor_desconto) 

print("O valor final da compra foi de R$", valor_final)