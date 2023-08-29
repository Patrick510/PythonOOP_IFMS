# Vamos iniciar um projeto de controle bancário!

# O objetivo do projeto é o desenvolvimento orientado a objetos para a execução de tarefas do cotidiano bancário, como saque, consulta de saldo e depósito.

# Durante esta aula, já desenvolvemos a classe Cliente e seus atributos. Agora, vamos desenvolver a classe Conta, que será definida recebendo o objeto Cliente, além dos atributos “número” e “saldo”.

class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular