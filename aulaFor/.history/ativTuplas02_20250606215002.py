lista = [12, 15, 7, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
lista2 = []


for i in lista:
  if i in lista2:
    continue
  lista2.append(i)
  
print(''lista2[::-1])
print(lista2)