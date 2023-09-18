n1 = int(input('insira o codigo \n'))

if n1 == 1:
    print('alimento n perecivel1')
elif n1 >= 2:
    if n1 <= 4:
      print('alimento perecivel')
    elif n1 >= 5:
       if n1 <= 6:
        print('vestuario')
       elif n1 == 7:
        print('higiene pessoal')
       elif n1 >= 8:
        if n1 <= 15:
          print('limpeza e utencilios')
        else:
          print('invalido')