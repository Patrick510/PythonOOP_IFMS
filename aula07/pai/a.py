from .filho.b import B
from .filho.neto.c import C

from filho.b import nome_modulo as b_nome_modulo
from filho.neto.c import nome_modulo as c_nome_modulo

A = 10

def nome_modulo():
    print("dentro de", __name__)

if __name__ == 'main':
    print(A,B,C)
    nome_modulo()
    b_nome_modulo()
    c_nome_modulo()