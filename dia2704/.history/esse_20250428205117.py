acesso = '12qw'
chance = ''

while chance != acesso:
  chance = input('Digite a chave: ')
  if chance == acesso:
    while cont <= 3:
      cont += 1
      print()
    print('---- Seja bem-vindo!! ----')
    break
  else:
    print('Errou, tente novamente!')