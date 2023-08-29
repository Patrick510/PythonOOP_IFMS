# Instanciando um novo Objeto
# Com a classe recem importada "Project"

class Project:
    pass

print('Testando o projeto')

from py4_first_class import Cliente
from py8_cont import Conta

c1 = Cliente("Jonas", "4002-8922")
conta = Conta(c1.nome, 6565, 0)

print(c1,"\n") # Aqui sera mostrado o ID do objeto
print(c1.nome," e ",c1.telefone) # Aqui vai exibir o conteúdo do objeto
print(conta.titular,' Numero: ',conta.numero,' Seu saldo: ',conta.saldo)