# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

n = 0
for n in range(10):
  n = int(input('Digite: '))
  if n % 2 == 0:
    print(f'{n} é par!')
  else:
    print(f'{n} é impar')
