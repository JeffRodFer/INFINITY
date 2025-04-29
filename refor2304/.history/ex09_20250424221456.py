num_sec = 7
palpite = None

while palpite != num_sec:
  palpite = input('Insira senha: ')
  if palpite == num_sec:
    print('Acertou!!')
      break
    else:
      print('Errou! Reinicie')