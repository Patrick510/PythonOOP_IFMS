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
      self.plano = novoplano
    else:
      print("Plano invalido")
      
  def verFilme(self,filme,planoFilme):
    if self.plano == planoFilme:
      print(f"Ver filme {filme}")
    elif self.plano == "premium":
      print(f"Ver filme {filme}")
    elif self.plano == "basic" and planoFilme == "premium":
      print("faça upgrade pra premium pae")
    else:
      print("Plano inválido")

cliente = Cliente("Tick", "lira@gmail.com", "basic")
#print(cliente.plano)
#cliente.verFilme("Harry Potter", "premium")
#print("MUDANDO PLANO...")

#upgrade
#cliente.mudarPlano("premium")
#print(cliente.plano)
#cliente.verFilme("Harry Potter", "premium")

cliente2 = Cliente("Honaldo", "gmail.com", "premium")
