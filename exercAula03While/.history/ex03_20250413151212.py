cont = 0
multi = 0
num = int (input("Enter a number: "))


while cont < 10:
  cont += 1
  multi = num * cont
  print(f'{num} x {cont} = {multi}')
  if multi % 3 == 0:
    print(f'{multi} is a multiple of 3')
  else:
    print(f'{multi} is not a multiple of 3')