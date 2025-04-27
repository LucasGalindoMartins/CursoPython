print('='*20)
print('10 TEMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = pt + (10 - 1) * r


for c in range(pt, d+r, r):
    print(f'{c} ->', end=' ')
print('ACABOU')