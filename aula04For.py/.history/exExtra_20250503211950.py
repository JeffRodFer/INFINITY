# n = 0
# c = 0
# for i in range(5):
#   n = int(input('Digite um numero: '))
#   if n % 2 == 0:
#     print(f'Numero par encontrado: {n}, laço interrompido.')
#     break
#   else:
#     print(f'Numero impar, segue o laço.')
# else:
#   print('Apenas impares.')
opcao = 0
while True:
  print('Menu:')
  print('1- Contar de 1 até 5.')
  print('2- Sair')
  opcao = int(input('Digite a sua opção: '))
  if opcao == 1:
    for i in range(5):
      print(i)
      si += 1
  elif opcao == 2:
    print('SAIR')
    break
  else:
    print('Opção inválida, tente novamente!')
print()