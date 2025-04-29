print('------------ IMC -------------')
print('Entre 18.5 e 24.99 = Peso Normal')
print('Entre 25.00 e 29.99 = Sobrepeso I')
print('Entre 30.00 e 39.99 = Obesidade II')
print('Acima de 40.00 = Obesidade Grave III')
nome = input('Insira o seu nome: ')
peso = float(input('Insira o seu peso: '))
alt = float(input('Insira a sua altura: '))
imc = peso / (alt*2)

if imc <= 18.49:
  print(f'Abaixo do peso!')
elif imc >= 18.50 and imc <= 29.99:
  print(f'IMC {imc:.2f} Peso normal')
elif imc >= 25.00 and imc <= 29.99:
  print(f'IMC {imc:.2f} Sobrepeso I')
elif imc >= 30.00 and imc <= 39.99:
  print(f'IMC {imc:.2f} Sobrepeso II')
else:
  print(f'IMC {imc:.2f} Obesidade Grave III')