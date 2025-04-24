print('='*10, 'LOJAS GALINDO','='*10)
price = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
op = int(input('Qual é a opção? '))

if op == 1:
    print(f'A vista você tem um desconto de 10%. O preço final fica R${price * 0.9}')
elif op == 2:
    print(print(f'A vista no cartão você tem um desconto de 5%. O preço final fica R${price * 0.95}'))
elif op == 3:
    print(f'Preço NORMAL. R${price}')
elif op  == 4:
    p = int(input('Quantas parcelas? '))
    pj = price * 1.2
    print(f'Sua compra será parcelada em {p}x de {pj/p:.2f} COM JUROS')
    print(f'Sua compra de R${price} vai custar R${pj:.2f} no final')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')