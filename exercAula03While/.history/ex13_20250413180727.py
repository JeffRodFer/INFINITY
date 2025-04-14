numSecreto = 6
tentativas = 3
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
  
  palpite2=
  palpite2 += 1
  if palpite2 == numSecreto:
    print('Player 2 venceu!')
    break
  else:
    print('Player 2 perdeu')
else:
  print('Ninguem acertou o numero')
  