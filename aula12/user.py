from id import Id

class Produto(Id):
  produto1 = "vazio"

  @classmethod
  def mostraprod(cls):
    print(cls.produto1)

  @staticmethod
  def idade(idade):
    if idade > 18:
      print(True)
    else:
      print(False)

  def __init__(self,idproduto,nome,preco):
    super().__init__(idproduto)
    self.nome = nome
    self.preco = preco

  def desconto(self,percentual):
    self.preco = (self.preco - (percentual / 100))

  def mostra_id(self):
    return super().mostra_id()

  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self,texto):
      self._nome = texto.lower().title()

  #getter
  @property
  def preco(self):
    return self._preco

  #setter
  @preco.setter
  def preco(self, valor):
    if isinstance(valor, str):
      valor = float(valor.replace("R$",""))
    self._preco = valor


p1 = Produto(1,"camisetA", 10)
p1.desconto(10)
print(f'id: {p1.idproduto}| preco: {p1.preco}| nome: {p1.nome}')

p2 = Produto(2,"canecA", "R$15")
p2.desconto(10)
print(p2.preco, p2.nome)

p1.mostraprod()
p1.idade(19)

p1.mostra_id()