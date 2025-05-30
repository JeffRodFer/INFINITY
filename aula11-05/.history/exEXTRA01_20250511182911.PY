senha = '1234'
c = 0
s =0
while s != senha:
  s = input('Digite a senha: ')
  if s == senha:
    c += 1
    print('Bem vindo ao sistema!')
    break
  elif c == 3:
    print('Fim das tentativas!')
  else:
    print('Tente novamente!')
    
