# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = []
# galera.append(teste[:])

# teste[0] = 'Lucas'
# teste[1] = 20
# galera.append(teste[:])

# print(galera)



# galera = [['Lucas', 19], ['Gustavo', 40], ['Ester', 14], ['Maria', 54]]
# print(galera[0][0])
# print(galera[2][1])

# for p in galera:
#     print(f'{p[0]} tem {p[1]} de idade.')

totmai = totmen = 0
galera = []
dado = []
for c  in range(0,5):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print('-='*30)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} tem {p[1]} de idade. É maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} tem {p[1]} de idade. É menor de idade!')
        totmen += 1
print('-='*30)
print(f'Pessoas maiores de idade: {totmai}')
print(f'Pessoas menores de idade: {totmen}')