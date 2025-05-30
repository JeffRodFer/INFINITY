n = 0
p = 0
c  = 0
senha = '1234'
print('3 tentativas ')
while c <= 4:
  c += 1
  n = input('Tente a senha: ')
  print(' ')
  if n == senha:
    print('Senha correta.')
    print(' ')
    break
  elif c == 4:
    print('Sem tentativas!')
    break

print('Segue o baile!!')

