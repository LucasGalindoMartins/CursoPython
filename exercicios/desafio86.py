# p1 = []
# p2 = []
# p3 = []

# for c in range(0,3):
#     v = int(input(f'Digite um valor para [0, {c}]: '))
#     p1.append(v)

# for c in range(0,3):
#     v = int(input(f'Digite um valor para [1, {c}]: '))
#     p2.append(v)

# for c in range(0,3):
#     v = int(input(f'Digite um valor para [2, {c}]: '))
#     p3.append(v)

# print('-='*30)
# for c in range(0,3):
#     print(f'[  {p1[c]}  ]', end='')
# print()
# for c in range(0,3):
#     print(f'[  {p2[c]}  ]', end='')
# print()
# for c in range(0,3):
#     print(f'[  {p3[c]}  ]', end='')

#COM O PROFESSOR
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]:^5', end='')
    print()
