# 12 - Sistema de Login:
# Desenvolva um programa que simule um sistema de login.
# O programa deve pedir o nome de usuário e a senha e verificar
# se correspondem a um usuário pré-cadastrado. Exiba mensagens
# apropriadas para login bem-sucedido ou falha.

login = input('Persona: ')
senha = input('Cadastre o código: ')

while True:
  user = input('Usuário: ')
  if login == user:
    print()

  ki = input('Digite a senha: ')
  if senha == ki:
    print('User OK!')
    print('Welcome to OS!')
    break
  else:
    print('Wrong key')
  

    