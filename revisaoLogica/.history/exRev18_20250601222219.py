# 18 - Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login.
# O programa deve solicitar o nome de usuário e senha até que o
# usuário insira as credenciais corretas ou até que o número máximo
# de tentativas seja atingido. Use um laço while com uma condicional
# para verificar as credenciais e limitar as tentativas.

c = 0
login = input('Persona: ')
senha = int(input('Cadastre o código: '))

while c < 3:
  user = input('Usuário: ')
  ki = int(input('Digite a senha: '))
  c += 1
    if login == user and senha == ki:
      print('User OK!')
      print('Key OK!')
      print('Welcome to OS!')
      break
    else:
      print('Usuário ou senha incorretos. Tente novamente.')  