senha = ''
n = 0
while n != '1234':
  n = int(input('Digite a senha: '))
  if n == 1234:
    print('Acesso liberado')
    
  else:
    print('Senha incorreta, tente novamente!')
