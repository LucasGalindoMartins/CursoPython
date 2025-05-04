print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print('~'*30)

# pt = 0
# s = 1
# prot = 1
# c = 1
# print(f'{pt} -> {prot} -> ', end='')
# while c <= termo-2:
#     s = pt+prot
#     print(f'{s} -> ', end='')
#     pt = prot
#     prot = s
#     c += 1
# print('FIM')
# print('~'*20)