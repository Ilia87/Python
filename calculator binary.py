base = int(input('выберите систему исчисления от 2 до 10: '))
x = y = int(input(f'десятечное число для перевода в {base}-ую систему: '))
while x > 0:
    digit = x % base
    # print(digit, end=' ')
    x //= base
print(f'число ' + str(y) + ' в ' + str(base) + '-ой системе = ' + str(digit))

print(f'справочно, число {y} в \n2-ой: ' + str(bin(y)) + ', \n8-ой: ' + str(oct(y)),
      ', \n16-ой: ' + str(hex(y)))
