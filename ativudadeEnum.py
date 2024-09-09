from enum import Enum 
import os 

class Sexo (Enum):
    """Definindo Enum."""
    FEMININO = "Feminino"
    MASCULINO = "Masculino"

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo 

    def __str__(self) -> str:
        """Equivalente ao toString() do Java."""
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                )

pessoa1 =  Pessoa("Marta",23, Sexo.FEMININO)

os.system("cls||clear")

print(pessoa1)