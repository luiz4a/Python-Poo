from enum import Enum 
import os 

class Sexo (Enum):
    """Definindo Enum."""
    FEMININO = "Feminino"
    MASCULINO = "Masculino"


class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RH = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing" 

class Funcionario:
    def __init__(self, nome: str, idade: int, sexo: Sexo, setor: Setor) -> None:
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo 
        self.setor = setor 

    def __str__(self) -> str:
        """Equivalente ao toString() do Java."""
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\nSetor: {self.setor.value}"
                )

funcionario1 =  Funcionario("Marta",23, Sexo.FEMININO, Setor.RH)

os.system("cls||clear")

print(funcionario1)