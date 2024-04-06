# UƟlizando a imagem abaixo, crie as respecƟvas classes apresentadas. 
class Editoras:
    def __init__(self, codEditora, razaoSocial, contao, telefone):
        self.codEditora = codEditora
        self.razaoSocial = razaoSocial
        self.contao = contao
        self.telefone = telefone

class Livros:
    def __init__(self, codigo, descLivro, ISBN, editora):
        self.codigo = codigo
        self.descLivro = descLivro
        self.ISBN = ISBN
        self.editora = editora  
