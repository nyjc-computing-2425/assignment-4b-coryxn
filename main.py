stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

if stdform.count('x10^') == 1:
  pos = stdform.find('x10^')
  mantissa = stdform[0:pos]
  exponent = stdform[pos+4:]
elif stdform.count('E') == 1:
  pos = stdform.find('E')
  mantissa = stdform[0:pos]
  exponent = stdform[pos+1:]
else: 
  print('Error converting to scientific E notation.')

list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'E', 'x', '.', '-', '^']
if not all(item in list for item in stdform) or not stdform.count('.') <= 1 or not stdform.count('x') <= 1 or not stdform.count('^') <= 1 or not exponent.count('.') == 0:
  print('Error converting to scientific E notation.')
else: 
  if stdform.count('x10^') == 1:
    stdform = stdform.replace('x10^', 'E')
  elif stdform.count('E') == 1:
    stdform = stdform.replace('E', 'x10^')
print(f'This number in E notation is {stdform}.' )