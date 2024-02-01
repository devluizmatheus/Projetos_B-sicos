import os
import random   


while True:
    entrada = input('▀▄▀▄▀▄🄳🄰🄳🄾🅂▀▄▀▄▀▄\nBem vindo a o simulador de dados! Deseja jogar:'
                    '\n[S]im\n[N]ão\n').upper()
    if entrada != 'S' and entrada != 'N':
        print('Escolha uma das opções')

    if entrada == 'N':
        print('Obrigado pela atenção')
        break
    if entrada == 'S':
        try:
            entrada_2 = int(input('Escolha quantos dados serão lançados: '))
            entrada_3 = int(input('Escolha quantas faces vai ter cada lado: '))
            for _ in range(entrada_2):
                print(random.randint(1, entrada_3))
                


        except ValueError:
            print('Digite um número válido')
