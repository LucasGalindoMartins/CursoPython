def area(l, c):
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {l*c:.1f} m2.')


print('Controle de Terrenos')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)