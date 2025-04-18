# from random import choice

# lista = [0, 1, 2, 3, 4, 5]
# n = choice(lista)

# escolha = int(input('Tente adivinhar o número de 0 até 5: '))

# if escolha == n:
#     print('Você acertou o número. GANHOU!!')
# else:
#     print(f'Você errou, o número certo era {n}. PERDEU!!')

from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 10)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if player == comp:
     print('Você acertou o número. GANHOU!!')
else:
    print(f'Você errou, o número certo era {comp}. PERDEU!!')