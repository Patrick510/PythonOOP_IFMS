import math

class Conta:
  _limite_precisao = 15
  precisao = _limite_precisao

  @classmethod
  def definir_precisao(cls, precisao):
    if precisao > cls._limite_precisao:
      precisao = cls._limite_precisao
    cls.precisao = precisao

  @property
  def pi(self):
    return round(math.pi, self.precisao)


Conta.definir_precisao(5)
print(f"Pi com precisao de {Conta().precisao} casas decimais: {Conta().pi}")

raio = 5.0
Conta.definir_precisao(2)
perimetro1 = 2 * Conta().pi * raio
print(f"Perímetro do círculo com precisão 2: {perimetro1}")

Conta.definir_precisao(3)
perimetro2 = 2 * Conta().pi * raio
print(f"Perímetro do circulo com precisao 3: {perimetro2}")