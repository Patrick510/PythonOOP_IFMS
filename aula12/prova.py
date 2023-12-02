class Estudante:
    def __init__(self,nome,sobrenome,notas):
        self._nome = self.altera_tipo_nome(nome).title()
        self._sobrenome = self.altera_tipo_sobrenome(sobrenome).title()
        self._notas = notas

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        if str.isalpha(nome) is False:
            print("digite apenas letras") 
            self._nome = None
        else:
            self._nome = nome
        return self._nome
            

    def altera_tipo_nome(self,valor):
        self.nome = str(valor)
        return self.nome
    
    def altera_tipo_sobrenome(self,valor):
        self.sobrenome = str(valor)
        return self.sobrenome
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self, sobrenome):
        if str.isalpha(sobrenome) is False:
            print("digite apenas letras") 
            self._sobrenome = None
        else:
            self._sobrenome = sobrenome
        return self._sobrenome
    
    @property
    def notas(self):
        return self._notas
    
    @notas.setter
    def notas(self,notas):
        self._notas = float(notas)
        return self._notas
    
    @property
    def nomecompleto(self):
        if self.nome is not None and self.sobrenome is not None:
            return f"{self.nome} {self.sobrenome}"
        else:
            return "Nome incompleto"
    
    @property
    def mostranotas(self):
        notas_str = ', '.join(map(str, self.notas))
        return notas_str

    def excluirnota(self, id):
        del self._notas[id]
        return self.notas
    
    @property
    def media(self):
        media = sum(self.notas) / len(self.notas)
        return media

notas = [10,5,8]
e1 = Estudante("joao","matias",notas)

print(e1.nome, e1.sobrenome, e1._notas)
print(e1.nome, e1.sobrenome, e1._notas)
print(e1.nomecompleto)

print(e1.media)
print(e1.mostranotas)