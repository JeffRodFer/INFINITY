cont = 0
soma = 0

while cont <= 100:
  cont += 1
  soma = soma + cont % 2 == 2
  print(cont)