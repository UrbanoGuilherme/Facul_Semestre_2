
class Veiculo:
    def __init__ (self, marca, modelo, ano): 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    
    def acelerar (self, incremento):
        self.velocidade += incremento

    def frear (self, decremento):
        self.velocidade_inicial = max(0, self.velocidade_inicial - decremento)

    def status (self):
       return (f"marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}")

class Carro (Veiculo):
    def __init__ (self, marca, modelo, ano, velocidade):
        super().__init__(marca, modelo, ano)
        self.velocidade = velocidade

    def acelerar (self, incremento):
        self.velocidade += incremento 

    def status (self):
       return (f"marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}, velocidade:{self.velocidade}")

class Bike (Veiculo):
    def __init__ (self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status (self):
        return (f"marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}, tipo:{self.tipo}")

carro1 = Carro("Honda", "Civic", 2025, 150)
bike1 = Bike("Trek", "Mountain", 2023, "MTB")

print(carro1.status())
print(bike1.status())

carro1.acelerar(100)
bike1.acelerar(20)

print(carro1.status())
print(bike1.status())
