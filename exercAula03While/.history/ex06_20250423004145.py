# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
cont = 1
num = 0
while num != 10:
    num = int(input("Enter a number: "))
    print(f'Chance {cont}')
    cont = cont + 1
    if cont == 3:
    print('perdeu')
        #cont = cont + 1
    #print(f'Chance {cont}')
print(f'Acertou {num}!')