print('='*20)
print('10 TEMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# d = pt + (10 - 1) * r


# while pt < d:
#     print(f'{pt} -> ', end='')
#     pt += r
# print('FIM')

cont = 1
while cont <= 10:
    print(f'{pt} -> ', end='')
    pt += r
    cont += 1
print('FIM')