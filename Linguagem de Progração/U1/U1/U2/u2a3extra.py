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
        if valor > 0:
            self.saldo += valor
            print("o novo saldo é: ", self.saldo)
        else:
            print("erro! digite um valor maior que zero")

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo-= valor
            print("o novo saldo é: ", self.saldo)
        else:
            print("erro! digite um valor menor que o saldo total")

    def exibir_infos(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)

class ContaPoupança(ContaBancaria): 
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        self.limite = 500


contas = []

while True:
    print("selecione:")
    print("1 - criar conta corrente")
    print("2 - listar contas")
    print("3 - depositar")
    print("4 - sacar")
    print("5 - sair")
    print("6 - criar conta poupança")
    opcao = int(input("digite:"))

    if opcao == 1:
       titular = input("digite o nome do titular:")
       saldo = float(input("digite o saldo:"))
       conta = ContaBancaria(titular, saldo)
       contas.append(conta)
       print("conta criada!")

    elif opcao == 2:
        for i, conta in enumerate(contas):
            print(f"{i} - titular: {conta.titular} | saldo: {conta.saldo}")

    elif opcao == 3:
        indice = int(input("escolha a conta:"))
        valor = float(input("valor para depositar:"))
        contas[indice].depositar(valor)
        print(f"o novo saldo do titular {contas[indice].titular} é: {contas[indice].saldo}")
        
    elif opcao == 4:
        indice = int(input("escolha a conta:"))
        valor = float(input("valor para saque:"))
        contas[indice].sacar(valor)
        print(f"o novo saldo do titular {contas[indice].titular} é: {contas[indice].saldo}")
    
    elif opcao == 5:
        print("encerrando...")
        break

    elif opcao == 6:
        titular = input("digite o nome do titular:")
        saldo = float(input("digite o saldo:"))
        

    else:
        print("opcao invalida")
        





