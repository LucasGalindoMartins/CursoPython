# print('-'*30)
# n = int(input('Quer ver a tabuada de qual valor? '))
# print('-'*30)
# while n > 0:
#     for c in range(1, 11):
#         print(f'{n} x {c} = {n*c}')
#     print('-'*30)
#     n = int(input('Quer ver a tabuada de qual valor? '))
#     print('-'*30)
# print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# 2 JEITOS DIFERENTES