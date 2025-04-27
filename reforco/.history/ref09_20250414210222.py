acesso = 'admin'
senha = 'Admin123'
print('Digite a senha para entrar: ')
nome = print(input('Insira um u´suario:'))
chave = print(input('Insira a senha:'))
if nome == acesso and chave == senha:
  print('Benvido ao sistema.')
else:
  print('Usúario sem acesso!')