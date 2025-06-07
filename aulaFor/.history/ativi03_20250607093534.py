lista = [3, 9, 5, 4, 2, 6]
lista2 = []
lista3 = []
lista4 = []

for i in lista:
  if i % 2 == 0:
    continue
  lista2.append(i)
for i in lista:
  if i % 2 != 0:
    continue
  lista3.append(i)

print('Lista original: ', lista)
print('',lista2)
print(sorted(lista3))
#  print(sorted(lista4))
