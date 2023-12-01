from abc import ABC,abstractmethod

class Id(ABC):
  def __init__(self,idproduto):
    self.idproduto = idproduto

  @abstractmethod
  def mostra_id(self):
    print(f"id: {self.idproduto}")
