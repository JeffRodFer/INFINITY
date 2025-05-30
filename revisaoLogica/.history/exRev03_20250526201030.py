# 3 - Cálculo de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC).
# Peça ao usuário para digitar seu peso e altura, armazene em
# variáveis e calcule o IMC.

print('------------- IMC --------------')

imc = 0
p = float(input('Digite o seu peso: '))
a = float(input('Digite a altura: '))

imc = p / (a * a)

if imc < 18.5:
  print('f{imc} Abaixo do peso.')
elif imc > 18.5 and imc <= 24.9:
  print(f'{imc} Peso normal.')
elif imc >= 25 and imc <= 29.9:
  print(f'{imc} Acima do peso.')
elif imc >= 30 and imc <= 34.9:
  print(f'')