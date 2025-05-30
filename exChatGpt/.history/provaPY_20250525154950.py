# PROVA 
# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada 
# aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi 
# aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome 
# do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.

print('--------- School ---------')

al = 0
nt = 0
md = 0

q = int(input('Insira a quantidade de alunos: '))

while c < 3:
  al = input('Nome: ') # Nome
  c += 1
  for i in range(0, q): # Para notas
    nt = float(input('Nota:'))
