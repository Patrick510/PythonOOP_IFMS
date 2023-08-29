# Aplicando na pratica encapsulamento
# Vou mexer nos atributos da classe Cliente

class Cliente:
    def __init__(self, n, fone):
        
        self._nome = n # Foi adicionado um underline(_) antes da definição do nome atributo
        self._telefone = fone