# opcao = ''

# while opcao != 'sair':
#   print('Menu 1: ')
#   print('Opção 2: ')
#   print('Opção 3: ')
#   print('Digite sair para encerrar.')
#   opcao = input('Escolha uma opção: ')
#   if opcao == '1':
#     print('Page 1 open')
#   elif opcao == '2':
#     print('Page 2 open')
#   elif opcao == '3':
#     print('Sair')
#   else:
#       print('Erro. Tente uma opção valida!')

num_sec = 7
tentat_totais = 3
jog1_tenta = 0
jog2_tenta = 0
while jog1_tenta < tentat_totais and jog2_tenta < tentat_totais:
  palpite = int(input('Jogador adivinhe o numero: '))
  jog1_tenta += 1
  if palpite == num_sec:
    print(f'{num_sec} Acertou!')
  else:
    print('Errou!')
  
  palpite2 = int(input('Jogador 2 adivinhe o numero: '))
  jog2_tenta 