# 5- Adivinhar Número:
# Desenvolva um jogo de adivinhação onde o
# programa escolhe um número aleatório entre 1 e
# 100. O usuário deve tentar adivinhar o número, e
# o programa deve fornecer dicas se o palpite está
# muito alto ou baixo.

s = 30
n = int(input('Digite um numero: '))
while n != s:
  if n < 10 and n > 50:
    print('Esta longe')
  elif n < 20 and n > 40
