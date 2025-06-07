lista = ['Jeff', 30, 1.77, 'Rod', 30, 1.77, 'Jeff']
lista2 = []
lista3 = [12, 15, 13, 10]

for i in lista:
  if i in lista2:
    continue
  lista2.append(i)

print(lista)
print(len(lista))
print(sum('Lista 3: ', lista3))

print(lista2)
print(len(lista2))