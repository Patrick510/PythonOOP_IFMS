class ControleRemoto:
  def __init__(self, cor,altura,profundidade,largura):
# anotação
    self.cor = cor
    self.altura = altura
    self.profundidade = profundidade
    self.largura = largura

  def passarCanal(self, botao):
    if botao == "+":
      print('Aumentar Canal')
    elif botao == "-":
      print('Diminuir Canal')

controle = ControleRemoto('green','1cm','3cm','1cm')
print("Control 1 have color",controle.cor)

controle.passarCanal("+")

controle2 = ControleRemoto('blue','1cm','3cm','1cm')
print("Control 2 have color",controle2.cor)
controle2.passarCanal('-')