# https://youtu.be/b8m9uRMpKJk
# 60 minute
base: int = int(input('выберите систему исчисления от 2 до 10: '))
x = y = int(input(f'десятечное число для перевода в {base}-ую систему: '))
while x > 0:
    digit = x % base
    str(print(digit, end=''))
    x //= base
print(f'число ' + str(y) + ' в ' + str(base) + '-ой системе = ' + str(x))

print(f'справочно, число {y} в '
      f'\n2-ой: {str(bin(y))}, '
      f'\n8-ой: {str(oct(y))}, '
      f'\n16-ой: {str(hex(y))}')
