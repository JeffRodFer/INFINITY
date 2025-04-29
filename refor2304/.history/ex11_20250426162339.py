# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.
print('------ Acerte o numero de entrada ------')
num = ''
while num != '7':
  v = input('Digite a chave: ')
  if v == '7':
    print(f'Acesso Liberado!')
    break
  else:
    print('Tente novamente!')