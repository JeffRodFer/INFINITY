numSecreto = 6
tentativas = 3
palpite = 0
palpite2 
player1 = 0
player2 = 0
while player1 < tentativas and player2 < tentativas:
  palpite = int(input("Player 1, tente um numero: "))
  player1 += 1
  if palpite == numSecreto:
    print('Player 1 acertou')
    break
  else:
    print('Player 1 perdeu')
  
  palpite2 = int(input('Player 2, tente um numero: '))
  palpite2 += 1
  if palpite2 == numSecreto:
    print('Player 2 venceu!')
    break
  else:
    print('Player 2 perdeu')
else:
  print('Ninguem acertou o numero')
  