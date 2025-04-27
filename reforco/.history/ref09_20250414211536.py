print('Digite usúario e senha para entrar: ')
num = print(int(input('Insira um usúario:')))
# senha = 'Admin123'
chave = int(print(input('Insira a senha:')))
if num >= chave:
  print('Benvido ao sistema.')
else:
  print('Usúario sem acesso!')