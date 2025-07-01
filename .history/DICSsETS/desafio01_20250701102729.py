# Gerenciamento de Compras de Produtos
# Você foi contratado para desenvolver um programa simples para
# auxiliar em um processo de compra de produtos. O programa deve
# permitir ao usuário inserir o nome e o preço de vários produtos,
# perguntando se deseja continuar inserindo mais produtos após cada
# entrada. Ao final, o programa deve fornecer um resumo da compra,
# incluindo:
# A- O total gasto na compra.
# B- A quantidade de produtos que custam mais de R$1000.
# C- O nome do produto mais barato.
# Desenvolva o programa em Python utilizando conceitos de
# entrada/saída de dados, condicionais e laços de repetição.

produtos = {}
print('--' * 10)
while True:
  print('Digite 1 para cadastrar e 0 para encerrar: ')
  opcao = int(input('Digite a opção: '))

  if opcao == 0 or opcao > 1:
    print('Opção inválida')
    break
  elif opcao == 1:
    nome_prod = input('Produto: ')
    preco_prod = float(input('Preço: '))
    produtod[nome_prod] = preco

  for nome, preco in produtos.itens():
    print(f'Produto: {nome_prod}: - Preço: {preco_prod:.}')
