# 5- Adivinhar Número:
# Desenvolva um jogo de adivinhação onde o
# programa escolhe um número aleatório entre 1 e
# 100. O usuário deve tentar adivinhar o número, e
# o programa deve fornecer dicas se o palpite está
# muito alto ou baixo.

s = 30
n = 0

while n != s:
  if n <= 10 and n >= 50:
    print('Esta friuu')
  elif n <= 20 and n >= 40:
    print('Tá morno')
  elif n >= 25 and n <= 35:
    print('Pegando fogo')

  print(n)  
