

lista = [12, 15, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
for i in lista:
  if i in lista2:
    continue
  lista2.append(i)

print(lista)
print(lista2)
