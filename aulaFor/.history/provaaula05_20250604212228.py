# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.




s = 0
m  = 0
a = 0

n = int(input('Quantos alunos: '))
for j in range(n):
  a = input('Nome: ')
  m = 0
  for i in range(1, 3):
    n = float(input('Nota: '))
    s += n
    m = s / i
  
  if m >= 6:
    print(f'{a} - Media: {m:.2f} Aprovado!')
    m = 0
  else:
    print(f'{a} - Media: {m:.2f} Reprovado.')
    
    m = 0