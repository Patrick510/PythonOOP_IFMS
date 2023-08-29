class Project:
    pass

print('Testando o projeto \n')

from client import Cliente
from account import Conta

c1 = Cliente("Jonas", "4002-8922")
conta = Conta(c1._nome,6565,0)

print(c1._nome," e ",c1._telefone,"\n")
print(conta.titular,' Numero:',conta.numero,' Seu saldo:', conta.saldo)
