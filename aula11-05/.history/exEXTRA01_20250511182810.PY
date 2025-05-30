senha = '1234'
c = 0
s =0
while s != senha:
  s = input('Digite a senha: ')
  if s == senha:
    print('Bem vindo ao sistema!')
    c += 1
    break
  elif c == 3:
    print('Fim das tentativas!')
  else:
    print('Tente ')
    break
