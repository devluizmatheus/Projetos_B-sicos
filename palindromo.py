import os
#while True:
try:
        entrada = str(input('Palindromos\nEscolha uma palavra para ver se é um palindromo: '))
        palavra_invertida = entrada[::-1]

        if entrada == palavra_invertida:
            print('Essa palavra é um palindromo')
        else:
            print('Essa palavra não é um palindromo')
except ValueError:
        print('Por favor! Digite uma palavra válida.')
