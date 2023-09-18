peso = float(input('bota teu peso ae: '))
alt = float(input('bota a altura: '))
sexu = int(input('homi(1) muié(2): '))

imc = int(peso/(alt*alt))

if sexu == 1:
  if imc <= 20.7:
    print('\nHomi seu imc é: ',imc,'\nTa abaixo do peso viu')
  elif imc <= 26.4:
    print('\nHomi seu imc é: ',imc,'\nTa no peso ideal viu')
  elif imc >= 26.5:
    print('\nHomi seu imc é: ',imc,'\nTa acima do peso pae')
else:
  if imc <= 19.1:
    print('\nMuie seu imc é: ',imc,'\nTa abaixo do peso viu')
  elif imc <= 25.8:
    print('\nMuie seu imc é: ',imc,'\nTa no peso ideal viu')
  elif imc >= 25.9:
    print('\nMuie seu imc é: ',imc,'\nTa acima do peso pae')


