n = 0
p = 0
c  = 0
senha = '1234'
while c <= 4:
  c += 1
  n = input('Tente a senha: ')
  if n == senha:
    print('Senha correta.')
    break
  else:
    print('Sem tentativas!')

print('Segue o baile!!')

