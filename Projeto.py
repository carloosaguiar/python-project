#equipe: Carlos Eduardo Rodrigues de Aguiar

import matplotlib.pyplot as plt

games = ['God of War','GTA San Andreas','Sonic Unleashed','Super Mario World','Clash Royale','Among Us','League of Legends','Watch Dogs','Dark Souls','Shadow of Colossus']
nota = [9.3,9.2,8.9,9.6,8.0,7.6,7.9,7.8,8.9,9.3]
desenvolvedor = ['Santa Monica','Rockstar Games','Sega','Nintendo','Supercell','InnerSloth','Riot Games','Ubisoft','FromSoftware','SCE Japan Studio']
descricao = ['''A história centra-se em torno de seu personagem, Kratos, um guerreiro espartano enganado para matar sua esposa e filha por seu antigo mestre, o deus da guerra Ares.
Kratos mata Ares a mando da deusa Atena e toma seu lugar como o novo deus da guerra,
mas ainda é assombrado por pesadelos de seu passado.''', '''Ambientado no fim de 1992, a trama de San Andreas gira em torno de um membro de gangue, Carl "CJ" Johnson,
que retorna para seu lar em Los Santos, depois de uma longa temporada em Liberty City (a versão de Nova York do jogo),
após descobrir a morte de sua mãe.''', '''. O jogo traz personagens e elementos novos ao universo Sonic, como um dos antagonistas, Dark Gaia, o novo parceiro de Sonic, Chip,
e a oportunidade de controlar Sonic the Werehog, forma que o protagonista assume ao cair da noite.''', '''Em Super Mario World, Mario, Luigi e princesa Peach foram passar férias na ilha dos dinossauros, mas o terrível Bowser está causando confusões por lá, raptando ovos de dinossauros.
Mario e Luigi percorrem sete mundos até chegar no grande castelo de Bowser para resgatarem a princesa.''','''Em Clash Royale, o jogador precisa montar decks com poucas cartas e desafiar outros jogadores em partidas online. No começo, enfrentamos um tutorial, mas em seguida, o jogador estará por sua própria conta e risco em uma arena online.
As cartas são poucas, mas a sequência se repete durante os combates''','''Among Us é um jogo disponível para Android que tem conquistado jogadores por sua premissa simples: temos vários players em uma nave espacial, sendo que um deles é um impostor. O objetivo da tripulação é descobrir quem é esse impostor, para expulsá-lo de lá.
Fácil de entender, mas nem tão fácil de executar.''','''League of Legends é um jogo de estratégia em que duas equipes de cinco poderosos Campeões se enfrentam para destruir a base uma da outra.
Escolha entre mais de 140 Campeões para realizar jogadas épicas, assegurar abates e destruir torres conforme você luta até a vitória.''','''A história segue um homem chamado Aiden Pearce (voz de Noam Jenkins), um hacker "grey hat" altamente qualificado, descrito como uma pessoa que usa bem os "punhos e a inteligência."
Devido a uma "tragédia familiar violenta", Aiden procura fazer a sua própria justiça para com os culpados manipulando o ctOS.''','''Dark Souls se passa primariamente no reino fictício de Lordran,
onde os jogadores assumem o papel de um personagem denominado "Chosen Undead" que,
segundo lendas, seria responsável pela quebra de uma maldição que torna incapazes de morrer aqueles que são afligidos por uma misteriosa marca negra.''','''O enredo do jogo se concentra em um jovem chamado Wander, que deve viajar por uma terra proibida com o objetivo de derrotar dezesseis criaturas,
conhecidas simplesmente como "Colossi", para restaurar a vida de uma garota chamada Mono.''']

##########################FUNÇÔES#############################

def adcionar_game():
    print('▀▄▀▄▀▄' * 10)

    novo_game = input('Digite o nome do novo game: ')
    novo_nota = float(input('Digite a nota deste novo game: '))
    novo_desenvolvedor = input('Digite o nome do desenvolvedor do game: ')
    novo_descricao = input('Digite a descrição do game: ')
     
    games.append(novo_game)
    nota.append(novo_nota)
    desenvolvedor.append(novo_desenvolvedor)
    descricao.append(novo_descricao)

    print('Atualizando...')
    print('Agora nós temos {} games cadastrados'.format(len(games)))
    print(games)
    print('')

    print('▀▄▀▄▀▄' * 10)

def detalhes():
    print('▀▄▀▄▀▄' * 10)
    
    select = input('Digite o nome do game: ')

    if select in games:
        indice = games.index(select)
        print('Game: {}'.format(select))
        print('Nota do Game: {}'.format(nota[indice]))
        print('O desenvolvero(a) é {}'.format(desenvolvedor[indice]))
        print('Descrição: {}'.format(descricao[indice]))
    else:
        print('Esse game não está no catalogo. Nome invalido!')

    print('▀▄▀▄▀▄' * 10)

def estatisticas():
    print('▀▄▀▄▀▄' * 10)

    media = sum(nota)/len(nota)

    print('A maior nota dada entre os games foi {0}'.format(max(nota)))
    print('')
    print('A menor nota dada entre os games foi {0}'.format(min(nota)))
    print('')
    print('A media das notas entre os games foi {:.2f}'.format(media))

    print('▀▄▀▄▀▄' * 10)

def grafico():
    with plt.style.context('ggplot'):
        plt.title('Notas dos games')
        plt.xlabel('Games')
        plt.ylabel('Notas')
        plt.bar(games, nota)#gráfico de barras
        plt.show()

########################################################

print('''================================
=          MEUS GAMES          =
=========  FAVORITOS   =========
================================
''')

print('''Já estão cadastrados {} games que mais gostei:'''.format(len(games)))
print('')
print(games)

print('''
Já estão cadastrados {} notas dos games :'''.format(len(nota)))
print('')
print(nota)

print('''
Já estão cadastrados {} desenvolvedores dos games :'''.format(len(desenvolvedor)))
print('')
print(desenvolvedor)

print('''
Já estão cadastrados {} descrições dos games:'''.format(len(descricao)))
print('')
print(descricao)

print('''▀▄▀▄▀▄''' * 10)

input('''
Pressione ENTER para continuar...
''') 

opcao = ''

while opcao != 5:
    opcao = int(input('''Escolha uma das opções abaixo:
    [1] Adicionar um game ao catálogo.
    [2] Ver as estatisticas.
    [3] Ver os detalhes de um game.
    [4] Mostra graficos comparativos.
    [5] Sair do programa.
    Qual opção você vai escolher:  
    '''))

    if opcao == 1:
        adcionar_game()

    elif opcao == 2:
        estatisticas()
    
    elif opcao == 3:
        detalhes()

    elif opcao == 4:
        grafico()    

print('Obrigado por usar meu programa. ( ͡▀̿ ̿ ͜ʖ ͡▀̿ ̿ )')