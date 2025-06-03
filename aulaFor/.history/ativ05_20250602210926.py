# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

n = 0
pos = 0
neg = 0
for i in range(10):
  n = int(input('Digite o numero: '))
  if n > 0:
    pos += 1
  else:
    neg += 1

print(f'Positivos {pos}')
print(f'Negisivos {neg}')