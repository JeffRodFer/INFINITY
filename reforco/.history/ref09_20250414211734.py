print('Digite usúario e senha para entrar: ')
num = (int(input('Insira um usúario:')))
chave = int(input('Insira a senha:'))
if num >= chave:
  print('Benvido ao sistema.')
else:
  print('Usúario sem acesso!')