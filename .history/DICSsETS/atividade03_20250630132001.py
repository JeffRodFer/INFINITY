par = 0
impar = 0
for i in range(0,9):
  n = int(input)
  if i % 2 == 0:
    par += 1
  elif i % 3 == 0:
    impar += 1

print(f'Pares: {par}')
print(f'Impares: {impar}')