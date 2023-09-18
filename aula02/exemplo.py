class Cliente():
  def __init__(self, nome,email,plano):
    self.nome = nome
    self.email = email
    self.planos = ["basic", "premium"]
    if plano in self.planos:
      self.plano = plano
    else:
      print("Plano inválido")

  def mudarPlano(self,novoplano):
    if novoplano in self.planos:
      pass

cliente = Cliente("Tick", "lira@gmail.com", "balas")
cliente.mudarPlano("eheh")
