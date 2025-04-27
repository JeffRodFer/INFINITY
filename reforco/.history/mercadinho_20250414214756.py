# mode 1 = 15% desconto
# mode 2 = 5% desconto
# mode 3 = R$ 15,00 desconto

print('----- Analise de clientes -----')
cliente = input('Digite o seu nome: ')
mode = int(print('Digite seu modelo: '))
# preco = float(input('Preço do produto'))
if mode == 1:
  print(f'O cliente {cl} com 15% de desconto.')
elif mode == 2:
