




s = 0
m  = 0
for i in range(1, 6):
  n = float(input('Nota: '))
  s += n
  m = s / i
  
if m >= 6:
  print(f'{m} Aprovado!')
else:
  print(f'{m} Reprovado.')