i = int(input(''))
if (i%4):
 print(' a normal year')
else:
 if (i%100):
  print('a leap year')
 else:
  if (i%400):
    print('a normal year')
  else:
    print('a leap year')
