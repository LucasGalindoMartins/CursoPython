from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        print(f'Contagam de {i} até {f} de {p} em {p}')
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!!')
    else:
        print(f'Contagam de {i} até {f} de {p} em {p}')
        for c in range(i, f-1, -p):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!!')
        


print('-='*30)
contador(1, 10, 1)
print('-='*30)
contador(10, 0, -2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print('-='*30)
contador(i, f, p)