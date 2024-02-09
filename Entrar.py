import os
import time
import re

contas = []
senhas = []

def pontinhos(mensagem, tempo_entre_pontos=1):
    print(mensagem, end='', flush=True)
    for _ in range(4):
        print('.', end='', flush=True)
        time.sleep(tempo_entre_pontos)
    print()  # Adicionando uma nova linha após os pontos

def tentativa(usuario, senha):
    if usuario not in contas or senha not in senhas:
        entrada = input('Seu Usuário ou Senha estão incorretos:\n'
                        '[L]ogar novamente\n'
                        '[R]egistrar\n').upper()

        if entrada == 'L':
            login()
            return False
        elif entrada == 'R':
            register()
            return False
    else:
        print('Você foi logado')
        return True

def login():
    print('===================================💲💲💲💲💲💲💲💲=====================================')
    print('                                 »»————-Ｌｏｇｉｎ————-««')
    usuario = input('Usuário: ')
    senha = input('Senha: ')
    print('=====================================💲💲💲💲💲💲💲💲=====================================')
    pontinhos('Logando')  # Chama a função pontinhos para exibir os pontos de espera
    if tentativa(usuario, senha):
        vc_entrou(usuario, senha)

def register():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        register_user = input('Digite um novo usuário: ')
        if len(register_user) < 5:
            print('O usuário tem que ter pelo menos 5 caracteres')
            continue

        register_senha = input('Digite uma nova senha: ')
        if len(register_senha) < 8 or not re.search('[0-9]', register_senha):
            print('A senha deve ter pelo menos 8 caracteres e conter pelo menos um número')
            continue

        os.system('cls' if os.name == 'nt' else 'clear')
        print('Sua conta foi criada:')
        print(f'Usuário: {register_user}\nSenha: {register_senha}')
        contas.append(register_user)
        senhas.append(register_senha)
        break
    entrar()

def entrar():
    print('===================================💲💲💲💲💲💲💲💲=====================================')
    print('                                    CENTRAL BANK')
    while True:
        opcao = input('Por favor! Escolha uma das opções abaixo:\n'
                      '[E]ntrar\n[R]egistrar\n').upper()
        
        if opcao == 'E':
            login()
            break
        elif opcao == 'R':
            register()
            break
        else:
            print('Por favor escolha apenas uma dessas opções!')

def vc_entrou(usuario, senha):
    if usuario in contas and senha in senhas:
        print('Você foi logado')
        menu0()

if __name__ == "__main__":
    entrar()
