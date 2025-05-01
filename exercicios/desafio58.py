from random import randint

comp = randint(0, 10)
# cont = 1

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

# --------------FEITO POR MIM-----------------------
# palpite = int(input('Qual seu palpite? ')) 

# while palpite != comp:
#     if comp > palpite:
#         print('Mais... Tente mais uma vez.')
#         palpite = int(input('Qual seu palpite? '))
#         cont += 1
#     elif comp < palpite:
#         print('Menos... Tente mais uma vez.')
#         palpite = int(input('Qual seu palpite? '))
#         cont += 1

# if palpite == comp:
#     print(f'Acertou com {cont} tentativas. Parabéns!')

#-------------COM O PROFESSOR-------------------
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    cont += 1
    if jogador ==  comp:
        acertou = True
    else: 
        if jogador < comp:
            print('Mais.. Tente mais uma vez.')
        elif jogador > comp:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {cont} tentativas. Parabéns!!')


