import os 
import random


choices = {
    'pedra': {'vence': 'tesoura', 'perde': 'papel'},
    'papel': {'vence': 'pedra', 'perde': 'tesoura'},
    'tesoura': {'vence': 'papel', 'perde': 'pedra'}
}

while True:
    entrada = input('Pedra, Papel e Tesoura\n[S]tart\n[E]xit\nEscolha uma das opções: ').upper()

    if entrada == 'E':
        print('Obrigado pela atenção')
        break
    elif entrada != 'S':
        print('Digite uma das opções')
        continue

    entrada_2 = input('Escolha Pedra, Papel ou Tesoura: ').lower()

    if entrada_2 not in choices:
        print('Escolha inválida. Tente novamente.')
        continue

    bot = random.choice(list(choices.keys()))

    if entrada_2 == bot:
        print('Empate -_-')
    elif bot == choices[entrada_2]['vence']:
        print('Você Ganhou!!🎉🎉🎉')
    else:
        print('Você Perdeu >:P')
