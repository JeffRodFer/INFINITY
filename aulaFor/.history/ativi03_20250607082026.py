lista = [12, 15, 13, 10, 12, 13, 12, 15, 10, 9, 5, 18]
lista2 = []
lista3 = []

for i in lista:
  if i % 2 != 0:
    continue
  lista2.append(i)
  
for i in lista2:
 if i in lista3:
   continue
 lista3.append(i)

 print(i)
 print(lista