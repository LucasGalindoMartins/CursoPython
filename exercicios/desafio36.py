value = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salário? '))
y = int(input('Em quantos anos você vai pagar a casa? '))
pres = value / (y*12)

print(f'Para pagar uma casa de R${value} em {y} anos a prestação será de R${pres:.2f}')

if pres > (sal * 0.3):
    print(f'\033[31mInfelizmente seu emprésimo foi NEGADO!!\033[m')
else:
    print('\033[32mSeu empréstimo foi APROVADO!!\033[m')   