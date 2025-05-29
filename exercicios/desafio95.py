# jogador = {}
# gols = []
# elenco = []
# while True:
#     jogador.clear()
#     jogador['nome'] = input('Nome do jogador: ')
#     partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
#     for p in range(0, partidas):
#         gols.append(int(input(f'      Quantos gols na partida {p+1}?')))
#     tot = sum(gols)
#     jogador['gol'] = gols[:]
#     gols.clear()
#     jogador['total'] = tot

#     elenco.append(jogador.copy())

    # while  True:
    #     r = input('Quer continuar? [S/N] ').upper()[0]
    #     if r in 'SN':
    #         break
    #     print('ERRO! Por favor digitar S ou N.')
    # if r == 'N':
    #     break
# print('-='*30)
# print('cod  nome            gols        total')
# print('-'*60)
# c = 0
# for pos, j in enumerate(elenco):
#     print(pos, end='')
#     for k, v in j.items():
#         print(f'     {v}     ', end='')
#     print()
# while True:
#     print('-'*60)
#     dados = int(input('Mostrar dados de qual jogador? (999 para parar)'))
#     if dados == 999:
#         break
#     elif dados > len(elenco)-1:
#         print('Esse jogador não existe. Tente novamente')
#     else:
#         print(f'LEVANTAMENTO DO JOGADOR ')
#         for pos, g in enumerate(gols):
#             print(f'Na partida {pos+1}, marcou {g} gols.')

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    tot =  int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0 , tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while  True:
        r = input('Quer continuar? [S/N] ').upper()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor digitar S ou N.')
    if r == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*60)

while True:
    busca = int(input('Buscar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'    --  LEVANTAMENTO DO JOGADOR {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    => No jogo {i+1} fez {g} gols.')
    print('-'*60)
print('<< VOLTE SEMPRE >>')