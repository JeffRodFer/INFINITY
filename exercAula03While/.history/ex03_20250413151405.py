cont = 0
multi = 0
num = int (input("Enter a number: "))


while cont < 10:
  cont += 1
  multi = num * cont
if multi % 3 == 0:
   print(f'{num} x {cont} = {multi}')
