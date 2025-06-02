# 18 - Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login.
# O programa deve solicitar o nome de usuário e senha até que o
# usuário insira as credenciais corretas ou até que o número máximo
# de tentativas seja atingido. Use um laço while com uma condicional
# para verificar as credenciais e limitar as tentativas.


login = input('Persona: ')
senha = input('Cadastre o código: ')

while True:
  while c <= 3:
    c += c
    user = input('Usuário: ')
    if login == user:
      # print(f'{user}')
      ki = input('Digite a senha: ')
      if senha == ki:
        print('User OK!')
      print('Key OK!')
        print('Welcome to OS!')
        break
      else:
        print('Wrong key')  