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
  print('f{imc} abaixo do peso')
elif imc > 18.5 and imc <= 24.9:
  print(f'')