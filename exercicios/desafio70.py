print('-'*70)
print('LOJA SUPER BARATÃO')
print('-'*70)
name = ' '
s = preco = contp = 0
menor = 1000000000000000

while True:
  name = input('Nome do Produto: ')
  preco = float(input('Preço: R$'))
  if preco < menor:
    menor = preco
  s += preco
  if preco > 1000:
    contp += 1
  r = ' '
  while r not in 'SN':
    r = input('Quer continuar? [S/N]').upper().strip()[0]
  if r == 'N':
    break
print('-'*15, 'FIM DO PROGRAMA', '-'*15)
print(f'O total da compra foi R${s:.2f}')
print(f'Quantidades de produtos custando mais de R$1000: {contp}')
print(f'Produto mais barato é: R${menor:.2f}')

# COM O PROFESSOR
# s = menor = contp = cont = 0
# barato = ''
# while True:
#   name = input('Nome do Produto: ')
#   preco = float(input('Preço: R$'))
#   cont += 1
#   s += preco
#   if preco > 1000:
#     contp += 1
#   if cont == 1 or preco < menor:
#     menor = preco
#     barato = name
#   r = ' '
#   while r not in 'SN':
#     r = input('Quer continuar? [S/N]').upper().strip()[0]
#   if r == 'N':
#     break
# print('-'*15, 'FIM DO PROGRAMA', '-'*15)
# print(f'O total da compra foi R${s:.2f}')
# print(f'Quantidades de produtos custando mais de R$1000: {contp}')
# print(f'Produto mais barato é {barato} que custou R${menor:.2f}')