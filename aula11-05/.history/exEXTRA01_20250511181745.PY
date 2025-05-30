senha = '1234'
c = 0

s = int(input('Digite a senha: '))
while s != senha:
  if s == senha:
    print('Bem vindo ao sistema!')
    break
  else:
    print('Errou! Tente novamente.')