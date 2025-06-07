lista = [ 9, 5, 4, 2, 6]
lista2 = []
lista3 = []
lista4 = []

for i in lista:
  for i in lista2:
   if i % 2 != 0:
     continue
   lista2.append(i)

# for i in lista2:
#  if i in lista3:
#    continue
#  lista3.append(i)

# #  for i in lista:
#   if i % 2 != 0:
#     continue
#   lista4.append(i)

print(sorted(lista))
print(sorted(lista2))
#  print(sorted(lista3))
#  print(sorted(lista4))
