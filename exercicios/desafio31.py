d = float(input('Distância da viagem: '))

if d <= 200:
    print(f'O valor da passagem é de {d * 0.5}')
else:
    print(f'O valor da passagem é de {d * 0.45}')