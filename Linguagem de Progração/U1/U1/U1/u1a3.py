print("\nCLASSIFICAÇÃO DE FILMES\n")
print("Você tem cinco filmes para classificar\n")
print("Pressione 0 para encerrar a classificação\n")

filmes = ["filme 1", "filme 2", "filme 3", "filme 4", "filme 5"]

avaliacoes = []
for filme in filmes:
    nota = float(input("nota do {} de 1 a 5:\n".format(filme)))
    
    if nota == 0:
        print("Sistema de classificação encerrado!\n")
        break
    elif nota < 1 or nota > 5:
        print("Nota inválida! Apenas valores de 1 a 5.\n")
        break
    else:
        print("Nota registrada\n")
        avaliacoes.append(nota)


print("As notas para {} foram respectivamente {}".format(filmes, avaliacoes))

