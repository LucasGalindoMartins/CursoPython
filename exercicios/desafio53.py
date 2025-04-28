frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''
inverso = junto[::-1]
# for letra in range(len(junto) - 1, -1,  -1):
#     inverso += junto[letra]

if inverso == junto:
    print(f'O inverso de {junto} é {inverso}. A frase digitada É um palíndromo!')
else:
    print(f'O inverso de {junto} é {inverso}. A frase digitada NÃO É um palíndromo!')