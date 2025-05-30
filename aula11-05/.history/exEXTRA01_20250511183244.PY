senha = '1234'
c = 0
s =0
while s != senha:
  s = input('Digite a senha: ')
  if s == senha:
    print('Bem vindo ao sistema!')
    break
  elif c == 2:
    print('Fim das tentativas!')
    print('-------------------')
    break
  else:
    print('Tente novamente!')
    c += 1
