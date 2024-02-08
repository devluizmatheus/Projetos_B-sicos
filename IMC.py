import os 
import random

while True:
    try:
        entrada = float(input('IMC\nDigite seu peso: '))
        entrada_2 = float(input('Digite sua altura: '))
        imc = entrada/(entrada ** 2)
        print(f'Seu IMC é {imc}')

    except ValueError:
        print('Digite números apenas.')

