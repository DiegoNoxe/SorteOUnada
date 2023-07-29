def titulo():
    print()
    print('''                                   \033[1;33mSorte ou Nada''')
    print()
    print('Como funciona?')
    print()
    print('''A maquina e o usuario vão ter 3 números aleatorios sorteados e quem tiver
a maior soma entre os números vence\033[m''')
    print()
def config():
    print()
    global pc
    global jg
    try:
     jg = str(input('Nome jogador: '))
     pc = str(input('Nome maquina: '))
    except ValueError:
        print('Tente novamente em 2s')
        config()
def derrota_vitoria():
    if pc1 > jg1:
        print('Vitoria de {}!'.format(pc))
    elif pc1 < jg1:
        print('Vitoria de {}!'.format(jg))
    else:
        print('Empate!')
def sorteio():
    global pc1, jg1
    pc1 = []
    jg1 = []
    from random import randint
    pc2 = randint(0,10), randint(0,10), randint(0,10)
    jg2 = randint(0,10), randint(0,10), randint(0,10)
    pc1.append(pc2)
    jg1.append(jg2)
    print('Os números sorteados de {} foram: {}'.format(pc, pc2))
    print('Os números sorteados de {} foram: {}'.format(jg, jg2))
    print()
    print('''No total a soma de {} deu: {} | Enquanto a soma de {} deu: {}!'''.format(pc, sum(pc2), jg, sum(jg2)))
titulo()
config()
sorteio()
derrota_vitoria()
#Obviamente é possivel reduzir esse codigo, mas eu não sou pro não kk.
#Boa sorte.