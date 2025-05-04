print('='*20)
print('TEMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = 0
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{pt} -> ', end='')
        pt += r
        c += 1
        termo += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer? '))
print(f'Progressão finalizada com {termo} termos mostrados.')