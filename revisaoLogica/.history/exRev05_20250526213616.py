# 5 - Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

print('------------------ School -------------------')
c = 0
n = 0
md = 0
s = 0
alu = input('Nome do aluno: ')
while c < 3:
  n = float(input('Digite a nota: '))
  if n < 0:
    print('Nota invalida. Reinicie o processo')
    break
  else:
    c += 1
    s += n
    md = s / c

if md <= 6.5:
  print(f'Média {md} reprovado.')
else:
  print(f'Média {md} Aprovado!')