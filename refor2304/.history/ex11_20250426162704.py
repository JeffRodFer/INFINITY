# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.
print('------ Acerte o numero de entrada ------')
num = ''
while num != '12':
  v = input('Digite um valor de 10 a 15: ')
  if v == '7':
    print(f'Acesso Liberado!')
    break
  elif  v <= 9:
    print('O numero deve ser maior.')
  elif v >= 16:
    print('O valor deve ser menor.')
  else:
    print('Tente novamente!')