lista = ['Jeff', 30, 1.77, 'Rod', 30, 1.77, 'Jeff']
lista2 = []
lista3 = [12, 15, 13, 10]
lista4 = ['Jeff', ' Rod', ' Ferr']

for i in lista:
  if i in lista2:
    continue
  lista2.append(i)

print('Lista 1: ', lista)
print(len(lista))

print('Lista 2: ', lista2)
print(len(lista2))

print('Lista 3: ', lista3)
print(sum(lista3))
print(max(lista3))
print(min(lista3))
