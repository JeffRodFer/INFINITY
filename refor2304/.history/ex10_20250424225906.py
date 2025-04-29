n = 0
cont = 0
while n <= 10:
  n = int(input('Digite um numero: '))
  if n <= 10:
    cont += 1
    n += n
  else:
    print(n)