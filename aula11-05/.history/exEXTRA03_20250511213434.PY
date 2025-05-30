n = 0
p = 0
c  = 0
senha = '1234'
while c <= 2:
  n = input('Tente a senha: ')
  c += 1
if n == senha:
  print('Senha correta.')
    breakpoint
else:
  print('Sem tentativas!.')

