import random

names = ['Maria', 'João', 'Lucas', 'Pedro']

random.shuffle(names)

print('Ordem de apresentação:')
for i, nome in enumerate(names, start=1):
    print(f'{i}. {nome}')