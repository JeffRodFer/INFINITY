# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
cont = 0
num = 10
while cha != num:
    num = int(input("Enter a number: "))
    print(f'Chance {cont}')
    cont = cont + 1
    if cont == 3:
        print('perdeu!!')
        break

print(f'Acertou {num}!')