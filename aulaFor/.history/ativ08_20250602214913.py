# Atividade 08:
# Cálculo de Média de Notas:
# Escreva um programa que solicite 5 notas de alunos. Use um laço for
# para somar as notas e uma condicional para exibir a média e a
# classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).

s = 0
m  = 0
for i in range(1, 6):
  n = float(input('Nota: '))
  s += n
  m = s / i

print(m)