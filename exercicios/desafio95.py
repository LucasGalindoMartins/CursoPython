jogador = {}
gols = []
elenco = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'      Quantos gols na partida {p+1}?')))
    tot = sum(gols)
    jogador['gol'] = gols[:]
    gols.clear()
    jogador['total'] = tot

    elenco.append(jogador.copy())

    while  True:
        r = input('Quer continuar? [S/N] ').upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor digitar S ou N.')
    if r == 'N':
        break
print('-='*30)
print('cod  nome            gols        total')
print('-'*60)
c = 0
for pos, j in enumerate(elenco):
    print(pos, end='')
    for k, v in j.items():
        print(f'     {v}     ', end='')
    print()
while True:
    print('-'*60)
    dados = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if dados == 999:
        break
    elif dados > len(elenco)-1:
        print('Esse jogador não existe. Tente novamente')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {elenco[dados][jogador["nome"]]}')
