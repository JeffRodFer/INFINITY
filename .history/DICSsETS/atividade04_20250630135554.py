jovem = 0
adulta = 0
idosa = 0
s_j = 0
s_a = 0
s_i = 0

for i in range(9):
  n = int(input('Digite a sua idade: '))
  if n > 0 and n <= 25:
    jovem += 1
    s_j += n
  elif n > 25 and 