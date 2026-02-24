print("SISTEMA DE VENDAS\n")

registro_vendas = []

tot_vendas_por_prod = {}

while True:
    data = int(input("insira a data da venda (ddmm): "))
    produto = str(input("insira o produto:"))
    qtd = int(input("insira a quantidade vendida:"))
    preco = float(input("insira o preco unitário:"))

    venda = (data, produto, qtd, preco)
    registro_vendas.append(venda)

    total_venda = qtd*preco

    if produto in tot_vendas_por_prod:
        tot_vendas_por_prod[produto] += total_venda
    else:
        tot_vendas_por_prod[produto] = total_venda

    continuar = int(input("deseja inserir mais produtos? (1 => SIM, 2 => NÃO)"))
    if continuar != 1:
        break

"""print("total de vendas por produto")
for produto, total in tot_vendas_por_prod.items():
    print(produto, "R$", total)"""""

print(registro_vendas, tot_vendas_por_prod)