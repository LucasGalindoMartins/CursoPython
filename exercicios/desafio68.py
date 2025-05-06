from random import randint

print('=-'*30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*30)
c = s = 0

while True:
  comp = randint(0, 10)
  jog = int(input('Digite um valor: '))
  poi = input('Par ou ímpar? [P/I] ').strip().upper()[0]
  s = jog + comp

  if s % 2 == 0:
    parimpar = 'PAR'
  else:
    parimpar = 'ÍMPAR'
  print('-'*80)
  print(f'Você jogou {jog} e o computador jogou {comp}. Total de {s} DEU {parimpar}.')
  print('-'*80)

  if (s % 2 == 0 and poi == 'P') or (s % 2 == 1 and poi == 'I'):
    print('Você GANHOU!!')
    print('Vamos jogar novamente...')
    print('=-'*30)
    c += 1
  elif (s % 2 == 1 and poi == 'P') or (s % 2 == 0 and poi == 'I'):
    print('Você PERDEU!!')
    print('=-'*30)
    break
  elif poi not in 'PpIi':
    print('Você não escolheu a opção PAR OU IMPAR. Tente novamente.')
print(f'GAME OVER! Você venceu {c} vezes.')

# PROFESSOR
# print('=-'*30)
# print('VAMOS JOGAR PAR OU ÍMPAR')
# print('=-'*30)
# c = 0

# while True:
#   comp = randint(0, 10)
#   jog = int(input('Digite um valor: '))
#   s = jog + comp
#   tipo = ' '
#   while tipo not in 'PI':
#     tipo = input('Par ou ímpar? [P/I] ').strip().upper()[0]
#   print(f'Você jogou {jog} e o computador jogou {comp}. Total de {s} ', end='')
#   print('DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')

#   if tipo == 'P':
#     if s % 2 == 0:
#       print('Você VENCEU!!')
#       c += 1
#     else:
#       print('Você PERDEU!!')
#       break
#   elif tipo =='I':
#     if s % 2 == 1:
#       print('Você VENCEU!!')
#       c += 1
#     else:
#       print('Você PERDEU!!')
#       break
#   print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {c} vezes.')