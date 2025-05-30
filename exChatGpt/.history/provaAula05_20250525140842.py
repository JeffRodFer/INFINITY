# PROVA AULA 05 Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

c = 0
md = 0
nt = 0
a1 = 'aluno'
print('--- Escola municipal ---')
while a1 != '':
  a1 = input('Digite o nome do aluno: ')
  if a1 == '':
    print('Para iniciar, insira nome do aluno.')

  while c < 3:
    c += 1
    nt = float(input('Nota: '))
    if nt < 0:
      break
    nt += nt  

  md = nt / c

if md >= 6.5:
  print(f'Aluno {a1}, Média: {md:.2f} aprovado!')
  print(c)
else:
  print(f'Aluno: {a1} Média: {md:.2f} Reprovado.')
  print(3)
