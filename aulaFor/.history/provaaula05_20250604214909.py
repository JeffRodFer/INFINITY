# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.




s = 0
md_al = 0
md_trm = 0
al = 0

n = int(input('Quantos alunos: '))
for j in range(1, n + 1):
  al = input('Nome: ')
  n1 = float(input('Nota: '))
  n2 = float(input('Nota: '))
  n3 = float(input('Nota: '))
  
  md_al = (n1 + n2 + n3) / 3
  md_trm = += md_al

  print(f'{al}: {n1}, {n2}, {n3}')
  print(f'Média: {md_al:.2f}')


  
  if m >= 7:
    print(f'{al} - Media: {m:.2f} Aprovado!')
  else:
    print(f'{a} - Media: {m:.2f} Reprovado.')
    