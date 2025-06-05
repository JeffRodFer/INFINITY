
# Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes


user = 'abre'
ki = '1234'
for i in range(3, 0, -1):
  usuario = input('Insira o usuario: ')
  senha = input('Digite a senha: ')

  if usuario == user and senha == ki:
    print('Acesso liberado!')
  else:
    print('Acesso negado. t')