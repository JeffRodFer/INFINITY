lista = [12, 15, 7, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
lista2 = []


for i in lista:
  if i in lista2:
    continue
  lista2.append(i)

print('Lista original: ', lista)
print('Lista sem repetição ordenada', sorted(lista2))
# lista2.sort(reverse=True)
print('Lista invertida', (lista2.sort(reverse=True)))