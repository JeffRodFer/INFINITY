# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,"Reprovado" para média < 6).
sn = 0
n = 0
for i in range(3):
  n = float(input('Digite a nota: '))
  i += 1
  sn += n
  m = sn / i

if m >= 6:
  print(f'Média {m:.2f}: Aprovado!')
else:
  print('Reprovado!')