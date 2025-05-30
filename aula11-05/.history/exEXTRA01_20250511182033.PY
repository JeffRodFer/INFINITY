senha = '1234'
c = 0
s =0
while s != senha:
  s = input('Digite a senha: ')
  if s == senha:
    print('Bem vindo ao sistema!')
    break
  else:
    print('Errou! Tente novamente.')
    
    c += 1