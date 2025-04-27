acesso = 5
senha = 'Admin123'
print('Digite usúario e senha para entrar: ')
num = printint(input('Insira um u´suario:'))
# chave = print(input('Insira a senha:'))
if num == acesso:
  print('Benvido ao sistema.')
else:
  print('Usúario sem acesso!')