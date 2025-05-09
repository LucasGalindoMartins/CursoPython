from random import randint

valores = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print('O valores sorteados foram: ', end='')
for n in valores:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O maior valor sorteado foi {min(valores)}')
