r = 'S'
c = maior = s = menor = 0

while r in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = input('Quer continuar? [S/N] ').strip()[0]
m = s/c
print(f'Você digitou {c} números e a média foi {m:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
    