
# MINHA RESOLUÇÃO
from math import factorial

num = int(input('De qual número você deseja o fatorial: '))
print(f'{num}! = ', end=' ')
for c in range(num, 1, -1):
    print(f'{c} x ', end='')
print('1', end='')
print(f' = {factorial(num)}')

# PRIMEIRA FORMA COM O PROFESSOR
# from math import factorial
# n = int(input('De qual número você deseja o fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}.')

# SEGUNDA FORMA
# n = int(input('De qual número você deseja o fatorial: '))
# c = n
# f = 1
# print(f'Calculando {n}! = ', end='')
# while c > 0:
#     print(f'{c}', end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print(f'{f}')
