import os

os.system("cls||clear") 

class Endereço:
    def __init__(self, logradouro: str, numero : int) -> None:
        self.logradouro = logradouro        
        self.numero = numero 


    def __str__(self) -> str:
        return f"Logradouro: {self.logradouro} \nNumero: {self.numero}"

class Aluno:
    def __init__(self, nome: str , idade: int, endereco: Endereço) -> None:
        self.nome = nome
        self.idade = idade 
        self.endereco = endereco 

    def exibir_dados (self) -> str:
       return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"

aluno1 = Aluno ("Marta",20, Endereço("Av.pajussara", 44))

print(aluno1.exibir_dados())

