from random import choice

lista = [0, 1, 2, 3, 4, 5]
n = choice(lista)

escolha = int(input('Tente adivinhar o número de 0 até 5: '))

if escolha == n:
    print('Você acertou o número. GANHOU!!')
else:
    print(f'Você errou, o número certo era {n}. PERDEU!!')

