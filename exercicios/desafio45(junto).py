from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')
sleep(1)

print(f'Computador jogou {itens[comp]}')
print(f'Jodador jogou {itens[jogador]}')

if comp == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else: 
        print('Jogada inválida')

elif comp == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else: 
        print('Jogada inválida')

elif comp == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else: 
        print('Jogada inválida')