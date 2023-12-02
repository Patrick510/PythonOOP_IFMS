from id import Id

class Produto(Id):
  produto_nome = "CHINELINHA"
  
  @staticmethod
  def mostraIdade():
    print("IDADE 19")
  
  @classmethod
  def mostraProduto(cls):
    print(cls.produto_nome)
  
  def __init__(self,idproduto,nome,preco):
    super().__init__(idproduto)
    self.nome = nome
    self.preco = preco

  def mostra_id(self):
    return super().mostra_id()

  def desconto(self,valor):
    self.preco = self.preco - (valor / 100)

  @property
  def preco(self):
    return self._preco

  @preco.setter
  def preco(self,valor):
    if isinstance(valor, str):
      valor = float(valor.replace("R$",""))
    self._preco = valor

p1 = Produto(1, "Chinelo", 10)
p1.desconto(10)
print(p1.idproduto, p1.nome, p1.preco)

p1.mostraProduto()
p1.mostraIdade()