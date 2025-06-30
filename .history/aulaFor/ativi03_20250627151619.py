lista = [3, 9, 5, 4, 2, 6]
lista2 = []
lista3 = []

for i in lista:
  if i % 2 == 0:
    continue
  lista2.append(i)
for i in lista:
  if i % 2 != 0:
    continue
  lista3.append(i)

print('Lista original: ', lista)
print('Lista impar: ', lista2)
print('Lista par ordenada: ', (sorted(lista3)))
print('Lista par ordenada: ', (sorted(lista2)))