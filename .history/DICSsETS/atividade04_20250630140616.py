jovem = 0
adulta = 0
idosa = 0
s_j = 0
s_a = 0
s_i = 0
mj = 0
ma = 0
mi = 0
c = 0
md = 0

for i in range(9):
  n = float(input('Digite a sua idade: '))
  soma += n
  c += 1
  md = soma / c

if md > 0 and md <= 25:
  print(f'Média da turma é {md}')
  print('Turma jovem')
elif md > 25 and md <= 60:
  print(f'Média da turma é {md}')
  print('Turma adulta')
elif md > 60:
  print(f'Média da turma é {md}')
  print('Turma idosa')
  

  mj = s_j / jovem
  ma = s_a / adulta
  mi = s_i / idosa

