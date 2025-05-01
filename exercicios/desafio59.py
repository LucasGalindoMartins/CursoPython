from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))

op = 0

while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>>> Qual é sua opção? '))

    if op == 1:
        print(f'A soma entre {v1} + {v2} é {v1+v2}')

    elif op == 2:
        print(f'A multiplicação entre {v1} x {v2} é {v1*v2}')

    elif op == 3:
        if v1 > v2:
            print(f'Entre {v1} e {v2} o maior valor é {v1}')
        elif v2 > v1:
            print(f'Entre {v1} e {v2} o maior valor é {v2}')
        else:
            print('Os 2 números são iguais.')
    
    elif op == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))

    elif op == 5:
        print('Finalizando...')

    else:
        print('Opção inválido, tente novamente.')

    print('=-'*15)
    sleep(2)

print('Fim do programa! Volte sempre!')