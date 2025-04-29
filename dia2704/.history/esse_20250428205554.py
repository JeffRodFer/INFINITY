acesso = '12qw'
chance = ''
cont = 0

while chance != acesso:
  chance = input('Digite a chave: ')
  while cont <= 3:
      cont += 1
      if chance == acesso:
        print('Chances esgotadas, tente após 2min.')
        break
        print('---- Seja bem-vindo!! ----')
  break
      else:
        print('Errou, tente novamente!')