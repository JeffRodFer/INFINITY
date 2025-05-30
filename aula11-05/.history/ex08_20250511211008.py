# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.
c = 0
n = 0
m = 0
s = 0
while n >= 0:
  n = float(input('Insira a nota: '))
  if n >= 0:
    n + n
    c += 1
    m = n / c

print(f'A média das notas é {m:.2f}')