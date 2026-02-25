"""class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
    def cumprimentar (self):
        return "olá, meu nome é {}".format(self.nome)
    def aniversario(self):
        self.idade +=1 

pessoa1 = Pessoa("Gui", 23, "masculino")
print(pessoa1.cumprimentar())
print("idade: {}".format(pessoa1.idade))
pessoa1.aniversario()
print("nova idade: {}".format(pessoa1.idade))"""""


class ContaBancaria:
    def __init__(self, titular, saldo): 
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
        print("o novo saldo é: ", self.saldo)
    def sacar(self, valor):
        self.saldo-= valor
        print("o novo saldo é: ", self.saldo)
    def exibir_infos(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

titular1 = str(input("digite o nome do titular:"))
saldo1 = float(input("digite o saldo da conta:"))

conta1 = ContaBancaria(titular1, saldo1)

while True:
    print("selecione:")
    print("1 - visualizar infos")
    print("2 - depositar")
    print("3 - sacar")
    print("4 - sair")
    opcao = int(input("digite:"))

    if opcao == 1:
       conta1.exibir_infos()

    elif opcao == 2:
        valor = float(input("valor para deposito:"))
        conta1.depositar(valor)

    elif opcao == 3:
        valor = float(input("valor para sacar:"))
        conta1.sacar(valor)

    elif opcao == 4:
        print("encerrando sistema...")
        break

    else:
        print("opcao invalida")
        





