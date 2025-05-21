# valores = []
# par = []
# imp = []
# for v in range(1,8):
#     valores.append(int(input(f'Digite o {v}o. valor: ')))

# for v in valores:
#     if v % 2 == 0:
#         par.append(v)
#     else:
#         imp.append(v)
# print('-='*30)
# par.sort()
# print(f'Os valores pares digitados foram: {par}')
# imp.sort()
# print(f'Os valores ímpares digitados foram: {imp}')

#COM O PROFESSOR
num = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
num[1].sort()
print(f'Os valores ímpares digitados foram: {num[1]}')