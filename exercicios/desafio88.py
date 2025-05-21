from random import randint
from time import sleep
print('-'*40)
print(' '*10, 'JOGA NA MEGA SENA')
print('-'*40)
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTEANDO {vezes} JOGOS ', '-='*5)
jogo = []
for j in range(1,vezes+1):
    sleep(1)
    print(f'Jogo {j}: ', end='')
    for n in range(0,6):
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
    print(f'{jogo}')
    jogo.clear()
print('-='*5, '< BOA SORTE! >', '-='*5)
