acesso = '12qw'
chance = ''
cont = 0

while chance != acesso:
  chance = input('Digite a chave: ')
  if chance == acesso:
    print('---- Seja bem-vindo!! ----')
    break
  else:
    print('Errou, tente novamente!')
   