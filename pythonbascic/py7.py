# Instanciando um novo Objeto
# Com a classe recem importada "Project"

class Project:
    pass

print('Testando o projeto')

from py4 import Cliente
from py8 import Conta

c1 = Cliente("Jonas", "4002-8922")
conta = Conta(c1.nome, 6565, 0)

print(c1,"\n") # Aqui sera mostrado o ID do objeto
print(c1.nome," e ",c1.telefone) # Aqui vai exibir o conteúdo do objeto
print(conta.titular,' Numero: ',conta.numero,' Seu saldo: ',conta.saldo)