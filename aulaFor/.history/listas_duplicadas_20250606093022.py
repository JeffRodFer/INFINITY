lista = ['Jeff', 30, 1.77, ['Rod', 132, 6], 1.77, 'Jeff']
lista2 = []
lista3 = [12, 15, 13, 10]
lista4 = ['Jeff', ' Rod', ' Ferr']

for i in lista:
  if i in lista2:
    continue
  lista2.append(i)# Adiciona iterns a lista

print('Lista 1: ', lista)
print(len(lista))# tamanho da lista

print('Lista 2: ', lista2)
print(len(lista2))

print('Lista 3: ', lista3)
print(sum(lista3))# Soma a lista
print(max(lista3))# Maior numero da lista
print(min(lista3))# Menor numero da lista

print(lista[3])