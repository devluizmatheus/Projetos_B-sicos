import os

def home():
    global inicio
    print(
        '============================================================\n'
        'Quizz de One Pice!!'
        'Regras:'
        '\n1° Digite apenas a alternativa\n'
        '2° São 3 perguntas\n'
        '3° Você terá apenas uma chance'
        '\n============================================================\n'
    )
    inicio = input('Deseja continuar?\n'
        '[S]im\n'
        '[N]ão\n'
        '==> '.upper()
)
def verificancao():
    if inicio == 'S':
        perguntas()
    elif inicio == 'N':
        os.system('cls')
        print('Obrigado pela atenção!!')
        
    else:
        os.system('cls')
        home()
    


def perguntas():
    global entrada
    entrada = input(
        'Quem é o caçador de marinheiros?\n'
        '[A] Roronoa Zoro\n'
        '[B] Ryuma\n'
        '[C] Donflamingo\n'
        '[D] Mihank\n'
        '[E] Crocodile\n'
        '=> '
).upper()
    resposta1()

    global entrada_2
    entrada_2 = input(
        '2° Pergunta: Quem são os irmãos do Luffy em One Pice?\n'
        '[A] Zoro e Sanji\n'
        '[B] Bon Clay e Nami\n'
        '[C] Ace e Sabo\n'
        '[D] Ace e Zoro\n'
        '[E] Ace e Koby\n'
        '=> '
).upper()
    resposta2()

    global entrada_3
    entrada_3 = input(
        '3° Pergunta quem Matou o Ace em One Pice?\n'
        '[A] Aokiji\n'
        '[B] Ankainu\n'
        '[C] Kizaru\n'
        '[D] Garp\n'
        '[E] Sengoku\n'
        '=> '
).upper()
    resposta3()
    
def resposta1():
    if entrada == 'D':
            print('Você acertou!!')
        
    else:
        print('Você errou....')

def resposta2():
    if entrada_2 == 'C':
        print('Você acerou!!')

    else:
        print('Você errou....')
def resposta3():
    if entrada_3 == 'B':
        print('Você acertou!!')
    else:
        print('Você errou....')

home()
