acesso = 5
senha = 'Admin123'
print('Digite usúario e senha para entrar: ')
num = print(int(input('Insira um usuario:')))
# chave = print(input('Insira a senha:'))
if num == acesso:
  print('Benvido ao sistema.')
else:
  print('Usúario sem acesso!')