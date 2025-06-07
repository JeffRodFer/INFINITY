lista = [12, 15, 7, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
lista2 = []
inv_lista = []


for i in lista:
  if i in lista2:
    continue
  lista2.append(i)
  inv_lista = reversed(lista)
print(lista(inv_lista))
print(lista2)