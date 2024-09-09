from abc import ABC, abstractmethod
import os  

os.system("cls||clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        super().__init__(logradouro, numero, cidade)
        self.logradouro = logradouro
        self.numero = numero 
        self.cidade = cidade 

class Funcionario(ABC):
    def __init__(self,nome: str,email : str , salario: float, endereco: Endereco) -> None:
        self.nome = nome 
        self.email = email  
        self.salario = salario 
        self.endereco = endereco 

    def exibir_dados (self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.email} \nEmail: {self.salario} \nEndereço: {self.endereco}"
    
    #def __str__(self) -> str:
     #   return super().__str__()
    

@abstractmethod
def calcular_salario(self) -> float:
    pass 

class Motoboy (Funcionario):
    def __init__ (self, nome: str, email : str, salario : float, endereco : Endereco, CNH: str) -> (None):
        super().__init__ (nome, email, salario)
        self.cnh = CNH

class Gerente(Funcionario): 
    def calcular_salario(self) -> float:
        #Acréscimo de 20% 
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
    
endereco_gerente = Endereco("Rua pajussara", "44", "Salvador")
endereco_motoboy = Endereco("Av Eduardo Magalhaes", "12", "Salvador")
        
gerente = Gerente ("José", "j0hgjhg@gmail.com", 5896.0, endereco_gerente)    
motoboy = Motoboy ("Carlos", "carlosanderson@gmail.com", 1412.0, endereco_motoboy, "675489")

print(gerente.exibir_dados())
print(motoboy.exibir_dados())

