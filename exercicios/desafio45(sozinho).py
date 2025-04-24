from random import choice

comp = [0, 1, 2]
jcom = choice(comp)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jpla = int(input('Qual sua jogada? '))

if jpla == jcom:
    if jpla == 0:
        print('-=' * 10)
        print('Computador jogou Pedra')
        print('Jogador jogou Pedra')
        print('-=' * 10)
        print('EMPATE')
    elif jpla == 1:
        print('-=' * 10)
        print('Computador jogou Papel')
        print('Jogador jogou Papel')
        print('-=' * 10)
        print('EMPATE')
    elif jpla == 2:
        print('-=' * 10)
        print('Computador jogou Tesoura')
        print('Jogador jogou Tesoura')
        print('-=' * 10)
        print('EMPATE')

if jpla == 0 and jcom == 1:
    print('-=' * 10)
    print('Computador jogou Papel')
    print('Jogador jogou Pedra')
    print('-=' * 10)
    print('JOGADOR PERDEU')

if jpla == 0 and jcom == 2:
    print('-=' * 10)
    print('Computador jogou Tesoura')
    print('Jogador jogou Pedra')
    print('-=' * 10)
    print('JOGADOR GANHOU')

if jpla == 1 and jcom == 0:
    print('-=' * 10)
    print('Computador jogou Pedra')
    print('Jogador jogou Papel')
    print('-=' * 10)
    print('JOGADOR GANHOU')

if jpla == 1 and jcom == 2:
    print('-=' * 10)
    print('Computador jogou Tesoura')
    print('Jogador jogou Papel')
    print('-=' * 10)
    print('JOGADOR PERDEU')

if jpla == 2 and jcom == 0:
    print('-=' * 10)
    print('Computador jogou Pedra')
    print('Jogador jogou Tesoura')
    print('-=' * 10)
    print('JOGADOR PERDEU')

if jpla == 2 and jcom == 1:
    print('-=' * 10)
    print('Computador jogou Papel')
    print('Jogador jogou Tesoura')
    print('-=' * 10)
    print('JOGADOR GANHOU')
