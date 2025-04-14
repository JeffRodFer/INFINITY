# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.
cont = 0
soma = 0
media = 0
n1 = 0
while n1 != -1:
  n1 = float(input("Enter the note: "))
  cont += 1
  if n1 != -1:
    soma += n1
    media = soma / cont
print(f'The average is:)