import os

os.system("cls||clear") # limpar terminal 

class Aluno:
    #nome, idade 
    def __init__(self, nome: str , idade: int) -> None:
        #Atributos
        self.nome = nome
        self.idade = idade 

    def exibir_dados (self) -> str:
       return f"nome: {self.nome} \nIdade: {self.idade}"


#instancia classe 
aluno = Aluno ("Marta", 18)

#print(f"Nome:  {aluno.nome}")
#print(f"Idade: {aluno.idade}")
print(aluno.exibir_dados())


