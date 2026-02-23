print("FILME EM CARTAZ: FILME 1, FILME 2 E FILME 3\n")

idade = int(input("Digite sua idade:\n"))

if idade < 12:
    print("Sua idade é {}, por isso recomendamos o filme infantil 1".format(idade))
elif idade >= 12 and idade < 18:
    print("Sua idade é {}, por isso recomendamos o filme juvenil 2".format(idade))
else:
    print("Sua idade é {}, por isso recomendamos o filme adulto 3".format(idade))

while True:
    print("\nselecione o filme que deseja assistir:")
    print("FILME 1")
    print("FILME 2")
    print("FILME 3")
    opcao = int(input("digite aqui: "))

    if opcao == 1:
        if idade < 12:
            print("\nÓtima escolha!")
            break
        else:
            print("\nBoa escolha! Esse filme é indicado para crianças, mas voce irá gostar!")
            break
    if opcao == 2:
        if idade >=12 and idade < 18:
            print("\nÓtima escolha!")
            break
        elif idade > 18:
            print("\nBoa escolha! Esse filme é indicado para idades entre 12 e 18, mas você irá gostar!")
            break
        else:
            print("\nVoce ainda não tem idade mínima para esse filme! Escolha outra opção")
            continue
    if opcao == 3:
        if idade >= 18:
            print("\nÓtima escolha!")
            break
        else:
            print("\nVoce ainda não tem idade mínima para esse filme! Escolha outra opção")
            continue


import random 

print("\nSELEÇÃO DE INGRESSOS")

ingressos = random.randint(0,10)

pedido = int(input("\nDigite a quantidade de ingressos que deseja:"))

print("\nPara esse filme temos {} ingressos".format(ingressos))

if pedido >= ingressos:
    print("\nQuantidade indisponível!")
else:
    print("\nQUantidade disponível! Aproveite!")
