# jovem = 0
# adulta = 0
# idosa = 0
# s_j = 0
# s_a = 0
# s_i = 0
# mj = 0
# ma = 0
# mi = 0
c = 0
md = 0
soma = 0

for i in range(9):
  n = float(input('Digite a sua idade: '))
  soma += n
  c += 1
  md = soma / c

if md > 0 and md <= 25:
  print('Turma jovem')
  print(f'Média da turma é {md:.2f}')
elif md > 25 and md <= 60:
  print('Turma adulta')
  print(f'Média da turma é {md:.2f}')
elif md > 60:
  print('Turma idosa')
  print(f'Média da turma é {md:.2f}')
  
