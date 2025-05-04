# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6,"Reprovado" para média < 6).
m = 0
n = 0
for n in range(6):
  n = float(input('Digite a nota: '))
  m += n
  if m >= 6:
    print(f'Média {m}:')