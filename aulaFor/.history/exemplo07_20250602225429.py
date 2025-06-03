while True:
  print('Menu: ')
  print('1- Contar de 1 a 5: ')
  print('2- Sair: ')
  opcao = input('Escolha uma opção: ')

  if opcao == '1':
    for i in range(3):
      print(i)
    elif opcao == '2':
      print('Sair do programa.')
      