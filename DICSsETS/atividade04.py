c = 0
md = 0
soma = 0

for i in range(5):
  n = float(input('Digite a sua idade: '))
  soma += n
  c += 1
  md = soma / c

if md > 0 and md <= 25:
  print('Turma jovem')
  print(f'Média de idade {md:.2f}')
elif md > 25 and md <= 60:
  print('Turma adulta')
  print(f'Média de idade {md:.2f}')
elif md > 60:
  print('Turma idosa')
  print(f'Média de idade {md:.2f}')
  
