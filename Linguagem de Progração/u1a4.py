print("\nCALCULANDO MÉDIAS\n")


def calcular_media (notas_gerais):
    if not notas_gerais:
        print("Valor de divisor inválido. Adicione notas.")
        return None
    
    media = sum(notas_gerais)/len(notas_gerais)
    return media


arredondar_media = lambda media: round(media,2)



notas_gerais = []

while True:
    notas = float(input("\nInsira a nota:"))
    notas_gerais.append(notas)

    print("\nDeseja inserir mais uma? (1 => sim || 2 => não)")
    opcao = int(input("\n"))
    if opcao == 2:
        print("\nObrigado por utilizar o sistema! Finalizado.\n")
        break
    elif opcao == 1:
        continue


print("As notas registradas foram:", notas_gerais)
print()

media_final = calcular_media(notas_gerais)
print("A média final arredondada foi:", arredondar_media(media_final))
