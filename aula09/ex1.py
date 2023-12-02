"""
Propriedades dinâmicas

Como a constante π é uma dízima não periódica, não é possível determinar seu valor exato. Dependendo das necessidades de sua aplicação, é aceitável que o π tenha um certo nível de precisão. 
Desenvolva uma classe Math que possua uma propriedade pi, que retorna o valor do π com um determinado número de casas decimais. 
Essa classe também possui um atributo de classe precision, que indica o número de casas decimais que a propriedade pi deve gerar. 
Para simplificar, considere que a classe Math pode gerar um π de até um valor máximo determinado de casas decimais.

Crie um módulo para testar a classe Math do exercício anterior. Neste módulo, calcule o perímetro de um círculo usando diferentes valores de precisão para π.
"""

import math

class Math:
    _limite_precisao = 15  # Limite máximo de casas decimais para o π

    @classmethod
    def definir_precisao(cls, precisao):
        if precisao > cls._limite_precisao:
            precisao = cls._limite_precisao
        cls.precisao = precisao

    @property
    def pi(self):
        return round(math.pi, self.precisao)

# Configurar a precisão desejada (por exemplo, 5 casas decimais)
Math.definir_precisao(5)

# Testar a classe Math
print(f"Pi com precisão de {Math.precisao} casas decimais: {Math().pi}")

# Calcular o perímetro de um círculo usando o π com diferentes precisões
raio = 5.0
perimetro_precisao_2 = 2 * Math().pi * raio
print(f"Perímetro do círculo com precisão 2: {perimetro_precisao_2}")

# Alterar a precisão para 3 casas decimais
Math.definir_precisao(3)
perimetro_precisao_3 = 2 * Math().pi * raio
print(f"Perímetro do círculo com precisão 3: {perimetro_precisao_3}")
