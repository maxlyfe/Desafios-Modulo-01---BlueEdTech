import random
vitoriasUsuario = 0
vitoriasPc = 0
escolaspc = ['pedra','papel','tesoura']
rodadas = int(input('Quantas rodadas vamos jogar?\n'))
for r in range(rodadas):
    usuario = input('Escolhe, pedra, papel ou tesoura:\n')
    pc = random.choice(escolaspc)
    print(f'Computador escolheu: \n{pc}')
    print()
    if usuario == 'pedra':
        if pc == 'tesoura':
            vitoriasUsuario +=1
        elif pc == 'papel':
            vitoriasPc +=1
        else:
            pass
    if usuario == 'papel':
        if pc == 'pedra':
            vitoriasUsuario +=1
        elif pc == 'tesoura':
            vitoriasPc +=1
        else:
            pass
    if usuario == 'tesoura':
        if pc == 'papel':
            vitoriasUsuario +=1
        elif pc == 'pedra':
            vitoriasPc +=1
        else:
            pass
    pc = 0
    r +=1
if vitoriasUsuario > vitoriasPc:
    print(f'Você ganhou com {vitoriasUsuario} pontos')
elif vitoriasPc > vitoriasUsuario:
    print(f'Você perdeu, o computador fez {vitoriasPc} pontos')
elif vitoriasPc == vitoriasUsuario:
    print('Vocês empataram, joga novamente para ver quem ganha desta vez.')
print()
print(f'Você ganhou {vitoriasUsuario} jogos e computador ganhou {vitoriasPc}.')