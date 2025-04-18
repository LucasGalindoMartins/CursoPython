pay = float(input('Qual o salário do funcionário? '))

if pay > 1250:
    print(f'Seu salário após o aumento é de {pay * 1.1:.2f}')
else:
    print(f'Seu salário após o aumento é de {pay * 1.15:.2f}')