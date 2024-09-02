from abc import ABC, abstractmethod
import os  

os.system("cls||clear")

class Funcionario(ABC) :
    def __init__(self,nome: str, idade: int, salario: float) -> None:
        self.nome = nome 
        self.idade = idade 
        self.salario = salario 

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario): 
    def calcular_salario(self) -> float:
        #Acréscimo de 20% 
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
    
    
class Motoboy (Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, CNH: str) -> None:
        super().__init__(nome, idade, salario)
        self.CNH = CNH 

    def calcular_salario(self) -> float:
        #Acréscimo de 10%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final
    

#instanciar classes.
#funcionario1 = Funcionario ("Marta ", 45, 4568.0)

    

gerente1 = Gerente("Maria", 36, 1000.0)    
print("===Dados do Gerente===")   
print(f"Nome: {gerente1.nome}")
print(f"Sálario: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Carlos", 28, 1000.0, "7895684")       
print("\n===Dados do Motoboy===")   
print(f"Nome: {motoboy1.nome}")
print(f"Sálario: {motoboy1.calcular_salario()}")


        
        
        
        
        
        
        
        
        
