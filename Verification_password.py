import re 


def password():
    global enter
    enter = input('Enter a password that has the following requeriments:\n' 
    '1° Your password must have uppercase and lowercase letters.\n'
    '2° Your password must have numbers.\n'
    '=> ')

    verification()

def verification():
         
        if re.search('[a-z]', enter) and re.search('[A-Z]', enter) and re.search('[0-9]', enter):
            print('Your password has been accepted')

        else:
            print("Your password has been refused")
            password


password()
