# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.
num = int(input("Enter a number between 1 and 10: "))
while num > 1 and num < 10:
   print("Valid number!")
 if num < 1 or num > 10:
print("Invalid number!") else:
