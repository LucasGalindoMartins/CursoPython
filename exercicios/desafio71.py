print('='*40)
print(' '*14, 'BANCO CEV')
print('='*40)

valor = int(input('Qual valor você quer sacar: R$'))

c50 = valor // 50
resto = valor % 50

c20 = resto // 20
resto = resto % 20

c10 = resto // 10
resto = resto % 10

c1 = resto // 1

if c50 > 0:
  print(f'Total de cédulas de R$50: {c50}')
if c20 > 0:
  print(f'Total de cédulas de R$20: {c20}')
if c10 > 0:
  print(f'Total de cédulas de R$10: {c10}')
if c1 > 0:
  print(f'Total de cédulas de R$1: {c1}')

print('='* 40)
print('VOLTE SEMPRE AO BANCO CEV! TENHA UM BOM DIA!!')

#--- COM O PROFESSOR
# print('='*40)
# print(' '*14, 'BANCO CEV')
# print('='*40)

# valor = int(input('Qual valor você quer sacar: R$'))
# total = valor
# ced = 50
# totced = 0
# while True:
#   if total >= ced:
#     total -= ced
#     totced += 1
#   else:
#     if totced > 0:
#       print(f'Total de {totced} cédulas de R${ced}')
#     if ced == 50:
#       ced = 20
#     elif ced == 20:
#       ced = 10
#     elif ced == 10:
#       ced = 1
#     totced = 0
#     if total == 0:
#       break

# print('='* 40)
# print('VOLTE SEMPRE AO BANCO CEV! TENHA UM BOM DIA!!')