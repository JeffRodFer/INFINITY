# mode 1 = 15% desconto
# mode 2 = 5% desconto
# mode 3 = R$ 15,00 desconto

print('----- Analise de clientes -----')
cliente = input('Digite o seu nome: ')
mode = int(input('Digite o seu modelo de cliente 1, 2 ou 3: '))
# preco = float(input('Preço do produto'))
if mode >= 4:
  print('Cliente ')
if mode == 1:
  print(f'O cliente {cliente} tem o beneficio de 15% de desconto em suas compras.')
elif mode == 2:
  print(f'O cliente {cliente} tem R$15,00 de desconto nas compras.')
else:
  print(f'O cliente {cliente} tem 5% de desconto para negociar os débitos.')
