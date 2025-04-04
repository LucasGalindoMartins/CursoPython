day = float(input('Número de dias que utilizou o carro: '))
km = float(input('Quantos km você percorreu com o carro: '))
precof = (day * 60) + (km * 0.15)
print(f'O total a pagar é de R${precof:.2f}')