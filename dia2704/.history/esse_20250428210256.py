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
    cont += 1
     cont <= 3:
      print('Chances esgotadas, tente após 2min.')
      break
      