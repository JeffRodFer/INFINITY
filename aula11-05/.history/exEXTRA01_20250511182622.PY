senha = '1234'
c = 0
s =0
while s != senha:
  s = input('Digite a senha: ')
  if s == senha:
    print('Bem vindo ao sistema!')
    break
  elif c != 
    print('Errou! Tente novamente.')
    if c != 3:
      c += 1
    print('Fim das tentativas!')
    break
