# 4 - Cálculo de Juros Simples:
# Crie um programa que calcule o valor futuro de um investimento
# usando a fórmula de juros simples. Peça ao usuário para digitar o
# capital inicial, a taxa de juros e o tempo de aplicação.
# j = (c * i * t) / 100


print('--------------- CALCULO DE JUROS SIMPLES ------------------')
j = 0
vf = 0
vi = float(input('Digite o valor inicial: R$'))
tx = float(input('Digite a taxa: '))
tempo = float(input('Meses de investimento: '))

j = (vi * tx * tempo) / 100
vf = j + vi

print(f'{vf}')