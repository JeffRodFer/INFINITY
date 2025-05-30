# 2 - Somatório de números: Peça ao usuário para inserir números inteiros um de cada vez. O programa deve continuar
# pedindo números até que o usuário digite zero. Ao final, exiba a soma de todos os números inseridos (excluindo o zero).
s  = 0
n = -1
while n != 0:
  n = int(input('Digite um numero: '))
  s = n + n
  print(f'Soma dos número: {n}')

