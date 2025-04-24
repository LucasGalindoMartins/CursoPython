weight = float(input('Qual é o seu peso (kg): '))
height = float(input('Qual é sua altura (m): '))
imc = weight / (height**2)

print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print(f'Você está abaixo do peso normal')
elif imc < 25:
    print(f'PARABÉNS, você está no peso IDEAL!')
elif imc < 30:
    print('Você está com SOBREPESO. SE CUIDE!!')
elif imc < 40:
    print('Você está sofrendo de OBESIDADE.')
else:
    print('Você está sofrendo de OBESIDADE MÓRBIDA.')