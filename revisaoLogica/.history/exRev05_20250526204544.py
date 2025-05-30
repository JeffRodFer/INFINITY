# 5 - Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6).

print('------------------ School -------------------')
c = 0
n = 0
md = 0
alu = input('Nome do aluno: ')
while c < 4:
  n = float(input('Digite a nota: '))
  c += 