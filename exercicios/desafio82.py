valores = []
contp = []
conti = []
while True:
    valores.append(int(input('Digite um número: ')))

    r = ' '
    while r not in 'NnSs':
        r = input('Quer continuar? [S/N]').upper()
    if r == 'N':
        break
print('-='*30)
print(f'A lista completa é {valores}')
for v in valores:
    if v % 2 == 0:
        contp.append(v)
    else:
        conti.append(v)
print(f'A lista de pares é {contp}')
print(f'A lista de ímpares é {conti}')
