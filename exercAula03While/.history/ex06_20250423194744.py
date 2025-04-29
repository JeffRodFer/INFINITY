# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.
cont = 0
cha = 0
num = 10
while cha != num:
    cha = int(input("Enter a number: "))
    #print('Chance')
    cont = cont + 1
    if cont < 3:
        print('Tente novamente.')
    else:
        print('PERDEU')
    
# print(f'Acertou {cha}!')