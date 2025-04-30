# 5- Adivinhar Número:
# Desenvolva um jogo de adivinhação onde o
# programa escolhe um número aleatório entre 1 e
# 100. O usuário deve tentar adivinhar o número, e
# o programa deve fornecer dicas se o palpite está
# muito alto ou baixo.

s = 30
n = 0

while n != s:
  n = int(input('Digite um numero: '))
  if n <= 10 or n >= 50:
    print('Esta friuu')
  elif n <= 20 or n >= 40:
    print('Tá morno')
  elif n >= 25 or n <= 35:
    print('Pegando fogo')

print(f'{n}')  
