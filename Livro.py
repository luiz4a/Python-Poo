import os 
os.system("cls||clear")

class Livro :
    
    def __init__(self, tituloLivro: str , autor: str, Npaginas : int, anoLançamento: str, preco: float ) -> None:

        self.tituloLivro = tituloLivro
        self.autor = autor
        self.Npaginas = Npaginas 
        self.anoLançamento = anoLançamento 
        self.preco = preco

    def exibir_detalhes (self) -> str:
        return f"Titulo do Livro: {self.tituloLivro} \nAutor: {self.autor} \nNúmero de Páginas: {self.Npaginas} \nAno de lançamento: {self.anoLançamento} \nPreço: {self.preco}"
        
livro1 = Livro("É assim que acaba", " Colleen Hoover", 368, "29 de fevereiro de 2016", 43.21 )
livro2 = Livro ("Assassinato no expresso do oriente", "Agatha Christie", 240, "1 de janeiro de 1934", 38.45)

print("====Dados do Primeiro Livro====")
print(livro1.exibir_detalhes())
print("\n====Dados do Segundo Livro====")
print(livro2.exibir_detalhes())
