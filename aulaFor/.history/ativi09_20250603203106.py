# Atividade 09:
# Verificar Números Pares e Impares com Interrupção:
# Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.
n = int(inpu)
for i in range(-1, 20):
  if i == 0:
    continue
  if i == n:
    break
  if i % 2 == 0:
    print(f'{i} par.')
  if i % 3 == 0:
    print(f'{i} é impar.')