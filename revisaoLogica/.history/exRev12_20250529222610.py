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
    print('User OK!')
    ki = input('')
  else:
    print('Wrong user.')

    