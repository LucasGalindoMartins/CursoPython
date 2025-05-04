print('='*20)
print('TEMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = 0
c = 1
while c <= 10:
    print(f'{pt} -> ', end='')
    pt += r
    c += 1
    termo += 1
print('PAUSA')

encerrar = 1
while encerrar != 0:
    cont = 1
    encerrar = int(input('Quantos termos a mais você quer? '))
    while cont <= encerrar:
        print(f'{pt} -> ', end='')
        pt += r
        cont += 1
        termo += 1
    print('PAUSA')

print(f'Progressão finalizada com {termo} termos mostrados.')


    