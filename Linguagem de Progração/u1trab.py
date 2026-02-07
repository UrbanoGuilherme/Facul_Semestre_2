print("\nCALCULADORA DE MÉDIA\n")

#Definição de uma função para calcular média
def calcular_media(notas):
    if not notas:
        print("\nValores de notas inválido! Insira novamente!")
        return None
    
    media = sum(notas)/len(notas)
    return media
    
    
#criação de lista vazia para armazenar notas
notas = []
#Laço para usuário inserir quantas notas quiser
while True:
    print("\nInsira as notas do aluno\n")
    nota = float(input("nota: "))
    if nota > 10 or nota < 0:
        print("Valor de nota inválido! Digite um valor de 0 a 10\n")
        continue
    #adicionar notas à lista
    notas.append(nota)

    opcao = int(input("\nDeseja inserir mais uma nota? 1 => SIM || 2 => NÃO\n"))

    if opcao == 2:
        print("Notas salvas!\n")
        break
    elif opcao == 1:
        continue
    else:
        print("Opção inválida!\n")
        continue

#apresentação das notas e média (chamando a função)
print("As notas inseridas foram:{}\n".format(notas))
media = calcular_media(notas)
print("A média das notas inseridas = {}\n".format(round(media, 2)))

#condiçào de aprovação
if media >= 7:
    print("Aluno aprovado!\n")
else:
    print("Aluno reprovado!\n")


