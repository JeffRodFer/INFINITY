lista = [12, 15, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
lista2 = []
lista3 = []

for i in lista:
  if i % 2 != 0:
    continue
  lista2.append(i)
  
  if i in lista2:

  print(i)