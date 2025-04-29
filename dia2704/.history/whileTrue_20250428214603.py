
while True:
  print('Menu:  ')
  print('1. Cheguei!')
  print('2. Vamos.')
  print('3. Adeus.')

  opcao = int(input('Escolha uma opção: '))
  if opcao == 1:
    print('Olá!')
    break
  elif opcao == 2:
    print(f'{opcao} Logo')
    break
  elif opcao == 3:
    print(f'{opcao} Muchacho!!')
    break
  print(f'{opcao} Ninguém acertou.')