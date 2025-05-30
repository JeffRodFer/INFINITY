opcao = ''
while opcao != 'sair':
  print('Menu:')
  print('1 - Textos: ')
  print('2 - Calculos: ')
  print('3 - Docs: ')
  print('4 - Sair: ')
  opcao = input('Digite a opção: ')
  if opcao == '1':
    print('Gramática e Redação.')
  elif opcao == 2:
    print('Raizes e expressões.')
  elif opcao == 3:
    print('Arquivos.')
  elif opcao == 4:
    print('Encerrado.')
    break
  else:
    print('Opção inválida, tente novamente!')
