# 1 - Conversão de Unidades:
# Crie um programa que converta metros para centímetros.
# Peça ao usuário para digitar um valor em metros, armazene
# em uma variável e converta para centímetros.
cm = 1

print('------------ Conversão --------------')
m = float(input('Quantidade de metros: '))
m = m * 100
cv = m / cm
print(f'Sua metragem em {cv:.2f}cm.')