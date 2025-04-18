v = float(input('Velocidade do carro (km/h): '))

if v > 80:
    print(f'MULTADO!! \nSua multa é de R${(v-80) * 7}')
else:
    print('Velocidade aceita.')