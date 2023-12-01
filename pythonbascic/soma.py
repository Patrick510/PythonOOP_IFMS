n = int(input("Digite um numero: "))
i = 1
soma = 0 

while i <= n:
  if i % 2 == 0: # Se o contador for impar apenas conte +1 no contador
    soma = soma + i # Soma o valor par
    print(f"Valor {i} é par e entra na soma")
  i = i+1


print(f"Soma é {soma}")